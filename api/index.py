# -*- coding: utf-8 -*-
"""
Vercel Serverless API - Happy Teen MVP
"""

import json
import random
import os
from pathlib import Path

# 数据文件路径（Vercel环境）
DATA_DIR = Path(__file__).parent.parent / 'data'
DATA_FILE = DATA_DIR / 'approved_content.json'

def load_content():
    """加载内容"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def handler(request):
    """主处理函数"""
    # 获取请求路径和方法
    path = request.path
    method = request.method.upper()

    # 只处理GET请求
    if method != 'GET':
        return {
            'statusCode': 405,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'success': False, 'message': 'Method not allowed'})
        }

    contents = load_content()

    # 主页路由 - 返回HTML
    if path == '/' or path == '/index':
        with open(Path(__file__).parent.parent / 'public' / 'index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': html_content
        }

    # API路由
    if path == '/api/content' or path == '/api/':
        # 获取10条随机内容
        if contents:
            selected = random.sample(contents, min(10, len(contents)))
        else:
            selected = []

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'success': True, 'data': selected}, ensure_ascii=False)
        }

    elif path.startswith('/api/content/'):
        # 按分类获取
        category = path.split('/')[-1]
        from urllib.parse import unquote
        category = unquote(category)

        filtered = [c for c in contents if c.get('category') == category]

        if filtered:
            selected = random.sample(filtered, min(10, len(filtered)))
        else:
            selected = []

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'success': True, 'category': category, 'data': selected}, ensure_ascii=False)
        }

    elif path == '/api/random':
        # 获取1条随机内容
        if contents:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'success': True, 'data': random.choice(contents)}, ensure_ascii=False)
            }
        else:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'success': False, 'message': '暂无内容'}, ensure_ascii=False)
            }

    # 默认返回
    return {
        'statusCode': 404,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'success': False, 'message': 'Not found'})
    }
