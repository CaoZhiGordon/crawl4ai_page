#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Crawl4AI 安装和功能测试脚本
测试各种基本功能以验证库是否正常工作
"""

import asyncio
import sys
from crawl4ai import AsyncWebCrawler

async def test_basic_crawl():
    """测试基本爬取功能"""
    print("🚀 开始测试基本爬取功能...")
    
    async with AsyncWebCrawler(verbose=True) as crawler:
        # 测试抓取一个简单的网页
        result = await crawler.arun(url="https://httpbin.org/html")
        
        print(f"✅ 成功抓取页面")
        print(f"📊 HTML 长度: {len(result.html)}")
        print(f"📋 页面标题: {result.metadata.get('title', 'N/A')}")
        print(f"⏱️  抓取时间: {result.metadata.get('processing_time', 'N/A')} 秒")
        
        return result

async def test_text_extraction():
    """测试文本提取功能"""
    print("\n🔤 开始测试文本提取功能...")
    
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://httpbin.org/html",
            word_count_threshold=10
        )
        
        print(f"✅ 成功提取文本")
        print(f"📝 提取的文本长度: {len(result.cleaned_html)}")
        print(f"🔍 文本内容预览: {result.cleaned_html[:200]}...")
        
        return result

async def test_with_custom_config():
    """测试自定义配置"""
    print("\n⚙️  开始测试自定义配置...")
    
    # 使用简单的配置测试
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://httpbin.org/user-agent",
            word_count_threshold=5
        )
        
        print(f"✅ 成功使用自定义配置")
        print(f"🤖 用户代理测试: {len(result.html) > 0}")
        print(f"📄 响应内容长度: {len(result.html)}")
        print(f"🔍 响应内容预览: {result.cleaned_html[:100] if result.cleaned_html else 'N/A'}...")
        
        return result

def test_import():
    """测试库导入"""
    print("📦 测试库导入...")
    
    try:
        import crawl4ai
        print(f"✅ crawl4ai 版本: {crawl4ai.__version__ if hasattr(crawl4ai, '__version__') else '未知'}")
        
        from crawl4ai import AsyncWebCrawler
        print("✅ AsyncWebCrawler 导入成功")
        
        from crawl4ai.extraction_strategy import LLMExtractionStrategy, CosineStrategy
        print("✅ 提取策略导入成功")
        
        from crawl4ai.chunking_strategy import RegexChunking, NlpSentenceChunking
        print("✅ 分块策略导入成功")
        
        return True
        
    except ImportError as e:
        print(f"❌ 导入失败: {e}")
        return False

async def main():
    """主测试函数"""
    print("🎯 Crawl4AI 安装测试开始")
    print("=" * 50)
    
    # 测试导入
    import_success = test_import()
    
    if not import_success:
        print("\n❌ 库导入失败，无法继续测试")
        sys.exit(1)
    
    try:
        # 基本功能测试
        await test_basic_crawl()
        
        # 文本提取测试  
        await test_text_extraction()
        
        # 自定义配置测试
        await test_with_custom_config()
        
        print("\n" + "=" * 50)
        print("🎉 所有测试通过！Crawl4AI 安装成功且工作正常")
        print("💡 你现在可以开始使用 Crawl4AI 进行网页爬取了")
        
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {e}")
        print(f"🔧 错误类型: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    # 运行测试
    asyncio.run(main())
