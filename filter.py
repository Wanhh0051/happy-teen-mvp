# -*- coding: utf-8 -*-
"""
内容过滤脚本
"""

import json
import os
import config

class ContentFilter:
    """内容过滤器"""

    def __init__(self):
        self.sensitive_words = config.TEENAGER_SENSITIVE_WORDS
        self.review_words = config.MANUAL_REVIEW_WORDS
        self.length_config = config.CONTENT_LENGTH

    def filter_all(self, contents):
        """过滤所有内容"""
        print("\n" + "="*50)
        print("开始内容过滤...")
        print("="*50)

        results = {
            'approved': [],
            'review': [],
            'rejected': []
        }

        for item in contents:
            result = self._filter_item(item)

            if result == 'APPROVE':
                results['approved'].append(item)
            elif result == 'REVIEW':
                results['review'].append(item)
            else:  # REJECT
                # 拒绝的内容不保存
                pass

        print(f"\n过滤结果:")
        print(f"  ✅ 通过: {len(results['approved'])} 条")
        print(f"  ⚠️  需审核: {len(results['review'])} 条")
        print(f"  ❌ 拒绝: 已过滤")

        return results

    def _filter_item(self, item):
        """过滤单个内容"""

        # 合并标题和内容进行检查
        text = item.get('title', '') + item.get('content', '')

        # 检查1: 长度
        if len(text) < self.length_config['min']:
            return 'REJECT'
        if len(text) > self.length_config['max']:
            return 'REJECT'

        # 检查2: 绝对禁止的词
        for word in self.sensitive_words:
            if word in text:
                return 'REJECT'

        # 检查3: 需要人工审核的词
        for word in self.review_words:
            if word in text:
                return 'REVIEW'

        # 通过所有检查
        return 'APPROVE'

    def save_results(self, results):
        """保存过滤结果"""
        os.makedirs(config.DATA_DIR, exist_ok=True)

        # 保存通过的内容
        approved = results['approved']
        review = results['review']

        # 加载已有的审核通过内容
        try:
            with open(config.APPROVED_FILE, 'r', encoding='utf-8') as f:
                old_approved = json.load(f)
        except:
            old_approved = []

        # 去重
        old_links = {item['link'] for item in old_approved}
        new_approved = [item for item in approved if item['link'] not in old_links]

        # 合并
        all_approved = old_approved + new_approved

        # 保存
        with open(config.APPROVED_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_approved, f, ensure_ascii=False, indent=2)

        # 保存待审核内容
        if review:
            review_file = 'data/review_queue.json'
            with open(review_file, 'w', encoding='utf-8') as f:
                json.dump(review, f, ensure_ascii=False, indent=2)
            print(f"\n⚠️  有 {len(review)} 条内容需要人工审核")
            print(f"   已保存到 {review_file}")

        print(f"\n✅ 已保存 {len(all_approved)} 条审核通过的内容")
        print(f"   新增: {len(new_approved)} 条")


if __name__ == '__main__':
    # 读取新抓取的内容
    try:
        with open(config.CONTENT_FILE, 'r', encoding='utf-8') as f:
            contents = json.load(f)
    except:
        print("没有找到新抓取的内容")
        exit()

    # 过滤
    filter_obj = ContentFilter()
    results = filter_obj.filter_all(contents)
    filter_obj.save_results(results)

    print("\n" + "="*50)
    print("过滤完成!")
    print("="*50)
