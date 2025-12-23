# -*- coding: utf-8 -*-
"""
主运行脚本 - 完整的自动化流程
"""

import os
import sys
from fetcher import RSSFetcher
from filter import ContentFilter

def main():
    """主函数"""

    print("\n" + "="*60)
    print("高中生搞笑内容平台 - 自动化抓取系统")
    print("="*60)

    # 步骤1: 抓取RSS内容
    print("\n[步骤 1/3] 抓取RSS内容...")
    fetcher = RSSFetcher()
    contents = fetcher.fetch_all()

    if not contents:
        print("没有获取到新内容")
        return

    fetcher.save(contents)

    # 步骤2: 内容过滤
    print("\n[步骤 2/3] 内容过滤...")
    filter_obj = ContentFilter()
    results = filter_obj.filter_all(contents)
    filter_obj.save_results(results)

    # 步骤3: 统计
    print("\n[步骤 3/3] 统计信息...")

    try:
        with open('data/approved_content.json', 'r', encoding='utf-8') as f:
            all_approved = json.load(f)
        print(f"   总内容数: {len(all_approved)} 条")
    except:
        print("   总内容数: 0 条")

    print("\n" + "="*60)
    print("✅ 自动化流程完成!")
    print("="*60)


if __name__ == '__main__':
    import json
    main()
