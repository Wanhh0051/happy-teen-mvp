# 开心高中生 - Happy Teen MVP

> 适合高中生的幽默内容平台 | 零成本 | 全自动 | 安全过滤

## 项目简介

Happy Teen MVP 是一个专为15-18岁高中生设计的幽默内容平台。通过RSS自动抓取、智能过滤和移动端友好的界面，为高中生提供健康、有趣的日常娱乐内容。

### 核心特点

- **零成本运营**: 使用Vercel免费套餐 + GitHub Actions
- **全自动化**: 每6小时自动抓取RSS内容
- **三级过滤**: APPROVE/REVIEW/REJECT智能内容过滤
- **移动优先**: 响应式设计，完美适配手机端
- **安全可控**: 内置敏感词库，确保内容适合高中生

### 内容分类

- 搞笑日常 - 校园生活中的趣事
- 校园学习 - 学习相关的轻松内容
- 正能量 - 积极向上的励志内容

## 快速开始

### 本地运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 抓取RSS内容（可选）
python run.py

# 3. 启动开发服务器
python app.py
```

访问: http://localhost:5000

### 部署到Vercel

```bash
# 1. 安装Vercel CLI
npm install -g vercel

# 2. 登录
vercel login

# 3. 部署
vercel
```

详细部署指南请查看 [DEPLOYMENT.md](DEPLOYMENT.md)

## 项目结构

```
happy-teen-mvp/
├── api/index.py            # Vercel Serverless API
├── public/index.html       # 前端页面
├── config.py               # 配置文件（RSS源、敏感词）
├── fetcher.py              # RSS抓取器
├── filter.py               # 内容过滤器
├── app.py                  # 本地Flask开发服务器
├── run.py                  # 完整运行脚本
├── requirements.txt        # Python依赖
├── vercel.json             # Vercel配置
└── .github/workflows/      # GitHub Actions自动化
```

## API接口

### GET /api/content
随机返回10条内容

### GET /api/content/{category}
按分类返回内容
- category: `搞笑日常` | `校园学习` | `正能量`

### GET /api/random
随机返回1条内容

## 内容过滤

### 过滤规则

1. **长度验证**: 20-500字
2. **敏感词过滤**: 绝对禁止的内容
3. **人工审核**: 需要人工判断的边缘内容

### 敏感词库

```python
# 绝对禁止
TEENAGER_SENSITIVE_WORDS = [
    '自杀', '自残', '想死', '结束生命',
    '色情', '成人',
    '赌博', '吸毒',
]

# 需要人工审核
MANUAL_REVIEW_WORDS = [
    '早恋', '分手',
    '不想活了', '活着没意思',
]
```

## 配置

编辑 `config.py` 添加RSS源:

```python
RSS_SOURCES = {
    '搞笑日常': [
        'https://rss.wilsond.cn/weibo/user/1742566624',
        'https://your-rss-source',
    ],
    '校园学习': [
        # 添加RSS源
    ],
}
```

## 自动化

项目使用GitHub Actions实现自动抓取:

- **触发方式**: 定时任务 (每6小时) 或 手动触发
- **自动提交**: 抓取的内容自动提交到仓库
- **零人工干预**: 完全自动运行

## 技术栈

- **后端**: Python + Flask (本地开发)
- **部署**: Vercel Serverless Functions
- **前端**: HTML + CSS + JavaScript (无框架)
- **数据存储**: JSON文件
- **自动化**: GitHub Actions
- **RSS解析**: feedparser

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎提出Issue。
