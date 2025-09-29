#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
深度网站爬取脚本
使用 crawl4ai 实现对任意网站的深度爬取，并将结果合并为完整的markdown项目

功能特性：
- 递归爬取网站的所有子页面
- 智能链接发现和过滤
- 避免重复爬取
- 并发爬取支持
- 生成完整的markdown文档
- 支持深度限制和域名过滤
- 进度实时显示

作者: AI Assistant
版本: 1.0
基于: crawl4ai
"""

import asyncio
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Set, List, Dict, Any, Optional, Tuple
from urllib.parse import urljoin, urlparse, urlunparse
from dataclasses import dataclass, field

try:
    from crawl4ai import AsyncWebCrawler
    import aiohttp
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"❌ 导入错误: {e}")
    print("请安装所需依赖: pip install crawl4ai aiohttp beautifulsoup4")
    sys.exit(1)

@dataclass
class CrawlConfig:
    """爬取配置类"""
    start_url: str
    max_depth: int = 3
    max_pages: int = 100
    concurrent_limit: int = 5
    delay: float = 1.0
    same_domain_only: bool = True
    include_patterns: List[str] = field(default_factory=list)
    exclude_patterns: List[str] = field(default_factory=list)
    output_dir: str = "deep_crawl_results"
    merge_markdown: bool = True
    word_count_threshold: int = 10
    
    def __post_init__(self):
        # 默认排除模式：常见的非内容链接
        if not self.exclude_patterns:
            self.exclude_patterns = [
                r'\.pdf$', r'\.jpg$', r'\.png$', r'\.gif$', r'\.svg$',
                r'\.css$', r'\.js$', r'\.xml$', r'\.json$',
                r'/search\?', r'/login', r'/logout', r'/register',
                r'/admin', r'/api/', r'#', r'javascript:',
                r'\.zip$', r'\.rar$', r'\.exe$', r'\.dmg$'
            ]

@dataclass
class PageResult:
    """单个页面爬取结果"""
    url: str
    title: str
    markdown: str
    html: str
    links: List[str]
    metadata: Dict[str, Any]
    depth: int
    timestamp: datetime
    success: bool
    error: Optional[str] = None

class DeepWebsiteCrawler:
    """深度网站爬取器"""
    
    def __init__(self, config: CrawlConfig):
        self.config = config
        self.visited_urls: Set[str] = set()
        self.pending_urls: Set[str] = set()
        self.results: Dict[str, PageResult] = {}
        self.semaphore = asyncio.Semaphore(config.concurrent_limit)
        self.session = None
        
        # 设置输出目录
        self.setup_output_directory()
        
        # 获取目标域名
        self.target_domain = urlparse(config.start_url).netloc
        
        print(f"🚀 初始化深度爬取器")
        print(f"📍 起始URL: {config.start_url}")
        print(f"🌐 目标域名: {self.target_domain}")
        print(f"📊 配置: 最大深度={config.max_depth}, 最大页面={config.max_pages}")
    
    def setup_output_directory(self):
        """设置输出目录"""
        try:
            # 创建主目录和子目录
            dirs = [
                self.config.output_dir,
                f"{self.config.output_dir}/pages",
                f"{self.config.output_dir}/html",
                f"{self.config.output_dir}/markdown", 
                f"{self.config.output_dir}/metadata"
            ]
            
            for dir_path in dirs:
                os.makedirs(dir_path, exist_ok=True)
            
            print(f"✅ 输出目录已准备: {self.config.output_dir}")
        except Exception as e:
            print(f"❌ 创建输出目录失败: {e}")
            sys.exit(1)
    
    def normalize_url(self, url: str, base_url: str) -> Optional[str]:
        """规范化URL"""
        try:
            # 处理相对链接
            url = urljoin(base_url, url)
            
            # 解析URL
            parsed = urlparse(url)
            
            # 移除fragment（锚点）
            parsed = parsed._replace(fragment='')
            
            # 重新组合URL
            normalized = urlunparse(parsed)
            
            return normalized
        except Exception:
            return None
    
    def is_valid_url(self, url: str, depth: int) -> bool:
        """检查URL是否应该被爬取"""
        try:
            # 基本检查
            if not url or url in self.visited_urls:
                return False
            
            # 深度检查
            if depth > self.config.max_depth:
                return False
            
            # 页面数量限制
            if len(self.visited_urls) >= self.config.max_pages:
                return False
            
            parsed = urlparse(url)
            
            # 域名检查
            if self.config.same_domain_only and parsed.netloc != self.target_domain:
                return False
            
            # 协议检查
            if parsed.scheme not in ['http', 'https']:
                return False
            
            # 排除模式检查
            for pattern in self.config.exclude_patterns:
                if re.search(pattern, url, re.IGNORECASE):
                    return False
            
            # 包含模式检查（如果有指定）
            if self.config.include_patterns:
                for pattern in self.config.include_patterns:
                    if re.search(pattern, url, re.IGNORECASE):
                        break
                else:
                    return False
            
            return True
            
        except Exception as e:
            print(f"⚠️ URL验证错误 {url}: {e}")
            return False
    
    def extract_links_from_content(self, html: str, base_url: str) -> List[str]:
        """从HTML内容中提取链接"""
        links = []
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            # 提取所有链接
            for link_tag in soup.find_all('a', href=True):
                href = link_tag['href'].strip()
                if href:
                    normalized = self.normalize_url(href, base_url)
                    if normalized and normalized not in links:
                        links.append(normalized)
            
            print(f"🔗 从页面提取到 {len(links)} 个链接")
            return links
            
        except Exception as e:
            print(f"⚠️ 提取链接失败: {e}")
            return []
    
    async def crawl_single_page(self, url: str, depth: int) -> Optional[PageResult]:
        """爬取单个页面"""
        async with self.semaphore:
            try:
                print(f"🌐 正在爬取 (深度 {depth}): {url}")
                
                async with AsyncWebCrawler(verbose=False) as crawler:
                    result = await crawler.arun(
                        url=url,
                        word_count_threshold=self.config.word_count_threshold,
                        exclude_external_links=False,
                        process_iframes=True,
                        remove_overlay_elements=True
                    )
                
                if not result.success:
                    print(f"❌ 爬取失败: {url} - {result.error_message}")
                    return PageResult(
                        url=url, title="", markdown="", html="", links=[],
                        metadata={}, depth=depth, timestamp=datetime.now(),
                        success=False, error=result.error_message
                    )
                
                # 提取链接
                links = self.extract_links_from_content(result.html, url)
                valid_links = [link for link in links if self.is_valid_url(link, depth + 1)]
                
                # 添加新发现的链接到待处理队列
                for link in valid_links:
                    if link not in self.visited_urls:
                        self.pending_urls.add(link)
                
                # 创建页面结果
                page_result = PageResult(
                    url=url,
                    title=result.metadata.get('title', '无标题'),
                    markdown=result.markdown,
                    html=result.html,
                    links=valid_links,
                    metadata=result.metadata,
                    depth=depth,
                    timestamp=datetime.now(),
                    success=True
                )
                
                # 保存单页结果
                await self.save_page_result(page_result)
                
                print(f"✅ 爬取完成: {url} (标题: {page_result.title[:50]}...)")
                print(f"📄 内容长度: {len(result.markdown)} 字符, 发现链接: {len(valid_links)} 个")
                
                # 添加延时
                if self.config.delay > 0:
                    await asyncio.sleep(self.config.delay)
                
                return page_result
                
            except Exception as e:
                print(f"❌ 爬取页面时发生错误 {url}: {e}")
                return PageResult(
                    url=url, title="", markdown="", html="", links=[],
                    metadata={}, depth=depth, timestamp=datetime.now(),
                    success=False, error=str(e)
                )
    
    async def save_page_result(self, result: PageResult):
        """保存单个页面的结果"""
        try:
            # 生成文件名
            timestamp = result.timestamp.strftime("%Y%m%d_%H%M%S")
            domain = urlparse(result.url).netloc.replace('.', '_')
            safe_path = re.sub(r'[^\w\-_.]', '_', urlparse(result.url).path)[:50]
            base_name = f"{timestamp}_{domain}_{safe_path}"
            
            # 保存HTML
            html_path = f"{self.config.output_dir}/html/{base_name}.html"
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(result.html)
            
            # 保存Markdown
            md_path = f"{self.config.output_dir}/markdown/{base_name}.md"
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {result.title}\n\n")
                f.write(f"**URL:** {result.url}\n\n")
                f.write(f"**爬取时间:** {result.timestamp}\n\n")
                f.write(f"**深度:** {result.depth}\n\n")
                f.write("---\n\n")
                f.write(result.markdown)
            
            # 保存元数据
            metadata_path = f"{self.config.output_dir}/metadata/{base_name}_metadata.json"
            metadata = {
                'url': result.url,
                'title': result.title,
                'depth': result.depth,
                'timestamp': result.timestamp.isoformat(),
                'success': result.success,
                'error': result.error,
                'links_count': len(result.links),
                'markdown_length': len(result.markdown),
                'html_length': len(result.html),
                'metadata': result.metadata,
                'files': {
                    'html': html_path,
                    'markdown': md_path,
                    'metadata': metadata_path
                }
            }
            
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            print(f"⚠️ 保存页面结果失败 {result.url}: {e}")
    
    async def crawl_website(self) -> Dict[str, PageResult]:
        """开始深度爬取网站"""
        print(f"\n🚀 开始深度爬取网站")
        print("=" * 60)
        
        start_time = time.time()
        
        # 添加起始URL
        self.pending_urls.add(self.config.start_url)
        
        current_depth = 0
        
        while self.pending_urls and current_depth <= self.config.max_depth:
            # 获取当前深度的URL
            current_batch = []
            for url in list(self.pending_urls):
                if len(self.visited_urls) >= self.config.max_pages:
                    break
                if url not in self.visited_urls:
                    current_batch.append((url, current_depth))
                    self.visited_urls.add(url)
                    self.pending_urls.discard(url)
            
            if not current_batch:
                current_depth += 1
                continue
            
            print(f"\n📊 爬取深度 {current_depth}: {len(current_batch)} 个页面")
            print("-" * 40)
            
            # 并发爬取当前批次
            tasks = [
                self.crawl_single_page(url, depth) 
                for url, depth in current_batch
            ]
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # 处理结果
            for result in results:
                if isinstance(result, PageResult) and result.success:
                    self.results[result.url] = result
                elif isinstance(result, Exception):
                    print(f"❌ 任务异常: {result}")
            
            # 显示进度
            success_count = len([r for r in results if isinstance(r, PageResult) and r.success])
            print(f"✅ 深度 {current_depth} 完成: {success_count}/{len(current_batch)} 页面成功")
            
            current_depth += 1
        
        elapsed_time = time.time() - start_time
        
        print(f"\n🎉 网站爬取完成!")
        print(f"📊 总计爬取: {len(self.results)} 个页面")
        print(f"⏱️ 总耗时: {elapsed_time:.2f} 秒")
        print(f"💾 结果保存在: {self.config.output_dir}")
        
        return self.results
    
    async def generate_merged_markdown(self) -> str:
        """生成合并的markdown文档"""
        if not self.config.merge_markdown or not self.results:
            return ""
        
        print(f"\n📝 生成合并的markdown文档...")
        
        # 按深度和URL排序
        sorted_results = sorted(
            self.results.values(), 
            key=lambda x: (x.depth, x.url)
        )
        
        # 构建markdown内容
        merged_content = []
        
        # 添加文档头部
        merged_content.append(f"# 深度爬取项目: {self.target_domain}\n")
        merged_content.append(f"**起始URL:** {self.config.start_url}\n")
        merged_content.append(f"**爬取时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        merged_content.append(f"**总页面数:** {len(self.results)}\n")
        merged_content.append(f"**最大深度:** {self.config.max_depth}\n\n")
        
        # 生成目录
        merged_content.append("## 📋 目录\n")
        for i, result in enumerate(sorted_results, 1):
            indent = "  " * result.depth
            title = result.title[:80] + "..." if len(result.title) > 80 else result.title
            merged_content.append(f"{indent}{i}. [{title}](#{i}-{result.depth})\n")
        merged_content.append("\n---\n\n")
        
        # 添加每个页面的内容
        for i, result in enumerate(sorted_results, 1):
            merged_content.append(f"## {i}. {result.title} {{#{i}-{result.depth}}}\n\n")
            merged_content.append(f"**URL:** {result.url}\n")
            merged_content.append(f"**深度:** {result.depth}\n")
            merged_content.append(f"**爬取时间:** {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            if result.markdown:
                # 调整markdown标题级别，避免冲突
                adjusted_markdown = result.markdown
                # 将原有的h1-h6标题都增加2级
                for level in range(6, 0, -1):
                    old_header = '#' * level + ' '
                    new_header = '#' * (level + 2) + ' '
                    adjusted_markdown = adjusted_markdown.replace(old_header, new_header)
                
                merged_content.append(adjusted_markdown)
            else:
                merged_content.append("*（此页面无内容）*\n")
            
            merged_content.append("\n---\n\n")
        
        # 添加统计信息
        merged_content.append("## 📊 爬取统计\n\n")
        total_chars = sum(len(r.markdown) for r in self.results.values())
        by_depth = {}
        for result in self.results.values():
            by_depth[result.depth] = by_depth.get(result.depth, 0) + 1
        
        merged_content.append(f"- 总页面数: {len(self.results)}\n")
        merged_content.append(f"- 总字符数: {total_chars:,}\n")
        merged_content.append("- 各深度页面分布:\n")
        for depth in sorted(by_depth.keys()):
            merged_content.append(f"  - 深度 {depth}: {by_depth[depth]} 页面\n")
        
        final_content = ''.join(merged_content)
        
        # 保存合并的markdown
        merged_path = f"{self.config.output_dir}/merged_website_content.md"
        with open(merged_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"✅ 合并文档已生成: {merged_path}")
        print(f"📄 文档大小: {len(final_content):,} 字符")
        
        return final_content

async def main():
    """主函数"""
    print("🌐 深度网站爬取工具")
    print("=" * 40)
    
    # 这里可以通过命令行参数或配置文件设置
    # 示例配置：爬取 PyOD 官网
    config = CrawlConfig(
        start_url="https://pyod.readthedocs.io/en/latest/index.html",
        max_depth=3,
        max_pages=50,
        concurrent_limit=3,
        delay=2.0,  # 增加延时以避免被封
        same_domain_only=True,
        output_dir="pyod_website_crawl",
        merge_markdown=True,
        word_count_threshold=10
    )
    
    crawler = DeepWebsiteCrawler(config)
    
    try:
        # 开始爬取
        results = await crawler.crawl_website()
        
        # 生成合并文档
        if config.merge_markdown:
            await crawler.generate_merged_markdown()
        
        print(f"\n🎉 深度爬取任务完成！")
        print(f"✅ 成功爬取 {len(results)} 个页面")
        print(f"📁 结果保存在: {config.output_dir}")
        
    except KeyboardInterrupt:
        print("\n⛔ 用户中断操作")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # 运行主程序
    asyncio.run(main())

