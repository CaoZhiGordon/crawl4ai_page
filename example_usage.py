#!/usr/bin/env python3
"""
Crawl4AI 使用示例
基于官方文档: https://docs.crawl4ai.com/
"""

import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy, CosineStrategy
from crawl4ai.chunking_strategy import RegexChunking

async def basic_crawling_example():
    """基本爬取示例 - 来自官方文档"""
    print("\n🚀 基本爬取示例")
    print("=" * 50)
    
    async with AsyncWebCrawler() as crawler:
        # 爬取官方示例页面
        result = await crawler.arun(url="https://crawl4ai.com")
        
        print(f"✅ 页面标题: {result.metadata.get('title', 'N/A')}")
        print(f"📄 HTML 长度: {len(result.html)}")
        print(f"📝 Markdown 长度: {len(result.markdown)}")
        print(f"🔗 链接数量: {len(result.links.get('internal', [])) + len(result.links.get('external', []))}")
        print(f"🖼️ 图片数量: {len(result.media.get('images', []))}")
        
        # 显示 Markdown 内容的前300字符
        print(f"\n📋 Markdown 内容预览:")
        print("-" * 30)
        print(result.markdown[:300] + "..." if len(result.markdown) > 300 else result.markdown)

async def structured_extraction_example():
    """结构化提取示例"""
    print("\n🎯 结构化提取示例")
    print("=" * 50)
    
    async with AsyncWebCrawler() as crawler:
        # 使用 CSS 选择器提取特定内容
        result = await crawler.arun(
            url="https://news.ycombinator.com",
            css_selector="tr.athing"  # 提取 Hacker News 的文章条目
        )
        
        print(f"✅ 成功提取结构化内容")
        print(f"📊 提取的内容长度: {len(result.cleaned_html)}")
        print(f"🔍 内容预览:")
        print("-" * 30)
        print(result.cleaned_html[:400] + "..." if len(result.cleaned_html) > 400 else result.cleaned_html)

async def markdown_generation_example():
    """Markdown 生成示例"""
    print("\n📝 Markdown 生成示例")
    print("=" * 50)
    
    async with AsyncWebCrawler() as crawler:
        # 生成清洁的 Markdown，适合 RAG 流水线
        result = await crawler.arun(
            url="https://python.org",
            word_count_threshold=10,  # 过滤掉少于10个词的内容块
            only_text=True  # 只返回文本内容
        )
        
        print(f"✅ 生成 Markdown 成功")
        print(f"📝 Markdown 长度: {len(result.markdown)}")
        print(f"🧹 清洁文本长度: {len(result.cleaned_html)}")
        
        # 保存 Markdown 到文件
        with open('/Users/lawgenesis-q6lr/Desktop/crawl4ai/python_org_content.md', 'w', encoding='utf-8') as f:
            f.write(result.markdown)
        print(f"💾 Markdown 已保存到: python_org_content.md")

async def advanced_crawling_example():
    """高级爬取示例 - 使用自定义配置"""
    print("\n⚙️ 高级爬取示例")
    print("=" * 50)
    
    async with AsyncWebCrawler(verbose=True) as crawler:
        # 使用高级参数进行爬取
        result = await crawler.arun(
            url="https://example.com",
            word_count_threshold=5,
            exclude_external_links=True,  # 排除外部链接
            exclude_social_media_links=True,  # 排除社交媒体链接
            bypass_cache=True,  # 绕过缓存
            process_iframes=True,  # 处理 iframe
            remove_overlay_elements=True  # 移除覆盖元素
        )
        
        print(f"✅ 高级爬取完成")
        print(f"📊 处理后的内容长度: {len(result.cleaned_html)}")
        print(f"🔗 内部链接: {len(result.links.get('internal', []))}")
        print(f"🌐 外部链接: {len(result.links.get('external', []))}")
        print(f"✅ 页面成功处理: {result.success}")

async def content_filtering_example():
    """内容过滤示例"""
    print("\n🔍 内容过滤示例")
    print("=" * 50)
    
    async with AsyncWebCrawler() as crawler:
        # 使用内容过滤
        result = await crawler.arun(
            url="https://httpbin.org/html",
            excluded_tags=['script', 'style', 'nav', 'footer'],  # 排除特定标签
            word_count_threshold=10,  # 最小词数阈值
            only_text=False  # 保留HTML结构
        )
        
        print(f"✅ 内容过滤完成")
        print(f"📄 过滤后HTML长度: {len(result.html)}")
        print(f"📝 清洁内容长度: {len(result.cleaned_html)}")
        print(f"🎯 Markdown长度: {len(result.markdown)}")

async def multiple_urls_example():
    """多URL爬取示例"""
    print("\n🌐 多URL爬取示例")
    print("=" * 50)
    
    urls = [
        "https://httpbin.org/html",
        "https://httpbin.org/json",
        "https://httpbin.org/user-agent"
    ]
    
    async with AsyncWebCrawler() as crawler:
        # 批量爬取多个URL
        results = await crawler.arun_many(
            urls=urls,
            word_count_threshold=5
        )
        
        print(f"✅ 批量爬取完成")
        print(f"📊 爬取URL数量: {len(results)}")
        
        for i, result in enumerate(results):
            if result.success:
                print(f"  {i+1}. {urls[i]} - 成功 (长度: {len(result.markdown)})")
            else:
                print(f"  {i+1}. {urls[i]} - 失败: {result.error_message}")

async def main():
    """主函数 - 运行所有示例"""
    print("🎯 Crawl4AI 官方文档示例测试")
    print("基于官方文档: https://docs.crawl4ai.com/")
    print("=" * 60)
    
    try:
        # 运行各种示例
        await basic_crawling_example()
        await structured_extraction_example()
        await markdown_generation_example()
        await advanced_crawling_example()
        await content_filtering_example()
        await multiple_urls_example()
        
        print("\n" + "=" * 60)
        print("🎉 所有示例测试完成！")
        print("💡 你现在可以根据这些示例开始使用 Crawl4AI 了")
        print("📚 更多信息请访问: https://docs.crawl4ai.com/")
        
    except Exception as e:
        print(f"❌ 运行示例时发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
