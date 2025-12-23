# -*- coding: utf-8 -*-
"""
配置文件 - 高中生搞笑内容平台
"""

# ================================
# RSS源配置
# ================================

RSS_SOURCES = {
    '搞笑日常': [
        'https://rss.wilsond.cn/weibo/user/1742566624',  # 这种bot
        # 可添加更多RSS源
    ],
    '校园学习': [
        # 待添加
    ],
    '正能量': [
        # 待添加
    ],
}

# ================================
# 内容过滤配置
# ================================

# 敏感词库（高中生肖用）
TEENAGER_SENSITIVE_WORDS = [
    # 绝对禁止
    '自杀', '自残', '想死', '结束生命',
    '色情', '成人',
    '赌博', '吸毒',
]

# 需要人工审核的词
MANUAL_REVIEW_WORDS = [
    '早恋', '分手',
    '不想活了', '活着没意思',
]

# 内容长度限制
CONTENT_LENGTH = {
    'min': 20,   # 最小20字
    'max': 500,  # 最大500字
}

# ================================
# 数据存储配置
# ================================

DATA_DIR = 'data'
CONTENT_FILE = 'data/content.json'
APPROVED_FILE = 'data/approved_content.json'

# ================================
# 自动化配置
# ================================

AUTO_FETCH = {
    'enabled': True,
    'interval_hours': 6,  # 每6小时抓取一次
}

MANUAL_REVIEW = {
    'enabled': True,
    'auto_approve_safe': True,  # 安全内容自动通过
}
