# 部署指南 - Happy Teen MVP

## 项目结构

```
happy-teen-mvp/
├── api/
│   └── index.py           # Vercel Serverless API
├── public/
│   └── index.html         # 前端页面
├── data/
│   └── approved_content.json  # 审核通过的内容
├── config.py              # 配置文件
├── fetcher.py             # RSS抓取器
├── filter.py              # 内容过滤器
├── app.py                 # 本地Flask开发服务器
├── run.py                 # 本地运行脚本
├── requirements.txt       # Python依赖
├── vercel.json            # Vercel配置
└── .github/workflows/
    └── auto_fetch.yml     # GitHub Actions自动抓取
```

## 本地开发

### 1. 安装依赖

```bash
cd C:\Users\Administrator\happy-teen-mvp
pip install -r requirements.txt
```

### 2. 抓取RSS内容

```bash
python run.py
```

### 3. 启动本地开发服务器

```bash
python app.py
```

访问: http://localhost:5000

## Vercel部署

### 步骤1: 安装Vercel CLI

```bash
npm install -g vercel
```

### 步骤2: 登录Vercel

```bash
vercel login
```

### 步骤3: 部署项目

```bash
cd C:\Users\Administrator\happy-teen-mvp
vercel
```

按提示操作：
- 链接到现有项目或创建新项目
- 确认项目设置
- 部署完成

### 步骤4: 设置生产环境

```bash
vercel --prod
```

## 部署到GitHub + Vercel（推荐）

### 1. 创建GitHub仓库

```bash
git init
git add .
git commit -m "Initial commit: Happy Teen MVP"
```

### 2. 推送到GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/happy-teen-mvp.git
git branch -M main
git push -u origin main
```

### 3. 在Vercel导入项目

1. 访问 https://vercel.com
2. 点击 "New Project"
3. 导入GitHub仓库
4. Vercel会自动检测配置并部署

### 4. 配置GitHub Actions自动化

推送后，GitHub Actions会自动每6小时抓取一次RSS内容。

### 5. 在GitHub仓库手动触发抓取

1. 访问你的GitHub仓库
2. 点击 "Actions" 标签
3. 选择 "自动抓取RSS内容"
4. 点击 "Run workflow" → "Run workflow"

## 其他免费部署平台

### Railway

1. 访问 https://railway.app
2. 点击 "New Project"
3. 选择 "Deploy from GitHub repo"
4. 选择你的仓库
5. Railway会自动检测Python项目并部署

### Render

1. 访问 https://render.com
2. 点击 "New" → "Web Service"
3. 连接GitHub仓库
4. 配置:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. 点击 "Deploy"

## 添加RSS源

编辑 `config.py`:

```python
RSS_SOURCES = {
    '搞笑日常': [
        'https://your-rss-source-1',
        'https://your-rss-source-2',
    ],
    '校园学习': [
        'https://your-rss-source-3',
    ],
}
```

然后运行 `python run.py` 抓取新内容。

## 测试数据

项目包含3条测试数据在 `data/approved_content.json`:
- 数学课的趣事 (校园学习)
- 食堂奇遇 (搞笑日常)
- 学习小技巧 (正能量)

## 抓取真实内容

确保有网络连接，然后运行:

```bash
pip install feedparser
python run.py
```

内容会自动抓取、过滤并保存到 `data/approved_content.json`。

## 项目特点

- 零成本：使用Vercel免费套餐
- 自动化：GitHub Actions每6小时自动抓取
- 安全：三级内容过滤（APPROVE/REVIEW/REJECT）
- 移动端响应式设计
- 适合15-18岁高中生

## 常见问题

**Q: Vercel部署后API返回404？**
A: 确保 `vercel.json` 配置正确，重新部署。

**Q: GitHub Actions失败？**
A: 检查仓库设置 → Actions → General → Workflow permissions，确保有写入权限。

**Q: 如何更新敏感词列表？**
A: 编辑 `config.py` 中的 `TEENAGER_SENSITIVE_WORDS` 和 `MANUAL_REVIEW_WORDS`。

## 许可证

MIT License
