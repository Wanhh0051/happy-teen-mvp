# -*- coding: utf-8 -*-
"""
RSS自动抓取脚本
"""

import feedparser
import json
import os
from datetime import datetime
import config

class RSSFetcher:
    """RSS内容抓取器"""

    def __init__(self):
        self.sources = config.RSS_SOURCES

    def fetch_from_url(self, url, category):
        """从单个RSS URL抓取内容"""
        try:
            feed = feedparser.parse(url)

            contents = []
            for entry in feed.entries:
                content = {
                    'title': entry.get('title', ''),
                    'content': entry.get('summary', entry.get('description', '')),
                    'link': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'category': category,
                    'fetched_at': datetime.now().isoformat()
                }

                # 内容不为空
                if content['content']:
                    contents.append(content)

            return contents

        except Exception as e:
            print(f"抓取失败 {url}: {e}")
            return []

    def fetch_all(self):
        """抓取所有RSS源"""
        all_content = []

        print("\n" + "="*50)
        print("开始抓取RSS内容...")
        print("="*50)

        for category, urls in self.sources.items():
            print(f"\n分类: {category}")

            for url in urls:
                print(f"  → {url}")
                contents = self.fetch_from_url(url, category)
                print(f"    获取 {len(contents)} 条")
                all_content.extend(contents)

        # 去重
        unique_content = self._remove_duplicates(all_content)

        print(f"\n总计: {len(all_content)} 条 (去重后 {len(unique_content)} 条)")

        return unique_content

    def _remove_duplicates(self, contents):
        """根据链接去重"""
        seen = set()
        unique = []

        for item in contents:
            if item['link'] not in seen:
                seen.add(item['link'])
                unique.append(item)

        return unique

    def save(self, contents):
        """保存到文件"""
        # 确保目录存在
        os.makedirs(config.DATA_DIR, exist_ok=True)

        # 保存新抓取的内容
        with open(config.CONTENT_FILE, 'w', encoding='utf-8') as f:
            json.dump(contents, f, ensure_ascii=False, indent=2)

        print(f"\n已保存到 {config.CONTENT_FILE}")


if __name__ == '__main__':
    fetcher = RSSFetcher()
    contents = fetcher.fetch_all()
    fetcher.save(contents)

    print("\n" + "="*50)
    print("抓取完成!")
    print("="*50)
