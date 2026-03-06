# SpiderScope - 智能爬虫管理系统

SpiderScope 是一个基于 Django + Vue3 + Scrapy 的全栈爬虫管理平台，支持多源招聘网站数据采集、任务调度和可视化展示。

## 功能特性

### 核心功能
- **多平台爬虫支持**：BOSS直聘、前程无忧、实习僧、应届生求职网、拉勾网
- **任务调度管理**：支持定时任务、任务状态监控
- **数据可视化**：职位信息展示、数据分析
- **用户权限管理**：多用户支持、任务归属

### 技术亮点
- **混合存储策略**：PostgreSQL 存储结构化数据 + MongoDB 存储原始爬取数据
- **异步任务处理**：Celery + Redis 实现分布式任务队列
- **动态渲染支持**：Playwright 处理 JavaScript 动态页面
- **现代化前端**：Vue3 + Element Plus + Pinia 状态管理

## 技术栈

### 后端
| 技术 | 版本 | 用途 |
|------|------|------|
| Django | 5.2.10 | Web 框架 |
| Django REST Framework | 3.16.1 | API 开发 |
| Scrapy | - | 爬虫框架 |
| Playwright | 1.51.0 | 浏览器自动化 |
| Celery | - | 异步任务队列 |
| PostgreSQL | 15 | 主数据库 |
| MongoDB | 6.0 | 原始数据存储 |
| Redis | 7 | 缓存 + 消息队列 |

### 前端
| 技术 | 版本 | 用途 |
|------|------|------|
| Vue | 3.5.24 | 前端框架 |
| Vite | 7.2.5 | 构建工具 |
| Element Plus | 2.13.1 | UI 组件库 |
| Pinia | 3.0.4 | 状态管理 |
| Vue Router | 4.6.4 | 路由管理 |
| Axios | 1.13.2 | HTTP 客户端 |

## 快速开始

### 环境要求
- Docker & Docker Compose
- 或 Python 3.12+ + Node.js 18+

### 方式一：Docker 部署（推荐）

```bash
# 克隆项目
git clone <your-repo-url>
cd SpiderScope

# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps
```

服务启动后访问：
- 前端界面：http://localhost:5173
- 后端 API：http://localhost:8000

### 方式二：本地开发

#### 1. 后端启动

```bash
cd backend

# 创建虚拟环境
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
python manage.py migrate

# 启动服务
python manage.py runserver
```

#### 2. 前端启动

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

#### 3. 启动 Celery Worker

```bash
cd backend
celery -A spiderscope worker -l info
```

## 项目结构

```
SpiderScope/
├── backend/                 # Django 后端
│   ├── core/               # 核心业务逻辑
│   │   ├── models.py       # 数据模型
│   │   ├── views.py        # API 视图
│   │   ├── serializers.py  # 序列化器
│   │   └── tasks.py        # Celery 任务
│   ├── crawler/            # Scrapy 爬虫
│   │   └── crawler/spiders/# 爬虫实现
│   ├── spiderscope/        # 项目配置
│   │   ├── settings.py     # Django 配置
│   │   ├── urls.py         # 路由配置
│   │   └── celery.py       # Celery 配置
│   └── manage.py           # Django 管理脚本
├── frontend/               # Vue3 前端
│   ├── src/
│   │   ├── views/          # 页面组件
│   │   ├── components/     # 通用组件
│   │   ├── stores/         # Pinia 状态
│   │   └── router/         # 路由配置
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml      # Docker 编排
└── README.md
```

## 数据模型

### SpiderTask（爬虫任务）
- 任务名称、目标 URL
- 爬虫配置（JSON 格式，灵活存储）
- 抓取频率、状态管理
- 创建人关联

### Job（职位信息）
- 基础信息：职位名称、薪资、公司、地点
- 进阶要求：经验、学历
- 公司画像：行业、规模
- 职位详情：标签、福利、描述
- 来源平台标记

## API 接口

### 认证
- `POST /api/token/` - 获取 JWT Token
- `POST /api/token/refresh/` - 刷新 Token

### 爬虫任务
- `GET /api/tasks/` - 任务列表
- `POST /api/tasks/` - 创建任务
- `GET /api/tasks/{id}/` - 任务详情
- `PUT /api/tasks/{id}/` - 更新任务
- `DELETE /api/tasks/{id}/` - 删除任务

### 职位数据
- `GET /api/jobs/` - 职位列表
- `GET /api/jobs/{id}/` - 职位详情

## 支持的爬虫平台

| 平台 | 状态 | 说明 |
|------|------|------|
| BOSS直聘 | ✅ | 主流招聘平台 |
| 前程无忧 | ✅ | 综合招聘网站 |
| 实习僧 | ✅ | 实习生招聘 |
| 应届生求职网 | ✅ | 校园招聘 |
| 拉勾网 | ✅ | 互联网招聘 |

## 配置说明

### 环境变量

```env
# 数据库
DB_HOST=localhost
DB_NAME=spider_db
DB_USER=spider_user
DB_PASSWORD=your_password
DB_PORT=5432

# Redis
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# MongoDB
MONGO_URI=mongodb://localhost:27017/

# Django
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

## 开发计划

- [ ] 数据可视化仪表盘
- [ ] 爬虫性能监控
- [ ] 数据导出功能（Excel/CSV）
- [ ] 更多数据源接入
- [ ] 分布式爬虫部署

## 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 [MIT](LICENSE) 许可证

## 联系方式

如有问题或建议，欢迎提交 Issue 或 Pull Request。
