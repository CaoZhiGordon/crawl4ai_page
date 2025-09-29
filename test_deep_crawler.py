#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
深度爬取器测试脚本

这个脚本用于快速测试深度爬取器的基本功能，确保所有依赖都正确安装
并且爬取器能够正常工作。

运行: python test_deep_crawler.py
"""

import asyncio
import sys
import os
from datetime import datetime

def test_imports():
    """测试所有必需的包导入"""
    print("🔍 测试依赖包导入...")
    
    missing_packages = []
    
    # 测试 crawl4ai
    try:
        import crawl4ai
        print("✅ crawl4ai - OK")
    except ImportError:
        print("❌ crawl4ai - 缺失")
        missing_packages.append("crawl4ai")
    
    # 测试 aiohttp
    try:
        import aiohttp
        print("✅ aiohttp - OK")
    except ImportError:
        print("❌ aiohttp - 缺失") 
        missing_packages.append("aiohttp")
    
    # 测试 beautifulsoup4
    try:
        from bs4 import BeautifulSoup
        print("✅ beautifulsoup4 - OK")
    except ImportError:
        print("❌ beautifulsoup4 - 缺失")
        missing_packages.append("beautifulsoup4")
    
    # 测试我们的模块
    try:
        from deep_website_crawler import DeepWebsiteCrawler, CrawlConfig
        print("✅ deep_website_crawler - OK")
    except ImportError as e:
        print(f"❌ deep_website_crawler - 导入失败: {e}")
        return False
    
    if missing_packages:
        print(f"\n❌ 缺少依赖包: {', '.join(missing_packages)}")
        print(f"请运行: pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ 所有依赖包导入成功!")
    return True

async def test_basic_crawl():
    """测试基本爬取功能"""
    print("\n🚀 测试基本爬取功能...")
    
    try:
        from deep_website_crawler import DeepWebsiteCrawler, CrawlConfig
        
        # 创建一个非常简单的测试配置
        config = CrawlConfig(
            start_url="https://httpbin.org/html",  # 简单的测试页面
            max_depth=1,                           # 只爬取1层
            max_pages=2,                           # 最多2个页面
            concurrent_limit=1,                    # 单线程
            delay=1.0,                             # 1秒延时
            same_domain_only=True,
            output_dir="test_crawl_output",
            merge_markdown=True
        )
        
        print(f"📋 测试配置:")
        print(f"   URL: {config.start_url}")
        print(f"   最大深度: {config.max_depth}")
        print(f"   最大页面: {config.max_pages}")
        
        # 创建爬取器并运行
        crawler = DeepWebsiteCrawler(config)
        results = await crawler.crawl_website()
        
        # 检查结果
        if results:
            print(f"✅ 基本爬取测试成功!")
            print(f"   爬取页面数: {len(results)}")
            
            # 生成合并文档
            if config.merge_markdown:
                await crawler.generate_merged_markdown()
                print(f"✅ 合并文档生成成功!")
            
            return True
        else:
            print(f"❌ 基本爬取测试失败: 没有爬取到页面")
            return False
            
    except Exception as e:
        print(f"❌ 基本爬取测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_url_validation():
    """测试URL验证功能"""
    print("\n🔍 测试URL验证功能...")
    
    try:
        from deep_website_crawler import DeepWebsiteCrawler, CrawlConfig
        
        config = CrawlConfig(
            start_url="https://example.com",
            max_depth=2,
            max_pages=10
        )
        
        crawler = DeepWebsiteCrawler(config)
        
        # 测试各种URL
        test_cases = [
            ("https://example.com/page1", 1, True),    # 应该通过
            ("https://other.com/page1", 1, False),     # 不同域名，应该失败
            ("javascript:void(0)", 1, False),          # JavaScript链接，应该失败
            ("https://example.com/file.pdf", 1, False),# PDF文件，应该失败
            ("https://example.com/page1#anchor", 1, True), # 锚点会被规范化
        ]
        
        all_passed = True
        for url, depth, expected in test_cases:
            result = crawler.is_valid_url(url, depth)
            if result == expected:
                print(f"✅ {url[:50]}... -> {result} (符合预期)")
            else:
                print(f"❌ {url[:50]}... -> {result} (预期: {expected})")
                all_passed = False
        
        if all_passed:
            print("✅ URL验证测试全部通过!")
            return True
        else:
            print("❌ 部分URL验证测试失败")
            return False
            
    except Exception as e:
        print(f"❌ URL验证测试失败: {e}")
        return False

def test_configuration():
    """测试配置系统"""
    print("\n⚙️ 测试配置系统...")
    
    try:
        from deep_website_crawler import CrawlConfig
        
        # 测试默认配置
        config1 = CrawlConfig(start_url="https://example.com")
        print(f"✅ 默认配置创建成功")
        print(f"   默认深度: {config1.max_depth}")
        print(f"   默认页面数: {config1.max_pages}")
        
        # 测试自定义配置
        config2 = CrawlConfig(
            start_url="https://example.com",
            max_depth=5,
            max_pages=200,
            concurrent_limit=10,
            delay=0.5
        )
        print(f"✅ 自定义配置创建成功")
        print(f"   自定义深度: {config2.max_depth}")
        print(f"   自定义页面数: {config2.max_pages}")
        
        # 验证排除模式
        if config1.exclude_patterns:
            print(f"✅ 默认排除模式已设置 ({len(config1.exclude_patterns)} 个规则)")
        
        return True
        
    except Exception as e:
        print(f"❌ 配置测试失败: {e}")
        return False

def cleanup_test_files():
    """清理测试文件"""
    try:
        import shutil
        test_dir = "test_crawl_output"
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
            print(f"🧹 已清理测试文件: {test_dir}")
    except Exception as e:
        print(f"⚠️ 清理测试文件失败: {e}")

async def main():
    """主测试函数"""
    print("🧪" + "=" * 50 + "🧪")
    print("        深度网站爬取器 - 功能测试")
    print("🧪" + "=" * 50 + "🧪")
    
    print(f"📅 测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    test_results = []
    
    # 1. 测试导入
    print(f"\n{'='*20} 第1项测试 {'='*20}")
    result1 = test_imports()
    test_results.append(("依赖包导入", result1))
    
    if not result1:
        print(f"\n❌ 依赖包测试失败，无法继续其他测试")
        return
    
    # 2. 测试配置系统
    print(f"\n{'='*20} 第2项测试 {'='*20}")
    result2 = test_configuration()
    test_results.append(("配置系统", result2))
    
    # 3. 测试URL验证
    print(f"\n{'='*20} 第3项测试 {'='*20}")
    result3 = await test_url_validation()
    test_results.append(("URL验证", result3))
    
    # 4. 测试基本爬取（可选，因为需要网络连接）
    print(f"\n{'='*20} 第4项测试 {'='*20}")
    print("⚠️ 注意: 此测试需要网络连接，可能需要30-60秒...")
    
    try:
        user_input = input("是否进行网络爬取测试？(y/N): ").strip().lower()
        if user_input in ['y', 'yes', '是']:
            result4 = await test_basic_crawl()
            test_results.append(("基本爬取", result4))
        else:
            print("⏭️ 跳过网络爬取测试")
            test_results.append(("基本爬取", None))  # 标记为跳过
    except KeyboardInterrupt:
        print("\n⏹️ 测试被用户中断")
        test_results.append(("基本爬取", False))
    
    # 显示测试结果总结
    print(f"\n{'🎯'*20} 测试结果总结 {'🎯'*20}")
    
    passed = 0
    failed = 0
    skipped = 0
    
    for test_name, result in test_results:
        if result is True:
            print(f"✅ {test_name}: 通过")
            passed += 1
        elif result is False:
            print(f"❌ {test_name}: 失败")
            failed += 1
        else:
            print(f"⏭️ {test_name}: 跳过")
            skipped += 1
    
    print(f"\n📊 测试统计:")
    print(f"   ✅ 通过: {passed}")
    print(f"   ❌ 失败: {failed}")
    print(f"   ⏭️ 跳过: {skipped}")
    
    if failed == 0:
        print(f"\n🎉 所有测试通过! 深度爬取器已准备就绪!")
        print(f"💡 您可以运行: python run_deep_crawler.py")
    else:
        print(f"\n⚠️ 有 {failed} 项测试失败，请检查配置和依赖")
    
    # 清理测试文件
    cleanup_test_files()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n👋 测试被中断，再见!")
    except Exception as e:
        print(f"\n💥 测试过程中发生未预期的错误: {e}")
        import traceback
        traceback.print_exc()

