# -*- coding: utf-8 -*-
"""
Web应用 - 高中生搞笑内容平台
使用Flask框架
"""

from flask import Flask, render_template, jsonify
import json
import random
import os

app = Flask(__name__)

# 数据文件路径
DATA_FILE = 'data/approved_content.json'

def load_content():
    """加载内容"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

@app.route('/')
def index():
    """首页"""
    return render_template('index.html')

@app.route('/api/content')
def api_content():
    """获取内容API"""
    contents = load_content()

    # 随机返回10条
    if contents:
        selected = random.sample(contents, min(10, len(contents)))
    else:
        selected = []

    return jsonify({
        'success': True,
        'data': selected
    })

@app.route('/api/content/<category>')
def api_content_by_category(category):
    """按分类获取内容"""
    contents = load_content()

    # 筛选分类
    filtered = [c for c in contents if c.get('category') == category]

    # 随机返回10条
    if filtered:
        selected = random.sample(filtered, min(10, len(filtered)))
    else:
        selected = []

    return jsonify({
        'success': True,
        'category': category,
        'data': selected
    })

@app.route('/api/random')
def api_random():
    """随机获取一条"""
    contents = load_content()

    if contents:
        return jsonify({
            'success': True,
            'data': random.choice(contents)
        })
    else:
        return jsonify({
            'success': False,
            'message': '暂无内容'
        })

if __name__ == '__main__':
    # 创建templates目录
    os.makedirs('templates', exist_ok=True)

    print("\n" + "="*50)
    print("Web服务器启动中...")
    print("访问地址: http://localhost:5000")
    print("="*50 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
