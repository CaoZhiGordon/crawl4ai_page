#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
深度网站爬取器 - 用户友好的运行脚本

这个脚本提供了一个简单的界面来配置和运行深度网站爬取器。
您可以通过修改下面的配置来自定义爬取行为。

使用方法:
1. 修改下方的 CRAWL_CONFIGS 配置
2. 运行: python run_deep_crawler.py
"""

import asyncio
import sys
from pathlib import Path

# 导入我们的深度爬取器
try:
    from deep_website_crawler import DeepWebsiteCrawler, CrawlConfig
except ImportError:
    print("❌ 无法导入 deep_website_crawler，请确保文件在同一目录下")
    sys.exit(1)

# 🎯 爬取配置 - 在这里自定义您的爬取设置
CRAWL_CONFIGS = {
    # PyOD 官方文档网站
    "pyod_docs": CrawlConfig(
        start_url="https://pyod.readthedocs.io/en/latest/index.html",
        max_depth=3,              # 爬取深度：3层
        max_pages=100,            # 最大页面数：100页
        concurrent_limit=3,       # 并发数：3个同时进行
        delay=1.5,                # 每次请求间隔：1.5秒
        same_domain_only=True,    # 只爬取同域名页面
        output_dir="pyod_website_crawl", # 输出目录
        merge_markdown=True,      # 生成合并的markdown文档
        word_count_threshold=10,  # 最小词数阈值
        # 额外的排除模式（可选）
        exclude_patterns=[
            r'\.pdf$', r'\.jpg$', r'\.png$', r'\.gif$', 
            r'/search\?', r'/genindex', r'/modindex',
            r'/_static/', r'/_sources/'
        ]
    ),
    
    # 其他网站示例配置
    "example_blog": CrawlConfig(
        start_url="https://example-blog.com",
        max_depth=2,
        max_pages=50,
        concurrent_limit=2,
        delay=2.0,
        same_domain_only=True,
        output_dir="example_blog_crawl",
        merge_markdown=True,
        include_patterns=[r'/blog/', r'/post/']  # 只包含博客文章
    ),
    
    "custom_site": CrawlConfig(
        start_url="https://your-target-site.com",
        max_depth=2,
        max_pages=30,
        concurrent_limit=2,
        delay=1.0,
        same_domain_only=True,
        output_dir="custom_site_crawl",
        merge_markdown=True
    )
}

def print_banner():
    """显示程序横幅"""
    print("🌐" + "=" * 58 + "🌐")
    print("          深度网站爬取器 - Deep Website Crawler")
    print("                   基于 crawl4ai 构建")
    print("🌐" + "=" * 58 + "🌐")

def print_config_info(config_name: str, config: CrawlConfig):
    """显示配置信息"""
    print(f"\n📋 爬取配置: {config_name}")
    print("-" * 50)
    print(f"🎯 起始URL: {config.start_url}")
    print(f"🏗️  最大深度: {config.max_depth} 层")
    print(f"📄 最大页面: {config.max_pages} 页")
    print(f"⚡ 并发数: {config.concurrent_limit} 个")
    print(f"⏱️  请求延时: {config.delay} 秒")
    print(f"🌐 同域限制: {'是' if config.same_domain_only else '否'}")
    print(f"📁 输出目录: {config.output_dir}")
    print(f"📝 合并文档: {'是' if config.merge_markdown else '否'}")

def select_config() -> tuple[str, CrawlConfig]:
    """让用户选择配置"""
    print("\n🎯 可用的爬取配置:")
    print("-" * 30)
    
    configs_list = list(CRAWL_CONFIGS.items())
    for i, (name, config) in enumerate(configs_list, 1):
        domain = config.start_url.split('/')[2] if '//' in config.start_url else config.start_url
        print(f"{i}. {name} - {domain}")
    
    while True:
        try:
            choice = input(f"\n请选择配置 (1-{len(configs_list)}) 或按 Enter 使用默认配置 [1]: ").strip()
            
            if not choice:  # 默认选择第一个
                choice = 1
            else:
                choice = int(choice)
            
            if 1 <= choice <= len(configs_list):
                selected = configs_list[choice - 1]
                return selected[0], selected[1]
            else:
                print(f"❌ 请输入 1-{len(configs_list)} 之间的数字")
                
        except ValueError:
            print("❌ 请输入有效的数字")
        except KeyboardInterrupt:
            print("\n👋 再见!")
            sys.exit(0)

def confirm_crawl(config_name: str, config: CrawlConfig) -> bool:
    """确认开始爬取"""
    print_config_info(config_name, config)
    
    print(f"\n⚠️  注意事项:")
    print(f"• 请遵守网站的robots.txt和使用条款")
    print(f"• 爬取可能需要 {config.max_pages * config.delay / 60:.1f} 分钟或更长时间")
    print(f"• 请确保您有权限爬取目标网站")
    
    while True:
        try:
            confirm = input("\n❓ 确定开始爬取？(y/N): ").strip().lower()
            if confirm in ['y', 'yes', '是', 'ok']:
                return True
            elif confirm in ['n', 'no', '否', ''] or not confirm:
                return False
            else:
                print("请输入 y 或 n")
        except KeyboardInterrupt:
            print("\n👋 再见!")
            sys.exit(0)

async def run_crawler(config_name: str, config: CrawlConfig):
    """运行爬取器"""
    print(f"\n🚀 开始爬取: {config_name}")
    print("=" * 60)
    
    try:
        crawler = DeepWebsiteCrawler(config)
        
        # 开始爬取
        results = await crawler.crawl_website()
        
        # 生成合并文档
        if config.merge_markdown and results:
            await crawler.generate_merged_markdown()
        
        # 显示最终结果
        print(f"\n" + "🎉" + "=" * 58 + "🎉")
        print(f"           爬取任务完成！")
        print(f"✅ 成功爬取: {len(results)} 个页面")
        print(f"📁 结果保存在: {config.output_dir}/")
        print(f"📝 主要文件:")
        print(f"   • {config.output_dir}/merged_website_content.md (合并文档)")
        print(f"   • {config.output_dir}/html/ (HTML文件)")
        print(f"   • {config.output_dir}/markdown/ (单页面MD文件)")
        print(f"   • {config.output_dir}/metadata/ (元数据)")
        print("🎉" + "=" * 58 + "🎉")
        
        return True
        
    except KeyboardInterrupt:
        print("\n⛔ 爬取被用户中断")
        return False
    except Exception as e:
        print(f"\n❌ 爬取过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
        return False

def show_usage_examples():
    """显示使用示例"""
    print(f"\n💡 使用示例:")
    print("-" * 20)
    print("1. 爬取PyOD官方文档：")
    print("   选择配置 1 (pyod_docs)")
    print("   将生成完整的PyOD文档markdown版本")
    
    print("\n2. 自定义网站爬取：")
    print("   修改 CRAWL_CONFIGS 中的 'custom_site' 配置")
    print("   设置您想爬取的网站URL和参数")
    
    print("\n3. 添加新配置：")
    print("   在 CRAWL_CONFIGS 中添加新的配置项")
    print("   设置URL、深度、页面数等参数")

async def main():
    """主函数"""
    print_banner()
    
    # 检查依赖
    try:
        import crawl4ai
        import aiohttp
        from bs4 import BeautifulSoup
    except ImportError as e:
        print(f"\n❌ 缺少依赖: {e}")
        print("请安装所需依赖:")
        print("pip install crawl4ai aiohttp beautifulsoup4")
        sys.exit(1)
    
    show_usage_examples()
    
    try:
        # 让用户选择配置
        config_name, config = select_config()
        
        # 确认爬取
        if confirm_crawl(config_name, config):
            # 开始爬取
            success = await run_crawler(config_name, config)
            
            if success:
                print(f"\n🎯 任务完成！查看 {config.output_dir}/ 目录获取结果")
            else:
                print(f"\n😞 任务未能完成")
        else:
            print("\n👋 任务已取消，再见！")
    
    except KeyboardInterrupt:
        print(f"\n👋 程序被中断，再见！")

if __name__ == "__main__":
    # 运行主程序
    asyncio.run(main())

