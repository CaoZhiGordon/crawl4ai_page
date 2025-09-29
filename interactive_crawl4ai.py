#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Crawl4AI 交互式程序
功能完整的网页爬取工具，集成官方文档的所有主要功能

作者: AI Assistant
版本: 1.0
基于: Crawl4AI v0.7.4 官方文档
"""

import asyncio
import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path

try:
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
    from crawl4ai.extraction_strategy import LLMExtractionStrategy, CosineStrategy, JsonCssExtractionStrategy
    from crawl4ai.chunking_strategy import RegexChunking, NlpSentenceChunking
    from crawl4ai.content_filter_strategy import BM25ContentFilter
    # 导入分页相关的配置类
    try:
        from crawl4ai.config import VirtualScrollConfig
    except ImportError:
        # 如果没有VirtualScrollConfig，我们将使用字典配置
        VirtualScrollConfig = None
except ImportError as e:
    print(f"❌ 导入错误: {e}")
    print("请确保已安装 crawl4ai: pip install crawl4ai")
    sys.exit(1)

class InteractiveCrawl4AI:
    """交互式 Crawl4AI 主类"""
    
    def __init__(self):
        self.session_data = {}
        self.results_history = []
        self.config_file = "crawl4ai_config.json"
        self.results_dir = "crawl4ai_results"
        self.profiles_dir = "browser_profiles"
        self.auto_save_enabled = True
        self.load_config()
        self.setup_results_directory()
        self.setup_profiles_directory()
    
    def setup_results_directory(self):
        """创建结果保存目录"""
        try:
            os.makedirs(self.results_dir, exist_ok=True)
            # 创建子目录
            subdirs = ['html', 'markdown', 'json', 'screenshots', 'extracted']
            for subdir in subdirs:
                os.makedirs(os.path.join(self.results_dir, subdir), exist_ok=True)
            print(f"✅ 结果保存目录已准备: {self.results_dir}")
        except Exception as e:
            print(f"⚠️ 创建结果目录失败: {e}")
    
    def setup_profiles_directory(self):
        """创建浏览器配置文件目录"""
        try:
            os.makedirs(self.profiles_dir, exist_ok=True)
            print(f"✅ 浏览器配置文件目录已准备: {self.profiles_dir}")
        except Exception as e:
            print(f"⚠️ 创建配置文件目录失败: {e}")
    
    def load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.session_data = json.load(f)
                self.auto_save_enabled = self.session_data.get('auto_save_results', True)
                print(f"✅ 已加载配置文件: {self.config_file}")
            except Exception as e:
                print(f"⚠️ 加载配置文件失败: {e}")
                self.session_data = {}
    
    def save_config(self):
        """保存配置文件"""
        try:
            self.session_data['auto_save_results'] = self.auto_save_enabled
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.session_data, f, ensure_ascii=False, indent=2)
            print(f"✅ 配置已保存到: {self.config_file}")
        except Exception as e:
            print(f"⚠️ 保存配置失败: {e}")
    
    def save_crawl_result(self, result, url, crawl_type="basic", extra_data=None):
        """实时保存爬取结果"""
        if not self.auto_save_enabled:
            return None
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            domain = url.split('/')[2].replace(':', '_').replace('.', '_')
            base_filename = f"{timestamp}_{domain}_{crawl_type}"
            
            saved_files = []
            
            # 保存HTML
            if hasattr(result, 'html') and result.html:
                html_file = os.path.join(self.results_dir, 'html', f"{base_filename}.html")
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(result.html)
                saved_files.append(html_file)
            
            # 保存Markdown
            if hasattr(result, 'markdown') and result.markdown:
                md_file = os.path.join(self.results_dir, 'markdown', f"{base_filename}.md")
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(result.markdown)
                saved_files.append(md_file)
            
            # 保存提取的内容
            if hasattr(result, 'extracted_content') and result.extracted_content:
                extracted_file = os.path.join(self.results_dir, 'extracted', f"{base_filename}_extracted.json")
                with open(extracted_file, 'w', encoding='utf-8') as f:
                    if isinstance(result.extracted_content, str):
                        json.dump({"content": result.extracted_content}, f, ensure_ascii=False, indent=2)
                    else:
                        json.dump(result.extracted_content, f, ensure_ascii=False, indent=2)
                saved_files.append(extracted_file)
            
            # 保存截图
            if hasattr(result, 'screenshot') and result.screenshot:
                screenshot_file = os.path.join(self.results_dir, 'screenshots', f"{base_filename}.png")
                with open(screenshot_file, 'wb') as f:
                    f.write(result.screenshot)
                saved_files.append(screenshot_file)
            
            # 保存元数据和统计信息
            metadata = {
                'timestamp': datetime.now().isoformat(),
                'url': url,
                'crawl_type': crawl_type,
                'success': result.success if hasattr(result, 'success') else True,
                'status_code': result.status_code if hasattr(result, 'status_code') else None,
                'title': result.metadata.get('title', 'N/A') if hasattr(result, 'metadata') else 'N/A',
                'html_length': len(result.html) if hasattr(result, 'html') else 0,
                'markdown_length': len(result.markdown) if hasattr(result, 'markdown') else 0,
                'links_count': {
                    'internal': len(result.links.get('internal', [])) if hasattr(result, 'links') else 0,
                    'external': len(result.links.get('external', [])) if hasattr(result, 'links') else 0
                },
                'media_count': {
                    'images': len(result.media.get('images', [])) if hasattr(result, 'media') else 0,
                    'videos': len(result.media.get('videos', [])) if hasattr(result, 'media') else 0
                },
                'saved_files': saved_files
            }
            
            if extra_data:
                metadata.update(extra_data)
            
            # 保存元数据
            metadata_file = os.path.join(self.results_dir, 'json', f"{base_filename}_metadata.json")
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
            saved_files.append(metadata_file)
            
            print(f"💾 结果已自动保存 ({len(saved_files)} 个文件):")
            for file_path in saved_files:
                print(f"  📁 {os.path.basename(file_path)}")
            
            return {
                'base_filename': base_filename,
                'saved_files': saved_files,
                'metadata_file': metadata_file
            }
            
        except Exception as e:
            print(f"⚠️ 自动保存失败: {e}")
            return None
    
    def create_browser_profile(self, profile_name, description=""):
        """创建新的浏览器配置文件"""
        try:
            profile_path = os.path.join(self.profiles_dir, profile_name)
            os.makedirs(profile_path, exist_ok=True)
            
            # 保存配置文件元数据
            metadata = {
                'name': profile_name,
                'description': description,
                'created': datetime.now().isoformat(),
                'last_used': None,
                'usage_count': 0,
                'websites': []
            }
            
            metadata_file = os.path.join(profile_path, 'profile_metadata.json')
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
            
            print(f"✅ 浏览器配置文件已创建: {profile_name}")
            return profile_path
            
        except Exception as e:
            print(f"⚠️ 创建配置文件失败: {e}")
            return None
    
    def list_browser_profiles(self):
        """列出所有浏览器配置文件"""
        try:
            profiles = []
            if os.path.exists(self.profiles_dir):
                for item in os.listdir(self.profiles_dir):
                    profile_path = os.path.join(self.profiles_dir, item)
                    if os.path.isdir(profile_path):
                        metadata_file = os.path.join(profile_path, 'profile_metadata.json')
                        if os.path.exists(metadata_file):
                            with open(metadata_file, 'r', encoding='utf-8') as f:
                                metadata = json.load(f)
                                profiles.append(metadata)
            return profiles
        except Exception as e:
            print(f"⚠️ 获取配置文件列表失败: {e}")
            return []
    
    def update_profile_usage(self, profile_name, website_url):
        """更新配置文件使用记录"""
        try:
            profile_path = os.path.join(self.profiles_dir, profile_name)
            metadata_file = os.path.join(profile_path, 'profile_metadata.json')
            
            if os.path.exists(metadata_file):
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                
                metadata['last_used'] = datetime.now().isoformat()
                metadata['usage_count'] = metadata.get('usage_count', 0) + 1
                
                # 记录访问的网站
                if website_url not in metadata.get('websites', []):
                    if 'websites' not in metadata:
                        metadata['websites'] = []
                    metadata['websites'].append(website_url)
                
                with open(metadata_file, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, ensure_ascii=False, indent=2)
                    
        except Exception as e:
            print(f"⚠️ 更新配置文件使用记录失败: {e}")
    
    def get_browser_config(self, profile_name=None, **kwargs):
        """获取浏览器配置"""
        config_params = {
            'headless': kwargs.get('headless', False),  # 默认非无头模式以便登录
            'browser_type': kwargs.get('browser_type', 'chromium'),
            'use_persistent_context': True,
            'ignore_https_errors': True,
            'java_script_enabled': True,
            'viewport_width': kwargs.get('viewport_width', 1920),
            'viewport_height': kwargs.get('viewport_height', 1080)
        }
        
        if profile_name:
            profile_path = os.path.join(self.profiles_dir, profile_name)
            config_params['user_data_dir'] = profile_path
        
        # 添加其他自定义参数
        for key, value in kwargs.items():
            if key not in config_params:
                config_params[key] = value
        
        return BrowserConfig(**config_params)
    
    def display_banner(self):
        """显示程序横幅"""
        print("=" * 80)
        print("🚀 Crawl4AI 交互式网页爬取工具")
        print("📚 集成官方文档的完整功能 | 版本 1.0")
        print("🔗 基于: https://docs.crawl4ai.com/")
        print("=" * 80)
    
    def display_main_menu(self):
        """显示主菜单"""
        auto_save_status = "✅开启" if self.auto_save_enabled else "❌关闭"
        print(f"\n📋 主菜单 (自动保存: {auto_save_status}):")
        print("1. 基础网页爬取")
        print("2. 高级爬取配置")
        print("3. 结构化数据提取")
        print("4. LLM 智能提取")
        print("5. 批量URL处理")
        print("6. JavaScript渲染")
        print("7. 内容过滤和清理")
        print("8. 自动翻页爬取")
        print("9. 导出和保存")
        print("10. 会话管理")
        print("11. 搜索历史记录")
        print("12. 浏览器配置文件管理")
        print("13. 管理自动保存")
        print("14. 设置和配置")
        print("15. 帮助和文档")
        print("0. 退出程序")
        print("-" * 50)
    
    async def basic_crawl(self):
        """基础网页爬取功能"""
        print("\n🚀 基础网页爬取")
        print("=" * 40)
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        # 全页滚动选项
        print("\n是否启用全页滚动 (适用于动态加载内容的网站):")
        print("1. 否 (普通爬取)")
        print("2. 是 (模拟滚动到底部，加载所有动态内容)")
        
        scroll_choice = input("请选择 (1-2): ").strip()
        scan_full_page = scroll_choice == "2"
        
        scroll_delay = 0.2  # 默认滚动延迟
        if scan_full_page:
            delay_input = input("滚动延迟时间 (秒，默认0.2): ").strip()
            if delay_input and delay_input.replace('.', '').isdigit():
                scroll_delay = float(delay_input)
        
        # 基础选项
        print("\n选择输出格式:")
        print("1. HTML (原始)")
        print("2. 清洁文本")
        print("3. Markdown")
        print("4. 全部")
        
        format_choice = input("请选择 (1-4): ").strip()
        
        try:
            async with AsyncWebCrawler(verbose=True) as crawler:
                # 构建爬取参数
                crawl_params = {'url': url}
                if scan_full_page:
                    crawl_params['scan_full_page'] = True
                    crawl_params['scroll_delay'] = scroll_delay
                    print(f"🔄 启用全页滚动，延迟: {scroll_delay}秒")
                
                result = await crawler.arun(**crawl_params)
                
                if result.success:
                    print(f"\n✅ 爬取成功!")
                    print(f"📄 页面标题: {result.metadata.get('title', 'N/A')}")
                    print(f"🌐 URL: {result.url}")
                    print(f"📊 状态码: {result.status_code}")
                    print(f"⏱️ 处理时间: {result.metadata.get('processing_time', 'N/A')}")
                    
                    # 根据选择显示内容
                    if format_choice == "1" or format_choice == "4":
                        print(f"\n📝 HTML内容 ({len(result.html)} 字符):")
                        print("-" * 30)
                        print(result.html[:500] + "..." if len(result.html) > 500 else result.html)
                    
                    if format_choice == "2" or format_choice == "4":
                        print(f"\n🧹 清洁文本 ({len(result.cleaned_html)} 字符):")
                        print("-" * 30)
                        print(result.cleaned_html[:500] + "..." if len(result.cleaned_html) > 500 else result.cleaned_html)
                    
                    if format_choice == "3" or format_choice == "4":
                        print(f"\n📋 Markdown ({len(result.markdown)} 字符):")
                        print("-" * 30)
                        print(result.markdown[:500] + "..." if len(result.markdown) > 500 else result.markdown)
                    
                    # 显示链接和媒体信息
                    print(f"\n🔗 链接统计:")
                    print(f"  内部链接: {len(result.links.get('internal', []))}")
                    print(f"  外部链接: {len(result.links.get('external', []))}")
                    print(f"🖼️ 媒体统计:")
                    print(f"  图片: {len(result.media.get('images', []))}")
                    print(f"  视频: {len(result.media.get('videos', []))}")
                    
                    # 实时保存结果
                    save_info = self.save_crawl_result(result, url, 'basic_crawl')
                    
                    # 保存到历史
                    history_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'type': 'basic_crawl',
                        'success': True,
                        'title': result.metadata.get('title', 'N/A')
                    }
                    if save_info:
                        history_entry['saved_files'] = save_info['saved_files']
                        history_entry['base_filename'] = save_info['base_filename']
                    self.results_history.append(history_entry)
                    
                else:
                    print(f"❌ 爬取失败: {result.error_message}")
                    
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    async def advanced_crawl(self):
        """高级爬取配置"""
        print("\n⚙️ 高级爬取配置")
        print("=" * 40)
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        # 高级配置选项
        print("\n🔧 配置选项:")
        
        # 用户代理
        custom_ua = input("自定义User-Agent (回车使用默认): ").strip()
        
        # 等待时间
        wait_time = input("页面加载等待时间/秒 (默认3): ").strip()
        wait_time = int(wait_time) if wait_time.isdigit() else 3
        
        # 延迟时间
        delay = input("请求延迟时间/秒 (默认1): ").strip()
        delay = float(delay) if delay.replace('.', '').isdigit() else 1.0
        
        # 缓存选项
        bypass_cache = input("绕过缓存? (y/N): ").strip().lower() == 'y'
        
        # 处理iframe
        process_iframes = input("处理iframe? (y/N): ").strip().lower() == 'y'
        
        # 移除覆盖元素
        remove_overlay = input("移除覆盖元素? (y/N): ").strip().lower() == 'y'
        
        # 截图
        take_screenshot = input("截取屏幕截图? (y/N): ").strip().lower() == 'y'
        
        try:
            crawler_kwargs = {
                'verbose': True
            }
            
            if custom_ua:
                crawler_kwargs['user_agent'] = custom_ua
            
            arun_kwargs = {
                'url': url,
                'wait_for': f'sleep:{wait_time}',
                'delay_before_return_html': delay,
                'bypass_cache': bypass_cache,
                'process_iframes': process_iframes,
                'remove_overlay_elements': remove_overlay,
                'screenshot': take_screenshot
            }
            
            async with AsyncWebCrawler(**crawler_kwargs) as crawler:
                result = await crawler.arun(**arun_kwargs)
                
                if result.success:
                    print(f"\n✅ 高级爬取成功!")
                    print(f"📄 页面标题: {result.metadata.get('title', 'N/A')}")
                    print(f"📊 HTML长度: {len(result.html)}")
                    print(f"📝 清洁文本长度: {len(result.cleaned_html)}")
                    print(f"📋 Markdown长度: {len(result.markdown)}")
                    
                    if take_screenshot and hasattr(result, 'screenshot'):
                        print(f"📸 截图已保存")
                    
                    # 实时保存结果
                    extra_data = {
                        'config': {
                            'wait_time': wait_time,
                            'delay': delay,
                            'bypass_cache': bypass_cache,
                            'process_iframes': process_iframes,
                            'remove_overlay': remove_overlay,
                            'screenshot': take_screenshot
                        }
                    }
                    save_info = self.save_crawl_result(result, url, 'advanced_crawl', extra_data)
                    
                    # 保存到历史
                    history_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'type': 'advanced_crawl',
                        'success': True,
                        'config': extra_data['config']
                    }
                    if save_info:
                        history_entry['saved_files'] = save_info['saved_files']
                        history_entry['base_filename'] = save_info['base_filename']
                    self.results_history.append(history_entry)
                    
                else:
                    print(f"❌ 爬取失败: {result.error_message}")
                    
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    async def structured_extraction(self):
        """结构化数据提取"""
        print("\n🎯 结构化数据提取")
        print("=" * 40)
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        print("\n选择提取策略:")
        print("1. CSS选择器提取")
        print("2. JSON+CSS提取")
        print("3. 余弦相似度提取")
        
        strategy_choice = input("请选择 (1-3): ").strip()
        
        try:
            async with AsyncWebCrawler(verbose=True) as crawler:
                extraction_strategy = None
                
                if strategy_choice == "1":
                    # CSS选择器提取
                    selector = input("请输入CSS选择器: ").strip()
                    if selector:
                        result = await crawler.arun(
                            url=url,
                            css_selector=selector
                        )
                        
                elif strategy_choice == "2":
                    # JSON+CSS提取
                    schema = {}
                    print("定义提取模式 (输入空行结束):")
                    while True:
                        key = input("字段名: ").strip()
                        if not key:
                            break
                        selector = input(f"{key}的CSS选择器: ").strip()
                        if selector:
                            schema[key] = selector
                    
                    if schema:
                        extraction_strategy = JsonCssExtractionStrategy(schema)
                        result = await crawler.arun(
                            url=url,
                            extraction_strategy=extraction_strategy
                        )
                
                elif strategy_choice == "3":
                    # 余弦相似度提取
                    query = input("请输入查询关键词: ").strip()
                    if query:
                        extraction_strategy = CosineStrategy(
                            semantic_filter=query,
                            word_count_threshold=10,
                            max_dist=0.2,
                            linkage_method='ward',
                            top_k=3
                        )
                        result = await crawler.arun(
                            url=url,
                            extraction_strategy=extraction_strategy
                        )
                
                else:
                    # 默认基础提取
                    result = await crawler.arun(url=url)
                
                if result.success:
                    print(f"\n✅ 结构化提取成功!")
                    print(f"📄 页面标题: {result.metadata.get('title', 'N/A')}")
                    
                    if result.extracted_content:
                        print(f"📊 提取的内容:")
                        print("-" * 30)
                        if isinstance(result.extracted_content, str):
                            print(result.extracted_content[:1000] + "..." if len(result.extracted_content) > 1000 else result.extracted_content)
                        else:
                            print(json.dumps(result.extracted_content, ensure_ascii=False, indent=2)[:1000])
                    
                    # 实时保存结果
                    extra_data = {'strategy': strategy_choice}
                    save_info = self.save_crawl_result(result, url, 'structured_extraction', extra_data)
                    
                    # 保存到历史
                    history_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'type': 'structured_extraction',
                        'strategy': strategy_choice,
                        'success': True
                    }
                    if save_info:
                        history_entry['saved_files'] = save_info['saved_files']
                        history_entry['base_filename'] = save_info['base_filename']
                    self.results_history.append(history_entry)
                    
                else:
                    print(f"❌ 提取失败: {result.error_message}")
                    
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    async def llm_extraction(self):
        """LLM 智能提取"""
        print("\n🤖 LLM 智能提取")
        print("=" * 40)
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        # LLM配置
        print("\n🧠 LLM配置:")
        api_token = input("请输入API Token (OpenAI/其他): ").strip()
        if not api_token:
            print("❌ 需要API Token才能使用LLM功能")
            return
        
        model_name = input("模型名称 (默认gpt-3.5-turbo): ").strip()
        if not model_name:
            model_name = "gpt-3.5-turbo"
        
        instruction = input("提取指令 (例如: 提取所有产品信息): ").strip()
        if not instruction:
            instruction = "提取页面的主要内容和关键信息"
        
        try:
            extraction_strategy = LLMExtractionStrategy(
                provider="openai",
                api_token=api_token,
                model=model_name,
                instruction=instruction
            )
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                result = await crawler.arun(
                    url=url,
                    extraction_strategy=extraction_strategy
                )
                
                if result.success:
                    print(f"\n✅ LLM提取成功!")
                    print(f"📄 页面标题: {result.metadata.get('title', 'N/A')}")
                    
                    if result.extracted_content:
                        print(f"🤖 LLM提取结果:")
                        print("-" * 30)
                        print(result.extracted_content)
                    
                    # 实时保存结果
                    extra_data = {
                        'model': model_name,
                        'instruction': instruction
                    }
                    save_info = self.save_crawl_result(result, url, 'llm_extraction', extra_data)
                    
                    # 保存到历史
                    history_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'type': 'llm_extraction',
                        'model': model_name,
                        'instruction': instruction,
                        'success': True
                    }
                    if save_info:
                        history_entry['saved_files'] = save_info['saved_files']
                        history_entry['base_filename'] = save_info['base_filename']
                    self.results_history.append(history_entry)
                    
                else:
                    print(f"❌ LLM提取失败: {result.error_message}")
                    
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    async def batch_crawl(self):
        """批量URL处理"""
        print("\n📊 批量URL处理")
        print("=" * 40)
        
        print("输入URL列表 (每行一个，输入空行结束):")
        urls = []
        while True:
            url = input().strip()
            if not url:
                break
            urls.append(url)
        
        if not urls:
            print("❌ 没有输入任何URL")
            return
        
        print(f"📋 将处理 {len(urls)} 个URL")
        
        # 并发设置
        max_concurrent = input("最大并发数 (默认3): ").strip()
        max_concurrent = int(max_concurrent) if max_concurrent.isdigit() else 3
        
        try:
            async with AsyncWebCrawler(verbose=True) as crawler:
                results = []
                semaphore = asyncio.Semaphore(max_concurrent)
                
                async def crawl_single(url):
                    async with semaphore:
                        try:
                            result = await crawler.arun(url=url)
                            return result
                        except Exception as e:
                            print(f"❌ 处理 {url} 时出错: {e}")
                            return None
                
                # 并发处理
                tasks = [crawl_single(url) for url in urls]
                results = await asyncio.gather(*tasks)
                
                # 统计结果
                success_count = sum(1 for r in results if r and r.success)
                
                print(f"\n✅ 批量处理完成!")
                print(f"📊 成功: {success_count}/{len(urls)}")
                
                for i, result in enumerate(results):
                    if result and result.success:
                        print(f"  ✅ {urls[i]} - 成功 (标题: {result.metadata.get('title', 'N/A')[:50]})")
                    else:
                        print(f"  ❌ {urls[i]} - 失败")
                
                # 批量保存结果
                for i, result in enumerate(results):
                    if result and result.success:
                        self.save_crawl_result(result, urls[i], 'batch_crawl')
                
                # 保存到历史
                self.results_history.append({
                    'timestamp': datetime.now().isoformat(),
                    'type': 'batch_crawl',
                    'urls': urls,
                    'success_count': success_count,
                    'total_count': len(urls)
                })
                
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    async def javascript_rendering(self):
        """JavaScript渲染"""
        print("\n🌐 JavaScript渲染")
        print("=" * 40)
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        # 全页滚动选项
        print("\n是否启用全页滚动 (适用于动态加载内容的网站):")
        print("1. 否 (使用下面的JavaScript操作)")
        print("2. 是 (模拟滚动到底部，加载所有动态内容)")
        
        scroll_choice = input("请选择 (1-2): ").strip()
        scan_full_page = scroll_choice == "2"
        
        scroll_delay = 0.2  # 默认滚动延迟
        if scan_full_page:
            delay_input = input("滚动延迟时间 (秒，默认0.2): ").strip()
            if delay_input and delay_input.replace('.', '').isdigit():
                scroll_delay = float(delay_input)
        
        js_choice = None
        if not scan_full_page:
            print("\n选择JavaScript操作:")
            print("1. 等待元素加载")
            print("2. 执行自定义JS代码")
            print("3. 点击元素")
            print("4. 滚动页面")
            
            js_choice = input("请选择 (1-4): ").strip()
        
        try:
            arun_kwargs = {'url': url}
            
            # 添加全页滚动参数
            if scan_full_page:
                arun_kwargs['scan_full_page'] = True
                arun_kwargs['scroll_delay'] = scroll_delay
                print(f"🔄 启用全页滚动，延迟: {scroll_delay}秒")
                print("💡 注意: 滚动过程中浏览器窗口会自动向下滚动以加载动态内容")
            
            if js_choice == "1":
                # 等待元素
                selector = input("等待的元素CSS选择器: ").strip()
                timeout = input("超时时间/秒 (默认10): ").strip()
                timeout = int(timeout) if timeout.isdigit() else 10
                
                if selector:
                    arun_kwargs['wait_for'] = f"css:{selector}"
                    arun_kwargs['page_timeout'] = timeout * 1000
                    
            elif js_choice == "2":
                # 执行JS代码
                js_code = input("请输入JavaScript代码: ").strip()
                if js_code:
                    arun_kwargs['js_code'] = [js_code]
                    
            elif js_choice == "3":
                # 点击元素
                selector = input("要点击的元素CSS选择器: ").strip()
                if selector:
                    js_code = f"document.querySelector('{selector}').click();"
                    arun_kwargs['js_code'] = [js_code]
                    arun_kwargs['wait_for'] = 'sleep:2'
                    
            elif js_choice == "4":
                # 滚动页面
                scroll_type = input("滚动类型 (bottom/top): ").strip().lower()
                if scroll_type == "bottom":
                    js_code = "window.scrollTo(0, document.body.scrollHeight);"
                else:
                    js_code = "window.scrollTo(0, 0);"
                arun_kwargs['js_code'] = [js_code]
                arun_kwargs['wait_for'] = 'sleep:2'
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                result = await crawler.arun(**arun_kwargs)
                
                if result.success:
                    print(f"\n✅ JavaScript渲染成功!")
                    print(f"📄 页面标题: {result.metadata.get('title', 'N/A')}")
                    print(f"📊 HTML长度: {len(result.html)}")
                    print(f"📝 文本长度: {len(result.cleaned_html)}")
                    
                    # 实时保存结果
                    extra_data = {'js_operation': js_choice}
                    save_info = self.save_crawl_result(result, url, 'javascript_rendering', extra_data)
                    
                    # 保存到历史
                    history_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'type': 'javascript_rendering',
                        'js_operation': js_choice,
                        'success': True
                    }
                    if save_info:
                        history_entry['saved_files'] = save_info['saved_files']
                        history_entry['base_filename'] = save_info['base_filename']
                    self.results_history.append(history_entry)
                    
                else:
                    print(f"❌ 渲染失败: {result.error_message}")
                    
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    async def content_filtering(self):
        """内容过滤和清理"""
        print("\n🔍 内容过滤和清理")
        print("=" * 40)
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        print("\n选择过滤选项:")
        print("1. 基础清理")
        print("2. BM25内容过滤")
        print("3. 自定义标签过滤")
        
        filter_choice = input("请选择 (1-3): ").strip()
        
        try:
            arun_kwargs = {'url': url}
            
            if filter_choice == "2":
                # BM25过滤
                query = input("BM25查询关键词: ").strip()
                if query:
                    content_filter = BM25ContentFilter(query)
                    arun_kwargs['content_filter'] = content_filter
                    
            elif filter_choice == "3":
                # 自定义标签过滤
                excluded_tags = input("要排除的HTML标签 (逗号分隔): ").strip()
                if excluded_tags:
                    tags = [tag.strip() for tag in excluded_tags.split(',')]
                    arun_kwargs['excluded_tags'] = tags
            
            # 其他清理选项
            remove_overlay = input("移除覆盖元素? (y/N): ").strip().lower() == 'y'
            if remove_overlay:
                arun_kwargs['remove_overlay_elements'] = True
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                result = await crawler.arun(**arun_kwargs)
                
                if result.success:
                    print(f"\n✅ 内容过滤成功!")
                    print(f"📄 页面标题: {result.metadata.get('title', 'N/A')}")
                    print(f"📊 原始HTML长度: {len(result.html)}")
                    print(f"🧹 清洁文本长度: {len(result.cleaned_html)}")
                    print(f"📋 Markdown长度: {len(result.markdown)}")
                    
                    # 显示清理后的内容预览
                    print(f"\n📝 清洁内容预览:")
                    print("-" * 30)
                    preview = result.cleaned_html[:500] + "..." if len(result.cleaned_html) > 500 else result.cleaned_html
                    print(preview)
                    
                    # 实时保存结果
                    extra_data = {'filter_type': filter_choice}
                    save_info = self.save_crawl_result(result, url, 'content_filtering', extra_data)
                    
                    # 保存到历史
                    history_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'type': 'content_filtering',
                        'filter_type': filter_choice,
                        'success': True
                    }
                    if save_info:
                        history_entry['saved_files'] = save_info['saved_files']
                        history_entry['base_filename'] = save_info['base_filename']
                    self.results_history.append(history_entry)
                    
                else:
                    print(f"❌ 过滤失败: {result.error_message}")
                    
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    async def pagination_crawl(self):
        """自动翻页爬取功能"""
        print("\n📄 自动翻页爬取")
        print("=" * 40)
        print("支持多种翻页策略，适用于各种动态内容网站")
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        print("\n选择翻页策略:")
        print("1. 虚拟滚动 (无限滚动网站，如社交媒体)")
        print("2. 点击按钮翻页 (传统翻页按钮)")
        print("3. JavaScript注入翻页 (自定义脚本)")
        print("4. 分页URL模式 (URL参数翻页)")
        print("5. 智能混合模式 (自动检测最佳策略)")
        
        strategy_choice = input("请选择策略 (1-5): ").strip()
        
        if strategy_choice == "1":
            await self._virtual_scroll_crawl(url)
        elif strategy_choice == "2":
            await self._button_click_crawl(url)
        elif strategy_choice == "3":
            await self._javascript_injection_crawl(url)
        elif strategy_choice == "4":
            await self._url_pattern_crawl(url)
        elif strategy_choice == "5":
            await self._smart_hybrid_crawl(url)
        else:
            print("❌ 无效选择")
    
    async def _virtual_scroll_crawl(self, url: str):
        """虚拟滚动翻页策略"""
        print("\n🔄 虚拟滚动翻页配置")
        print("-" * 30)
        
        # 配置参数
        max_pages = input("最大滚动次数 (默认10): ").strip()
        max_pages = int(max_pages) if max_pages.isdigit() else 10
        
        scroll_delay = input("滚动间隔时间/秒 (默认2): ").strip()
        scroll_delay = float(scroll_delay) if scroll_delay.replace('.', '').isdigit() else 2.0
        
        scroll_distance = input("单次滚动距离/像素 (默认1000): ").strip()
        scroll_distance = int(scroll_distance) if scroll_distance.isdigit() else 1000
        
        # 停止条件
        print("\n停止条件设置:")
        print("1. 固定滚动次数")
        print("2. 检测到底部")
        print("3. 内容不再变化")
        print("4. 指定关键词出现")
        
        stop_condition = input("选择停止条件 (1-4): ").strip()
        
        target_keyword = ""
        if stop_condition == "4":
            target_keyword = input("输入目标关键词: ").strip()
        
        try:
            # 构建虚拟滚动配置
            if VirtualScrollConfig:
                # 使用官方配置类
                scroll_config = VirtualScrollConfig(
                    pages=max_pages,
                    delay=scroll_delay,
                    scroll_distance=scroll_distance
                )
                crawler_config = {'virtual_scroll_config': scroll_config}
            else:
                # 使用字典配置
                crawler_config = {
                    'virtual_scroll': {
                        'enabled': True,
                        'pages': max_pages,
                        'delay': scroll_delay,
                        'scroll_distance': scroll_distance,
                        'stop_condition': stop_condition,
                        'target_keyword': target_keyword
                    }
                }
            
            print(f"\n🚀 开始虚拟滚动爬取...")
            print(f"📊 配置: {max_pages}次滚动, 间隔{scroll_delay}秒, 距离{scroll_distance}px")
            
            all_content = []
            page_count = 0
            previous_content_hash = ""
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                for page in range(max_pages):
                    print(f"\n🔄 第 {page + 1}/{max_pages} 次滚动...")
                    
                    # 构建JavaScript滚动命令
                    js_scroll_command = f"""
                    // 滚动到指定位置
                    window.scrollBy(0, {scroll_distance});
                    
                    // 等待内容加载
                    await new Promise(resolve => setTimeout(resolve, {scroll_delay * 1000}));
                    
                    // 检查是否到达底部
                    const isAtBottom = (window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100;
                    
                    // 返回页面信息
                    return {{
                        scrolled: true,
                        isAtBottom: isAtBottom,
                        currentScroll: window.scrollY,
                        bodyHeight: document.body.offsetHeight,
                        newContent: document.body.innerText.length
                    }};
                    """
                    
                    # 执行爬取
                    result = await crawler.arun(
                        url=url,
                        js_code=js_scroll_command,
                        wait_for=f"sleep:{scroll_delay}",
                        bypass_cache=True
                    )
                    
                    if result.success:
                        # 内容去重检查
                        current_content_hash = hash(result.cleaned_html)
                        if current_content_hash == previous_content_hash:
                            print("🛑 内容未变化，停止滚动")
                            break
                        
                        previous_content_hash = current_content_hash
                        page_count += 1
                        
                        # 保存当前页面内容
                        page_data = {
                            'page': page + 1,
                            'url': result.url,
                            'title': result.metadata.get('title', 'N/A'),
                            'content_length': len(result.cleaned_html),
                            'markdown_length': len(result.markdown),
                            'links_count': len(result.links.get('internal', [])) + len(result.links.get('external', [])),
                            'images_count': len(result.media.get('images', [])),
                            'html': result.html,
                            'cleaned_html': result.cleaned_html,
                            'markdown': result.markdown,
                            'links': result.links,
                            'media': result.media,
                            'metadata': result.metadata
                        }
                        
                        all_content.append(page_data)
                        
                        print(f"✅ 第{page + 1}页爬取成功")
                        print(f"📄 内容长度: {len(result.cleaned_html)}")
                        print(f"🔗 链接数: {page_data['links_count']}")
                        print(f"🖼️ 图片数: {page_data['images_count']}")
                        
                        # 检查停止条件
                        if stop_condition == "2":
                            # 检测是否到达底部（通过JavaScript返回值）
                            if hasattr(result, 'js_result') and result.js_result.get('isAtBottom'):
                                print("🛑 已到达页面底部，停止滚动")
                                break
                        
                        elif stop_condition == "4" and target_keyword:
                            if target_keyword.lower() in result.cleaned_html.lower():
                                print(f"🎯 发现目标关键词 '{target_keyword}'，停止滚动")
                                break
                        
                        # 暂停以避免过快请求
                        await asyncio.sleep(scroll_delay)
                        
                    else:
                        print(f"❌ 第{page + 1}页爬取失败: {result.error_message}")
                        break
            
            # 合并结果并保存
            if all_content:
                await self._save_pagination_results(url, all_content, "virtual_scroll", {
                    'strategy': 'virtual_scroll',
                    'max_pages': max_pages,
                    'scroll_delay': scroll_delay,
                    'scroll_distance': scroll_distance,
                    'stop_condition': stop_condition,
                    'actual_pages': page_count
                })
                
                print(f"\n🎉 虚拟滚动爬取完成!")
                print(f"📊 总共爬取了 {page_count} 页")
                print(f"📄 总内容长度: {sum(len(p['cleaned_html']) for p in all_content)}")
                print(f"🔗 总链接数: {sum(p['links_count'] for p in all_content)}")
                print(f"🖼️ 总图片数: {sum(p['images_count'] for p in all_content)}")
            else:
                print("❌ 没有成功爬取到任何内容")
                
        except Exception as e:
            print(f"❌ 虚拟滚动爬取错误: {e}")
    
    async def _button_click_crawl(self, url: str):
        """点击按钮翻页策略"""
        print("\n🖱️ 点击按钮翻页配置")
        print("-" * 30)
        
        # 按钮选择器配置
        print("请配置翻页按钮:")
        next_button_selector = input("下一页按钮CSS选择器 (如: .next-page, #next-btn): ").strip()
        if not next_button_selector:
            print("❌ 必须提供下一页按钮选择器")
            return
        
        max_pages = input("最大翻页数 (默认10): ").strip()
        max_pages = int(max_pages) if max_pages.isdigit() else 10
        
        click_delay = input("点击间隔时间/秒 (默认3): ").strip()
        click_delay = float(click_delay) if click_delay.replace('.', '').isdigit() else 3.0
        
        wait_for_load = input("页面加载等待时间/秒 (默认5): ").strip()
        wait_for_load = int(wait_for_load) if wait_for_load.isdigit() else 5
        
        # 可选的停止条件
        stop_selector = input("停止条件选择器 (可选，如按钮禁用类): ").strip()
        
        try:
            print(f"\n🚀 开始按钮点击翻页...")
            print(f"🔘 按钮选择器: {next_button_selector}")
            print(f"📊 最大翻页: {max_pages}, 间隔: {click_delay}秒")
            
            all_content = []
            page_count = 0
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                # 爬取第一页
                print("📄 爬取第1页 (初始页面)...")
                result = await crawler.arun(
                    url=url,
                    wait_for=f"sleep:{wait_for_load}"
                )
                
                if result.success:
                    page_data = self._extract_page_data(result, 1)
                    all_content.append(page_data)
                    page_count = 1
                    print(f"✅ 第1页爬取成功，内容长度: {len(result.cleaned_html)}")
                else:
                    print(f"❌ 第1页爬取失败: {result.error_message}")
                    return
                
                # 翻页爬取
                for page in range(2, max_pages + 1):
                    print(f"\n🔄 点击翻页到第{page}页...")
                    
                    # 构建点击翻页的JavaScript
                    click_js = f"""
                    // 查找下一页按钮
                    const nextButton = document.querySelector('{next_button_selector}');
                    
                    if (!nextButton) {{
                        return {{ error: 'Next button not found', selector: '{next_button_selector}' }};
                    }}
                    
                    // 检查按钮是否可点击
                    const isDisabled = nextButton.disabled || 
                                     nextButton.classList.contains('disabled') ||
                                     nextButton.getAttribute('aria-disabled') === 'true';
                    
                    if (isDisabled) {{
                        return {{ error: 'Next button is disabled', disabled: true }};
                    }}
                    
                    // 滚动到按钮位置
                    nextButton.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    
                    // 点击按钮
                    nextButton.click();
                    
                    // 等待页面更新
                    await new Promise(resolve => setTimeout(resolve, {click_delay * 1000}));
                    
                    return {{ 
                        clicked: true, 
                        page: {page},
                        buttonText: nextButton.textContent.trim(),
                        currentUrl: window.location.href
                    }};
                    """
                    
                    # 执行点击和爬取
                    result = await crawler.arun(
                        url=url if page == 2 else result.url,  # 第二页用原URL，之后用当前URL
                        js_code=click_js,
                        wait_for=f"sleep:{wait_for_load}",
                        bypass_cache=True
                    )
                    
                    if result.success:
                        # 检查JavaScript执行结果
                        if hasattr(result, 'js_result'):
                            js_result = result.js_result
                            if isinstance(js_result, dict) and js_result.get('error'):
                                print(f"🛑 {js_result['error']}")
                                break
                        
                        page_data = self._extract_page_data(result, page)
                        
                        # 检查是否有新内容（避免重复）
                        if any(p['content_hash'] == page_data['content_hash'] for p in all_content):
                            print("🛑 检测到重复内容，可能已到最后一页")
                            break
                        
                        all_content.append(page_data)
                        page_count = page
                        
                        print(f"✅ 第{page}页爬取成功")
                        print(f"📄 内容长度: {len(result.cleaned_html)}")
                        print(f"🔗 链接数: {page_data['links_count']}")
                        
                        # 检查停止条件
                        if stop_selector:
                            stop_element_js = f"document.querySelector('{stop_selector}') !== null"
                            stop_result = await crawler.arun(
                                url=result.url,
                                js_code=f"return {stop_element_js}",
                                wait_for="sleep:1"
                            )
                            if stop_result.success and hasattr(stop_result, 'js_result') and stop_result.js_result:
                                print("🛑 检测到停止条件，结束翻页")
                                break
                        
                        # 暂停以避免过快请求
                        await asyncio.sleep(click_delay)
                        
                    else:
                        print(f"❌ 第{page}页爬取失败: {result.error_message}")
                        break
            
            # 保存结果
            if all_content:
                await self._save_pagination_results(url, all_content, "button_click", {
                    'strategy': 'button_click',
                    'next_button_selector': next_button_selector,
                    'max_pages': max_pages,
                    'click_delay': click_delay,
                    'actual_pages': page_count
                })
                
                print(f"\n🎉 按钮点击翻页完成!")
                print(f"📊 成功爬取 {page_count} 页")
                print(f"📄 总内容长度: {sum(len(p['cleaned_html']) for p in all_content)}")
            else:
                print("❌ 没有成功爬取到任何内容")
                
        except Exception as e:
            print(f"❌ 按钮点击翻页错误: {e}")
    
    async def _javascript_injection_crawl(self, url: str):
        """JavaScript注入翻页策略"""
        print("\n⚡ JavaScript注入翻页配置")
        print("-" * 30)
        print("可以自定义JavaScript代码来实现复杂的翻页逻辑")
        
        max_pages = input("最大翻页数 (默认5): ").strip()
        max_pages = int(max_pages) if max_pages.isdigit() else 5
        
        page_delay = input("翻页间隔时间/秒 (默认3): ").strip()
        page_delay = float(page_delay) if page_delay.replace('.', '').isdigit() else 3.0
        
        print("\n选择预设JavaScript模板:")
        print("1. 自动检测翻页按钮")
        print("2. 滚动触发加载更多")
        print("3. AJAX翻页请求")
        print("4. 自定义JavaScript代码")
        
        template_choice = input("选择模板 (1-4): ").strip()
        
        if template_choice == "1":
            js_template = """
            // 自动检测翻页按钮
            const selectors = [
                'a[rel="next"]', '.next', '.page-next', '#next',
                'button:contains("下一页")', 'button:contains("Next")',
                'a:contains("下一页")', 'a:contains("Next")',
                '.pagination .next', '.pager .next'
            ];
            
            let nextButton = null;
            for (const selector of selectors) {
                try {
                    nextButton = document.querySelector(selector);
                    if (nextButton && nextButton.offsetParent !== null) break;
                } catch(e) {}
            }
            
            if (!nextButton) {
                return { error: 'No next button found' };
            }
            
            nextButton.scrollIntoView({ behavior: 'smooth' });
            await new Promise(resolve => setTimeout(resolve, 1000));
            nextButton.click();
            
            return { clicked: true, buttonFound: nextButton.tagName + '.' + nextButton.className };
            """
            
        elif template_choice == "2":
            js_template = """
            // 滚动触发加载更多
            const loadMoreSelectors = [
                '.load-more', '#load-more', 'button:contains("加载更多")',
                'button:contains("Load More")', '.show-more'
            ];
            
            // 先尝试滚动到底部
            window.scrollTo(0, document.body.scrollHeight);
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            // 查找加载更多按钮
            let loadButton = null;
            for (const selector of loadMoreSelectors) {
                try {
                    loadButton = document.querySelector(selector);
                    if (loadButton && loadButton.offsetParent !== null) break;
                } catch(e) {}
            }
            
            if (loadButton) {
                loadButton.click();
                await new Promise(resolve => setTimeout(resolve, 3000));
                return { scrolled: true, clicked: true };
            }
            
            return { scrolled: true, clicked: false };
            """
            
        elif template_choice == "3":
            js_template = """
            // AJAX翻页请求（需要根据具体网站调整）
            const currentPage = parseInt(document.querySelector('.current-page')?.textContent || '1');
            const nextPage = currentPage + 1;
            
            // 这里需要根据实际网站的AJAX请求进行调整
            try {
                const response = await fetch(`/api/content?page=${nextPage}`, {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' }
                });
                
                if (response.ok) {
                    const data = await response.json();
                    // 将新内容插入到页面中
                    const container = document.querySelector('.content-container');
                    if (container && data.html) {
                        container.innerHTML += data.html;
                    }
                    return { ajax: true, page: nextPage, success: true };
                }
            } catch(e) {
                return { ajax: true, error: e.message };
            }
            
            return { ajax: true, error: 'AJAX request failed' };
            """
            
        elif template_choice == "4":
            print("\n请输入自定义JavaScript代码 (输入'END'结束):")
            js_lines = []
            while True:
                line = input("JS> ")
                if line.strip() == "END":
                    break
                js_lines.append(line)
            js_template = "\n".join(js_lines)
        else:
            print("❌ 无效选择")
            return
        
        try:
            print(f"\n🚀 开始JavaScript注入翻页...")
            print(f"📊 最大翻页: {max_pages}, 间隔: {page_delay}秒")
            
            all_content = []
            page_count = 0
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                current_url = url
                
                for page in range(1, max_pages + 1):
                    print(f"\n📄 处理第{page}页...")
                    
                    if page == 1:
                        # 第一页，正常爬取
                        result = await crawler.arun(
                            url=current_url,
                            wait_for=f"sleep:{page_delay}"
                        )
                    else:
                        # 后续页面，执行JavaScript翻页
                        result = await crawler.arun(
                            url=current_url,
                            js_code=js_template,
                            wait_for=f"sleep:{page_delay}",
                            bypass_cache=True
                        )
                    
                    if result.success:
                        page_data = self._extract_page_data(result, page)
                        
                        # 检查是否有新内容
                        if page > 1 and any(p['content_hash'] == page_data['content_hash'] for p in all_content):
                            print("🛑 检测到重复内容，停止翻页")
                            break
                        
                        all_content.append(page_data)
                        page_count = page
                        current_url = result.url  # 更新当前URL
                        
                        print(f"✅ 第{page}页处理成功")
                        print(f"📄 内容长度: {len(result.cleaned_html)}")
                        
                        # 检查JavaScript执行结果
                        if page > 1 and hasattr(result, 'js_result'):
                            js_result = result.js_result
                            if isinstance(js_result, dict):
                                if js_result.get('error'):
                                    print(f"🛑 JavaScript执行错误: {js_result['error']}")
                                    break
                                elif js_result.get('clicked'):
                                    print("✅ 成功执行翻页操作")
                        
                        await asyncio.sleep(page_delay)
                        
                    else:
                        print(f"❌ 第{page}页处理失败: {result.error_message}")
                        break
            
            # 保存结果
            if all_content:
                await self._save_pagination_results(url, all_content, "javascript_injection", {
                    'strategy': 'javascript_injection',
                    'template_choice': template_choice,
                    'max_pages': max_pages,
                    'page_delay': page_delay,
                    'actual_pages': page_count,
                    'custom_js': js_template[:200] + "..." if len(js_template) > 200 else js_template
                })
                
                print(f"\n🎉 JavaScript注入翻页完成!")
                print(f"📊 成功处理 {page_count} 页")
                print(f"📄 总内容长度: {sum(len(p['cleaned_html']) for p in all_content)}")
            else:
                print("❌ 没有成功处理任何内容")
                
        except Exception as e:
            print(f"❌ JavaScript注入翻页错误: {e}")
    
    async def _url_pattern_crawl(self, url: str):
        """分页URL模式翻页策略"""
        print("\n🔗 分页URL模式翻页配置")
        print("-" * 30)
        print("适用于URL中包含页码参数的网站")
        
        print("\n分析URL模式:")
        print(f"当前URL: {url}")
        
        # 检测URL中可能的页码参数
        import re
        from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
        
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)
        
        # 常见的页码参数名
        page_param_names = ['page', 'p', 'pagenum', 'pageno', 'offset', 'start', 'skip']
        detected_params = []
        
        for param_name in page_param_names:
            if param_name in params:
                detected_params.append(param_name)
        
        if detected_params:
            print(f"🔍 检测到可能的页码参数: {', '.join(detected_params)}")
            suggested_param = detected_params[0]
        else:
            # 检查URL路径中的数字
            path_numbers = re.findall(r'/(\d+)/', parsed_url.path)
            if path_numbers:
                print(f"🔍 检测到路径中的数字: {', '.join(path_numbers)}")
                suggested_param = "path_number"
            else:
                suggested_param = "page"
        
        print("\n选择URL模式:")
        print("1. 查询参数模式 (如: ?page=1, ?p=2)")
        print("2. 路径参数模式 (如: /page/1/, /2/)")
        print("3. 片段模式 (如: #page=1)")
        print("4. 自定义模式")
        
        pattern_choice = input("选择模式 (1-4): ").strip()
        
        if pattern_choice == "1":
            param_name = input(f"页码参数名 (建议: {suggested_param}): ").strip() or suggested_param
            start_page = input("起始页码 (默认1): ").strip()
            start_page = int(start_page) if start_page.isdigit() else 1
            
            def generate_url(base_url, page_num):
                if '?' in base_url:
                    # 替换现有参数或添加新参数
                    parsed = urlparse(base_url)
                    params = parse_qs(parsed.query)
                    params[param_name] = [str(page_num)]
                    
                    new_query = urlencode(params, doseq=True)
                    return urlunparse(parsed._replace(query=new_query))
                else:
                    separator = '&' if '?' in base_url else '?'
                    return f"{base_url}{separator}{param_name}={page_num}"
            
        elif pattern_choice == "2":
            path_pattern = input("路径模式 (如: /page/{page}/ 或 /{page}/): ").strip()
            if not path_pattern:
                path_pattern = "/page/{page}/"
            
            start_page = input("起始页码 (默认1): ").strip()
            start_page = int(start_page) if start_page.isdigit() else 1
            
            def generate_url(base_url, page_num):
                parsed = urlparse(base_url)
                new_path = path_pattern.format(page=page_num)
                return urlunparse(parsed._replace(path=new_path))
            
        elif pattern_choice == "3":
            fragment_param = input("片段参数名 (默认page): ").strip() or "page"
            start_page = input("起始页码 (默认1): ").strip()
            start_page = int(start_page) if start_page.isdigit() else 1
            
            def generate_url(base_url, page_num):
                parsed = urlparse(base_url)
                new_fragment = f"{fragment_param}={page_num}"
                return urlunparse(parsed._replace(fragment=new_fragment))
            
        elif pattern_choice == "4":
            print("请输入URL模板，使用 {page} 作为页码占位符")
            print("例如: https://example.com/news?page={page}")
            url_template = input("URL模板: ").strip()
            
            start_page = input("起始页码 (默认1): ").strip()
            start_page = int(start_page) if start_page.isdigit() else 1
            
            def generate_url(base_url, page_num):
                return url_template.format(page=page_num)
        else:
            print("❌ 无效选择")
            return
        
        max_pages = input(f"最大页数 (默认10): ").strip()
        max_pages = int(max_pages) if max_pages.isdigit() else 10
        
        page_delay = input("页面间隔时间/秒 (默认2): ").strip()
        page_delay = float(page_delay) if page_delay.replace('.', '').isdigit() else 2.0
        
        # 停止条件
        check_404 = input("检测404页面自动停止? (Y/n): ").strip().lower() != 'n'
        min_content_length = input("最小内容长度 (默认100): ").strip()
        min_content_length = int(min_content_length) if min_content_length.isdigit() else 100
        
        try:
            print(f"\n🚀 开始URL模式翻页爬取...")
            print(f"📊 页码范围: {start_page} - {start_page + max_pages - 1}")
            print(f"⏱️ 间隔时间: {page_delay}秒")
            
            all_content = []
            page_count = 0
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                for page_offset in range(max_pages):
                    current_page = start_page + page_offset
                    current_url = generate_url(url, current_page)
                    
                    print(f"\n📄 爬取第{current_page}页...")
                    print(f"🔗 URL: {current_url}")
                    
                    result = await crawler.arun(
                        url=current_url,
                        wait_for=f"sleep:{page_delay}",
                        bypass_cache=True
                    )
                    
                    if result.success:
                        # 检查页面是否有效
                        if check_404 and result.status_code == 404:
                            print("🛑 检测到404页面，停止爬取")
                            break
                        
                        if len(result.cleaned_html) < min_content_length:
                            print(f"🛑 页面内容过短 ({len(result.cleaned_html)} < {min_content_length})，可能已到最后一页")
                            break
                        
                        page_data = self._extract_page_data(result, current_page)
                        
                        # 检查重复内容
                        if any(p['content_hash'] == page_data['content_hash'] for p in all_content):
                            print("🛑 检测到重复内容，停止爬取")
                            break
                        
                        all_content.append(page_data)
                        page_count += 1
                        
                        print(f"✅ 第{current_page}页爬取成功")
                        print(f"📄 内容长度: {len(result.cleaned_html)}")
                        print(f"📊 状态码: {result.status_code}")
                        
                        await asyncio.sleep(page_delay)
                        
                    else:
                        print(f"❌ 第{current_page}页爬取失败: {result.error_message}")
                        if check_404 and "404" in str(result.error_message):
                            print("🛑 检测到404错误，停止爬取")
                            break
            
            # 保存结果
            if all_content:
                await self._save_pagination_results(url, all_content, "url_pattern", {
                    'strategy': 'url_pattern',
                    'pattern_choice': pattern_choice,
                    'start_page': start_page,
                    'max_pages': max_pages,
                    'page_delay': page_delay,
                    'actual_pages': page_count,
                    'url_pattern': generate_url(url, 999)  # 示例URL
                })
                
                print(f"\n🎉 URL模式翻页完成!")
                print(f"📊 成功爬取 {page_count} 页")
                print(f"📄 总内容长度: {sum(len(p['cleaned_html']) for p in all_content)}")
            else:
                print("❌ 没有成功爬取到任何内容")
                
        except Exception as e:
            print(f"❌ URL模式翻页错误: {e}")
    
    async def _smart_hybrid_crawl(self, url: str):
        """智能混合模式翻页策略"""
        print("\n🧠 智能混合模式翻页")
        print("-" * 30)
        print("自动检测网站类型并选择最佳翻页策略")
        
        max_pages = input("最大页数 (默认10): ").strip()
        max_pages = int(max_pages) if max_pages.isdigit() else 10
        
        try:
            print(f"\n🔍 正在分析网站结构...")
            
            async with AsyncWebCrawler(verbose=True) as crawler:
                # 第一步：分析首页
                result = await crawler.arun(url=url, wait_for="sleep:3")
                
                if not result.success:
                    print(f"❌ 无法加载首页: {result.error_message}")
                    return
                
                print("✅ 首页加载成功，分析翻页特征...")
                
                # 分析页面特征的JavaScript
                analysis_js = """
                const features = {
                    hasNextButton: false,
                    hasPageNumbers: false,
                    hasLoadMore: false,
                    hasInfiniteScroll: false,
                    urlHasPageParam: false,
                    pageElements: []
                };
                
                // 检测翻页按钮
                const nextSelectors = [
                    'a[rel="next"]', '.next', '.page-next', '#next',
                    'button:contains("下一页")', 'button:contains("Next")',
                    'a:contains("下一页")', 'a:contains("Next")',
                    '.pagination .next', '.pager .next'
                ];
                
                for (const selector of nextSelectors) {
                    try {
                        const element = document.querySelector(selector);
                        if (element && element.offsetParent !== null) {
                            features.hasNextButton = true;
                            features.pageElements.push({
                                type: 'next_button',
                                selector: selector,
                                text: element.textContent.trim()
                            });
                            break;
                        }
                    } catch(e) {}
                }
                
                // 检测页码
                const pageSelectors = [
                    '.pagination a', '.pager a', '.page-numbers a',
                    '[class*="page"] a', '[id*="page"] a'
                ];
                
                for (const selector of pageSelectors) {
                    try {
                        const elements = document.querySelectorAll(selector);
                        if (elements.length > 1) {
                            features.hasPageNumbers = true;
                            features.pageElements.push({
                                type: 'page_numbers',
                                selector: selector,
                                count: elements.length
                            });
                            break;
                        }
                    } catch(e) {}
                }
                
                // 检测加载更多按钮
                const loadMoreSelectors = [
                    '.load-more', '#load-more', '.show-more',
                    'button:contains("加载更多")', 'button:contains("Load More")',
                    'button:contains("查看更多")', 'button:contains("Show More")'
                ];
                
                for (const selector of loadMoreSelectors) {
                    try {
                        const element = document.querySelector(selector);
                        if (element && element.offsetParent !== null) {
                            features.hasLoadMore = true;
                            features.pageElements.push({
                                type: 'load_more',
                                selector: selector,
                                text: element.textContent.trim()
                            });
                            break;
                        }
                    } catch(e) {}
                }
                
                // 检测无限滚动特征
                const scrollTriggers = [
                    '[data-infinite]', '[class*="infinite"]', '[id*="infinite"]',
                    '[class*="scroll"]', '[data-scroll]'
                ];
                
                for (const selector of scrollTriggers) {
                    try {
                        if (document.querySelector(selector)) {
                            features.hasInfiniteScroll = true;
                            features.pageElements.push({
                                type: 'infinite_scroll',
                                selector: selector
                            });
                            break;
                        }
                    } catch(e) {}
                }
                
                // 检测URL参数
                const urlParams = new URLSearchParams(window.location.search);
                const pageParams = ['page', 'p', 'pagenum', 'pageno', 'offset', 'start'];
                for (const param of pageParams) {
                    if (urlParams.has(param)) {
                        features.urlHasPageParam = true;
                        features.pageElements.push({
                            type: 'url_param',
                            param: param,
                            value: urlParams.get(param)
                        });
                        break;
                    }
                }
                
                return features;
                """
                
                # 执行分析
                analysis_result = await crawler.arun(
                    url=url,
                    js_code=analysis_js,
                    wait_for="sleep:2"
                )
                
                if analysis_result.success and hasattr(analysis_result, 'js_result'):
                    features = analysis_result.js_result
                    
                    print("\n📊 网站特征分析结果:")
                    print(f"🔘 翻页按钮: {'✅' if features.get('hasNextButton') else '❌'}")
                    print(f"🔢 页码导航: {'✅' if features.get('hasPageNumbers') else '❌'}")
                    print(f"📄 加载更多: {'✅' if features.get('hasLoadMore') else '❌'}")
                    print(f"♾️ 无限滚动: {'✅' if features.get('hasInfiniteScroll') else '❌'}")
                    print(f"🔗 URL页码: {'✅' if features.get('urlHasPageParam') else '❌'}")
                    
                    # 智能选择策略
                    selected_strategy = None
                    strategy_reason = ""
                    
                    if features.get('hasInfiniteScroll') or features.get('hasLoadMore'):
                        selected_strategy = "virtual_scroll"
                        strategy_reason = "检测到无限滚动或加载更多按钮"
                    elif features.get('hasNextButton'):
                        selected_strategy = "button_click"
                        strategy_reason = "检测到明确的翻页按钮"
                    elif features.get('urlHasPageParam'):
                        selected_strategy = "url_pattern"
                        strategy_reason = "检测到URL中的页码参数"
                    elif features.get('hasPageNumbers'):
                        selected_strategy = "button_click"
                        strategy_reason = "检测到页码导航"
                    else:
                        selected_strategy = "virtual_scroll"
                        strategy_reason = "未检测到明确翻页特征，尝试虚拟滚动"
                    
                    print(f"\n🎯 推荐策略: {selected_strategy}")
                    print(f"💡 原因: {strategy_reason}")
                    
                    # 询问用户是否使用推荐策略
                    use_recommended = input(f"\n是否使用推荐策略 '{selected_strategy}'? (Y/n): ").strip().lower() != 'n'
                    
                    if use_recommended:
                        print(f"\n🚀 使用推荐策略: {selected_strategy}")
                        
                        if selected_strategy == "virtual_scroll":
                            # 使用检测到的元素配置虚拟滚动
                            await self._execute_smart_virtual_scroll(url, max_pages, features)
                        elif selected_strategy == "button_click":
                            # 使用检测到的按钮配置点击翻页
                            await self._execute_smart_button_click(url, max_pages, features)
                        elif selected_strategy == "url_pattern":
                            # 使用检测到的URL参数配置翻页
                            await self._execute_smart_url_pattern(url, max_pages, features)
                    else:
                        print("请手动选择其他翻页策略")
                        return
                else:
                    print("❌ 无法分析网站特征，使用默认虚拟滚动策略")
                    await self._virtual_scroll_crawl(url)
                    
        except Exception as e:
            print(f"❌ 智能混合模式错误: {e}")
    
    async def _execute_smart_virtual_scroll(self, url: str, max_pages: int, features: dict):
        """执行智能虚拟滚动"""
        print("📱 执行智能虚拟滚动策略...")
        
        # 从特征中提取配置
        load_more_elements = [elem for elem in features.get('pageElements', []) if elem['type'] == 'load_more']
        
        all_content = []
        page_count = 0
        
        async with AsyncWebCrawler(verbose=True) as crawler:
            for page in range(max_pages):
                print(f"\n🔄 第 {page + 1}/{max_pages} 次处理...")
                
                if load_more_elements:
                    # 有加载更多按钮，使用点击策略
                    selector = load_more_elements[0]['selector']
                    js_code = f"""
                    // 滚动到底部
                    window.scrollTo(0, document.body.scrollHeight);
                    await new Promise(resolve => setTimeout(resolve, 2000));
                    
                    // 点击加载更多
                    const loadBtn = document.querySelector('{selector}');
                    if (loadBtn && loadBtn.offsetParent !== null) {{
                        loadBtn.click();
                        await new Promise(resolve => setTimeout(resolve, 3000));
                        return {{ clicked: true, hasMore: true }};
                    }}
                    return {{ clicked: false, hasMore: false }};
                    """
                else:
                    # 使用纯滚动策略
                    js_code = """
                    const originalHeight = document.body.scrollHeight;
                    window.scrollTo(0, document.body.scrollHeight);
                    await new Promise(resolve => setTimeout(resolve, 3000));
                    const newHeight = document.body.scrollHeight;
                    return { scrolled: true, heightChanged: newHeight > originalHeight };
                    """
                
                result = await crawler.arun(
                    url=url,
                    js_code=js_code,
                    wait_for="sleep:3",
                    bypass_cache=True
                )
                
                if result.success:
                    page_data = self._extract_page_data(result, page + 1)
                    
                    # 检查重复内容
                    if any(p['content_hash'] == page_data['content_hash'] for p in all_content):
                        print("🛑 内容未变化，停止滚动")
                        break
                    
                    all_content.append(page_data)
                    page_count += 1
                    
                    print(f"✅ 第{page + 1}次处理成功，内容长度: {len(result.cleaned_html)}")
                    
                    # 检查是否还有更多内容
                    if hasattr(result, 'js_result'):
                        js_result = result.js_result
                        if isinstance(js_result, dict):
                            if load_more_elements and not js_result.get('hasMore'):
                                print("🛑 没有更多内容可加载")
                                break
                            elif not load_more_elements and not js_result.get('heightChanged'):
                                print("🛑 页面高度未变化，已到底部")
                                break
                else:
                    print(f"❌ 第{page + 1}次处理失败: {result.error_message}")
                    break
        
        # 保存结果
        if all_content:
            await self._save_pagination_results(url, all_content, "smart_virtual_scroll", {
                'strategy': 'smart_virtual_scroll',
                'detected_features': features,
                'max_pages': max_pages,
                'actual_pages': page_count
            })
            
            print(f"\n🎉 智能虚拟滚动完成!")
            print(f"📊 成功处理 {page_count} 次")
            print(f"📄 总内容长度: {sum(len(p['cleaned_html']) for p in all_content)}")
    
    async def _execute_smart_button_click(self, url: str, max_pages: int, features: dict):
        """执行智能按钮点击"""
        print("🖱️ 执行智能按钮点击策略...")
        
        # 从特征中提取按钮选择器
        next_button_elements = [elem for elem in features.get('pageElements', []) if elem['type'] == 'next_button']
        
        if not next_button_elements:
            print("❌ 未找到翻页按钮")
            return
        
        selector = next_button_elements[0]['selector']
        await self._button_click_crawl(url)  # 使用现有的按钮点击逻辑
    
    async def _execute_smart_url_pattern(self, url: str, max_pages: int, features: dict):
        """执行智能URL模式"""
        print("🔗 执行智能URL模式策略...")
        
        # 从特征中提取URL参数
        url_param_elements = [elem for elem in features.get('pageElements', []) if elem['type'] == 'url_param']
        
        if not url_param_elements:
            print("❌ 未找到URL页码参数")
            return
        
        param_name = url_param_elements[0]['param']
        print(f"🔍 使用检测到的参数: {param_name}")
        
        await self._url_pattern_crawl(url)  # 使用现有的URL模式逻辑
    
    def _extract_page_data(self, result, page_num: int) -> dict:
        """提取页面数据的通用方法"""
        content_hash = hash(result.cleaned_html)
        
        return {
            'page': page_num,
            'url': result.url,
            'title': result.metadata.get('title', 'N/A'),
            'content_length': len(result.cleaned_html),
            'markdown_length': len(result.markdown),
            'links_count': len(result.links.get('internal', [])) + len(result.links.get('external', [])),
            'images_count': len(result.media.get('images', [])),
            'content_hash': content_hash,
            'html': result.html,
            'cleaned_html': result.cleaned_html,
            'markdown': result.markdown,
            'links': result.links,
            'media': result.media,
            'metadata': result.metadata,
            'status_code': result.status_code
        }
    
    async def _save_pagination_results(self, original_url: str, all_content: list, strategy: str, config: dict):
        """保存翻页爬取结果"""
        try:
            # 合并所有页面的内容
            merged_html = "\n".join([page['html'] for page in all_content])
            merged_cleaned = "\n".join([page['cleaned_html'] for page in all_content])
            merged_markdown = "\n".join([page['markdown'] for page in all_content])
            
            # 合并链接和媒体
            all_links = {'internal': [], 'external': []}
            all_media = {'images': [], 'videos': []}
            
            for page in all_content:
                all_links['internal'].extend(page['links'].get('internal', []))
                all_links['external'].extend(page['links'].get('external', []))
                all_media['images'].extend(page['media'].get('images', []))
                all_media['videos'].extend(page['media'].get('videos', []))
            
            # 去重
            all_links['internal'] = list(set(all_links['internal']))
            all_links['external'] = list(set(all_links['external']))
            all_media['images'] = list(set(all_media['images']))
            all_media['videos'] = list(set(all_media['videos']))
            
            # 创建合并的结果对象（模拟CrawlResult）
            class MockResult:
                def __init__(self):
                    self.success = True
                    self.url = original_url
                    self.html = merged_html
                    self.cleaned_html = merged_cleaned
                    self.markdown = merged_markdown
                    self.links = all_links
                    self.media = all_media
                    self.metadata = {
                        'title': all_content[0]['title'] if all_content else 'N/A',
                        'strategy': strategy,
                        'total_pages': len(all_content),
                        'config': config,
                        'pages_info': [
                            {
                                'page': p['page'],
                                'url': p['url'],
                                'title': p['title'],
                                'content_length': p['content_length']
                            }
                            for p in all_content
                        ]
                    }
                    self.status_code = 200
            
            merged_result = MockResult()
            
            # 保存合并的结果
            extra_data = {
                'strategy': strategy,
                'config': config,
                'total_pages': len(all_content),
                'individual_pages': all_content
            }
            
            save_info = self.save_crawl_result(
                merged_result, 
                original_url, 
                f'pagination_{strategy}', 
                extra_data
            )
            
            # 保存到历史
            history_entry = {
                'timestamp': datetime.now().isoformat(),
                'url': original_url,
                'type': f'pagination_{strategy}',
                'success': True,
                'strategy': strategy,
                'total_pages': len(all_content),
                'config': config
            }
            if save_info:
                history_entry['saved_files'] = save_info['saved_files']
                history_entry['base_filename'] = save_info['base_filename']
            
            self.results_history.append(history_entry)
            
            print(f"\n💾 翻页结果已保存")
            if save_info:
                print(f"📁 保存位置: {save_info['base_filename']}")
                print(f"📋 保存文件: {', '.join(save_info['saved_files'])}")
            
        except Exception as e:
            print(f"❌ 保存翻页结果时出错: {e}")
    
    def export_and_save(self):
        """导出和保存功能"""
        print("\n💾 导出和保存")
        print("=" * 40)
        
        if not self.results_history:
            print("❌ 没有可导出的历史记录")
            return
        
        print("选择导出格式:")
        print("1. JSON格式")
        print("2. CSV格式")
        print("3. 文本格式")
        
        export_choice = input("请选择 (1-3): ").strip()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        try:
            if export_choice == "1":
                # JSON导出
                filename = f"crawl4ai_history_{timestamp}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.results_history, f, ensure_ascii=False, indent=2)
                print(f"✅ 已导出到: {filename}")
                
            elif export_choice == "2":
                # CSV导出
                filename = f"crawl4ai_history_{timestamp}.csv"
                import csv
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    if self.results_history:
                        writer = csv.DictWriter(f, fieldnames=self.results_history[0].keys())
                        writer.writeheader()
                        writer.writerows(self.results_history)
                print(f"✅ 已导出到: {filename}")
                
            elif export_choice == "3":
                # 文本导出
                filename = f"crawl4ai_history_{timestamp}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("Crawl4AI 历史记录\n")
                    f.write("=" * 50 + "\n\n")
                    for i, record in enumerate(self.results_history, 1):
                        f.write(f"{i}. {record.get('timestamp', 'N/A')}\n")
                        f.write(f"   类型: {record.get('type', 'N/A')}\n")
                        f.write(f"   URL: {record.get('url', 'N/A')}\n")
                        f.write(f"   状态: {'成功' if record.get('success', False) else '失败'}\n")
                        f.write("-" * 30 + "\n")
                print(f"✅ 已导出到: {filename}")
                
        except Exception as e:
            print(f"❌ 导出失败: {e}")
    
    def session_management(self):
        """会话管理"""
        print("\n⚙️ 会话管理")
        print("=" * 40)
        
        print("选择操作:")
        print("1. 查看当前会话信息")
        print("2. 保存会话")
        print("3. 清除历史记录")
        print("4. 设置会话参数")
        
        session_choice = input("请选择 (1-4): ").strip()
        
        if session_choice == "1":
            # 查看会话信息
            print(f"\n📊 会话统计:")
            print(f"历史记录数: {len(self.results_history)}")
            print(f"配置文件: {self.config_file}")
            
            if self.results_history:
                success_count = sum(1 for r in self.results_history if r.get('success', False))
                print(f"成功率: {success_count}/{len(self.results_history)} ({success_count/len(self.results_history)*100:.1f}%)")
                
                # 按类型统计
                type_counts = {}
                for record in self.results_history:
                    record_type = record.get('type', 'unknown')
                    type_counts[record_type] = type_counts.get(record_type, 0) + 1
                
                print("\n📈 操作类型统计:")
                for op_type, count in type_counts.items():
                    print(f"  {op_type}: {count}")
        
        elif session_choice == "2":
            # 保存会话
            self.save_config()
            
        elif session_choice == "3":
            # 清除历史
            confirm = input("确认清除所有历史记录? (y/N): ").strip().lower()
            if confirm == 'y':
                self.results_history.clear()
                print("✅ 历史记录已清除")
            
        elif session_choice == "4":
            # 设置会话参数
            print("\n设置会话参数:")
            max_history = input(f"最大历史记录数 (当前: {self.session_data.get('max_history', 100)}): ").strip()
            if max_history.isdigit():
                self.session_data['max_history'] = int(max_history)
            
            auto_save_config = input("自动保存配置? (y/N): ").strip().lower()
            self.session_data['auto_save'] = auto_save_config == 'y'
            
            auto_save_results = input(f"自动保存爬取结果? (当前: {'y' if self.auto_save_enabled else 'n'}): ").strip().lower()
            if auto_save_results in ['y', 'n']:
                self.auto_save_enabled = auto_save_results == 'y'
            
            print("✅ 会话参数已更新")
    
    def search_history(self):
        """搜索历史记录"""
        print("\n🔍 搜索历史记录")
        print("=" * 40)
        
        if not self.results_history:
            print("❌ 没有历史记录")
            return
        
        search_term = input("请输入搜索关键词 (URL/标题/类型): ").strip().lower()
        if not search_term:
            return
        
        matches = []
        for i, record in enumerate(self.results_history):
            # 搜索URL、标题、类型
            searchable_text = " ".join([
                record.get('url', ''),
                record.get('title', ''),
                record.get('type', '')
            ]).lower()
            
            if search_term in searchable_text:
                matches.append((i, record))
        
        if matches:
            print(f"\n🎯 找到 {len(matches)} 条匹配记录:")
            print("-" * 50)
            
            for i, (index, record) in enumerate(matches[:10], 1):  # 最多显示10条
                print(f"{i}. [{record.get('timestamp', 'N/A')}]")
                print(f"   类型: {record.get('type', 'N/A')}")
                print(f"   URL: {record.get('url', 'N/A')}")
                print(f"   状态: {'✅成功' if record.get('success', False) else '❌失败'}")
                if record.get('title'):
                    print(f"   标题: {record['title'][:50]}...")
                print("-" * 30)
        else:
            print("❌ 未找到匹配的记录")
    
    async def manage_browser_profiles(self):
        """浏览器配置文件管理"""
        print("\n👤 浏览器配置文件管理")
        print("=" * 40)
        
        while True:
            profiles = self.list_browser_profiles()
            
            print("\n选择操作:")
            print("1. 创建新配置文件")
            print("2. 列出所有配置文件")
            print("3. 使用配置文件爬取")
            print("4. 删除配置文件")
            print("5. 返回主菜单")
            
            choice = input("请选择 (1-5): ").strip()
            
            if choice == "1":
                # 创建新配置文件
                print("\n📝 创建新的浏览器配置文件")
                profile_name = input("配置文件名称: ").strip()
                if not profile_name:
                    print("❌ 配置文件名称不能为空")
                    continue
                
                # 检查是否已存在
                if any(p['name'] == profile_name for p in profiles):
                    print("❌ 配置文件已存在")
                    continue
                
                description = input("描述 (可选): ").strip()
                
                profile_path = self.create_browser_profile(profile_name, description)
                if profile_path:
                    print(f"✅ 配置文件创建成功！")
                    print(f"📁 保存路径: {profile_path}")
                    print("\n💡 提示: 现在您可以使用此配置文件进行爬取，登录状态将自动保存")
            
            elif choice == "2":
                # 列出配置文件
                print(f"\n📋 浏览器配置文件列表 (共 {len(profiles)} 个):")
                if not profiles:
                    print("❌ 暂无配置文件")
                else:
                    print("-" * 70)
                    for i, profile in enumerate(profiles, 1):
                        print(f"{i}. {profile['name']}")
                        if profile.get('description'):
                            print(f"   描述: {profile['description']}")
                        print(f"   创建时间: {profile.get('created', 'N/A')}")
                        print(f"   使用次数: {profile.get('usage_count', 0)}")
                        if profile.get('last_used'):
                            print(f"   最后使用: {profile['last_used']}")
                        if profile.get('websites'):
                            print(f"   已登录网站: {len(profile['websites'])} 个")
                            for site in profile['websites'][:3]:  # 显示前3个
                                domain = site.split('/')[2] if '/' in site else site
                                print(f"     • {domain}")
                            if len(profile['websites']) > 3:
                                print(f"     ... 还有 {len(profile['websites']) - 3} 个")
                        print("-" * 70)
            
            elif choice == "3":
                # 使用配置文件爬取
                if not profiles:
                    print("❌ 暂无配置文件，请先创建")
                    continue
                
                print("\n🚀 使用配置文件爬取")
                print("选择配置文件:")
                for i, profile in enumerate(profiles, 1):
                    print(f"{i}. {profile['name']} (使用 {profile.get('usage_count', 0)} 次)")
                
                try:
                    profile_idx = int(input("请选择配置文件 (输入数字): ").strip()) - 1
                    if 0 <= profile_idx < len(profiles):
                        selected_profile = profiles[profile_idx]
                        await self.crawl_with_profile(selected_profile['name'])
                    else:
                        print("❌ 无效选择")
                except ValueError:
                    print("❌ 请输入有效数字")
            
            elif choice == "4":
                # 删除配置文件
                if not profiles:
                    print("❌ 暂无配置文件")
                    continue
                
                print("\n🗑️ 删除配置文件")
                print("选择要删除的配置文件:")
                for i, profile in enumerate(profiles, 1):
                    print(f"{i}. {profile['name']}")
                
                try:
                    profile_idx = int(input("请选择配置文件 (输入数字): ").strip()) - 1
                    if 0 <= profile_idx < len(profiles):
                        selected_profile = profiles[profile_idx]
                        confirm = input(f"确认删除配置文件 '{selected_profile['name']}'? (y/N): ").strip().lower()
                        if confirm == 'y':
                            import shutil
                            profile_path = os.path.join(self.profiles_dir, selected_profile['name'])
                            shutil.rmtree(profile_path)
                            print(f"✅ 配置文件 '{selected_profile['name']}' 已删除")
                    else:
                        print("❌ 无效选择")
                except ValueError:
                    print("❌ 请输入有效数字")
                except Exception as e:
                    print(f"❌ 删除失败: {e}")
            
            elif choice == "5":
                break
            
            else:
                print("❌ 无效选择，请重新输入")
            
            input("\n按回车键继续...")
    
    async def crawl_with_profile(self, profile_name):
        """使用指定配置文件进行爬取"""
        print(f"\n🚀 使用配置文件 '{profile_name}' 进行爬取")
        print("=" * 50)
        
        url = input("请输入URL: ").strip()
        if not url:
            print("❌ URL不能为空")
            return
        
        # 全页滚动选项
        print("\n是否启用全页滚动 (适用于动态加载内容的网站):")
        print("1. 否 (普通爬取)")
        print("2. 是 (模拟滚动到底部，加载所有动态内容)")
        
        scroll_choice = input("请选择 (1-2): ").strip()
        scan_full_page = scroll_choice == "2"
        
        scroll_delay = 0.2  # 默认滚动延迟
        if scan_full_page:
            delay_input = input("滚动延迟时间 (秒，默认0.2): ").strip()
            if delay_input and delay_input.replace('.', '').isdigit():
                scroll_delay = float(delay_input)
        
        # 选择爬取模式
        print("\n选择爬取模式:")
        print("1. 基础爬取")
        print("2. JavaScript渲染爬取")
        print("3. 高级配置爬取")
        
        mode_choice = input("请选择 (1-3): ").strip()
        
        try:
            # 获取浏览器配置
            browser_config = self.get_browser_config(profile_name)
            
            # 根据模式设置不同参数
            crawler_kwargs = {'config': browser_config, 'verbose': True}
            arun_kwargs = {'url': url}
            
            # 添加全页滚动参数
            if scan_full_page:
                arun_kwargs['scan_full_page'] = True
                arun_kwargs['scroll_delay'] = scroll_delay
                print(f"🔄 启用全页滚动，延迟: {scroll_delay}秒")
                print("💡 注意: 滚动过程中浏览器窗口会自动向下滚动以加载动态内容")
            
            if mode_choice == "2":
                # JavaScript渲染模式
                wait_time = input("等待时间 (秒, 默认3): ").strip()
                wait_time = int(wait_time) if wait_time.isdigit() else 3
                arun_kwargs['wait_for'] = f'sleep:{wait_time}'
                # 注意：如果启用了scan_full_page，就不需要手动滚动了
                if not scan_full_page:
                    arun_kwargs['js_code'] = "window.scrollTo(0, document.body.scrollHeight);"
                
            elif mode_choice == "3":
                # 高级配置模式
                wait_time = input("等待时间 (秒, 默认3): ").strip()
                wait_time = int(wait_time) if wait_time.isdigit() else 3
                arun_kwargs['wait_for'] = f'sleep:{wait_time}'
                
                screenshot = input("截图? (y/N): ").strip().lower() == 'y'
                arun_kwargs['screenshot'] = screenshot
                
                bypass_cache = input("绕过缓存? (y/N): ").strip().lower() == 'y'
                arun_kwargs['bypass_cache'] = bypass_cache
            
            print(f"\n🌐 开始使用配置文件 '{profile_name}' 爬取...")
            print("💡 提示: 浏览器将以非无头模式启动，您可以手动登录网站")
            
            async with AsyncWebCrawler(**crawler_kwargs) as crawler:
                result = await crawler.arun(**arun_kwargs)
                
                if result.success:
                    print(f"\n✅ 爬取成功!")
                    print(f"📄 页面标题: {result.metadata.get('title', 'N/A')}")
                    print(f"🌐 URL: {url}")
                    print(f"📊 状态码: {result.status_code}")
                    print(f"📝 内容长度: {len(result.markdown)} 字符")
                    if scan_full_page:
                        print(f"🔄 全页滚动已完成，内容可能包含动态加载的部分")
                    
                    # 更新配置文件使用记录
                    self.update_profile_usage(profile_name, url)
                    
                    # 实时保存结果
                    extra_data = {'profile_used': profile_name}
                    save_info = self.save_crawl_result(result, url, 'profile_crawl', extra_data)
                    
                    # 保存到历史
                    history_entry = {
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'type': 'profile_crawl',
                        'profile_used': profile_name,
                        'success': True,
                        'title': result.metadata.get('title', 'N/A')
                    }
                    if save_info:
                        history_entry['saved_files'] = save_info['saved_files']
                        history_entry['base_filename'] = save_info['base_filename']
                    self.results_history.append(history_entry)
                    
                    # 显示部分内容
                    if len(result.markdown) > 500:
                        print(f"\n📋 内容预览 (前500字符):")
                        print("-" * 30)
                        print(result.markdown[:500] + "...")
                    else:
                        print(f"\n📋 完整内容:")
                        print("-" * 30)
                        print(result.markdown)
                    
                    print(f"\n✅ 配置文件 '{profile_name}' 的登录状态已自动保存")
                    
                else:
                    print(f"\n❌ 爬取失败: {result.error_message}")
                    
        except Exception as e:
            print(f"❌ 爬取过程中出现错误: {e}")
    
    def show_settings(self):
        """显示设置和配置"""
        print("\n⚙️ 设置和配置")
        print("=" * 40)
        
        print("当前配置:")
        print(f"📁 配置文件: {self.config_file}")
        print(f"📊 历史记录: {len(self.results_history)} 条")
        print(f"💾 自动保存配置: {'是' if self.session_data.get('auto_save', False) else '否'}")
        print(f"💾 自动保存结果: {'是' if self.auto_save_enabled else '否'}")
        print(f"📈 最大历史: {self.session_data.get('max_history', 100)} 条")
        print(f"📁 结果目录: {self.results_dir}")
        
        print("\n可用功能:")
        features = [
            "✅ 基础网页爬取",
            "✅ 高级配置选项",
            "✅ 结构化数据提取",
            "✅ LLM智能提取",
            "✅ 批量URL处理",
            "✅ JavaScript渲染",
            "✅ 内容过滤清理",
            "✅ 多格式导出",
            "✅ 会话管理",
            "✅ 历史记录搜索"
        ]
        
        for feature in features:
            print(f"  {feature}")
    
    def show_help(self):
        """显示帮助信息"""
        print("\n❓ 帮助和文档")
        print("=" * 40)
        
        print("🚀 Crawl4AI 交互式工具使用指南")
        print("\n📚 主要功能:")
        
        help_info = [
            ("1️⃣ 基础爬取", "简单的网页内容抓取，支持HTML、文本、Markdown格式"),
            ("2️⃣ 高级配置", "自定义User-Agent、等待时间、缓存、iframe处理等"),
            ("3️⃣ 结构化提取", "使用CSS选择器、JSON模式、余弦相似度提取特定内容"),
            ("4️⃣ LLM智能提取", "集成OpenAI等LLM模型进行智能内容提取"),
            ("5️⃣ 批量处理", "同时处理多个URL，支持并发控制"),
            ("6️⃣ JavaScript渲染", "处理动态内容，执行JS代码，等待元素加载"),
            ("7️⃣ 内容过滤", "使用BM25算法、标签过滤等清理和过滤内容"),
            ("8️⃣ 导出保存", "支持JSON、CSV、TXT多种格式导出"),
        ]
        
        for title, desc in help_info:
            print(f"\n{title}")
            print(f"  {desc}")
        
        print(f"\n🔗 官方资源:")
        print("  📖 官方文档: https://docs.crawl4ai.com/")
        print("  🐙 GitHub: https://github.com/unclecode/crawl4ai")
        print("  📦 PyPI: https://pypi.org/project/crawl4ai/")
        
        print(f"\n💡 使用技巧:")
        tips = [
            "使用高级配置可以处理复杂的动态网页",
            "LLM提取功能需要有效的API Token",
            "批量处理时建议控制并发数避免被限制",
            "JavaScript渲染适用于SPA应用和动态加载内容",
            "定期保存会话以避免丢失历史记录"
        ]
        
        for i, tip in enumerate(tips, 1):
            print(f"  {i}. {tip}")
    
    async def run(self):
        """运行主程序"""
        self.display_banner()
        
        while True:
            try:
                self.display_main_menu()
                choice = input("请选择功能 (输入数字): ").strip()
                
                if choice == "1":
                    await self.basic_crawl()
                elif choice == "2":
                    await self.advanced_crawl()
                elif choice == "3":
                    await self.structured_extraction()
                elif choice == "4":
                    await self.llm_extraction()
                elif choice == "5":
                    await self.batch_crawl()
                elif choice == "6":
                    await self.javascript_rendering()
                elif choice == "7":
                    await self.content_filtering()
                elif choice == "8":
                    await self.pagination_crawl()
                elif choice == "9":
                    self.export_and_save()
                elif choice == "10":
                    self.session_management()
                elif choice == "11":
                    self.search_history()
                elif choice == "12":
                    await self.manage_browser_profiles()
                elif choice == "13":
                    self.manage_auto_save()
                elif choice == "14":
                    self.show_settings()
                elif choice == "15":
                    self.show_help()
                elif choice == "0":
                    print("\n👋 感谢使用 Crawl4AI 交互式工具!")
                    if self.session_data.get('auto_save', False):
                        self.save_config()
                        print("✅ 会话已自动保存")
                    break
                else:
                    print("❌ 无效选择，请输入有效数字 (0-15)")
                
                # 限制历史记录数量
                max_history = self.session_data.get('max_history', 100)
                if len(self.results_history) > max_history:
                    self.results_history = self.results_history[-max_history:]
                
                input("\n按回车键继续...")
                
            except KeyboardInterrupt:
                print("\n\n👋 程序被用户中断，再见!")
                break
            except Exception as e:
                print(f"\n❌ 程序错误: {e}")
                print("程序将继续运行...")
                input("按回车键继续...")

def main():
    """程序入口"""
    try:
        app = InteractiveCrawl4AI()
        asyncio.run(app.run())
    except KeyboardInterrupt:
        print("\n👋 再见!")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
