# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys
import django

# 获取当前文件的路径
# current: .../backend/crawler/crawler/
current_dir = os.path.dirname(os.path.abspath(__file__))
# print(f"当前文件路径：{current_dir}")

# 往上跳 2 层，找到 backend 目录
#  .../backend/crawler/crawler <- 目前
#  .../backend/crawler
#  .../backend (这里有 manage.py)
backend_path = os.path.dirname(os.path.dirname(current_dir))

# 将 backend 目录加入系统路径，这样 Python 才能找到 'spiderscope' 模块
sys.path.append(backend_path)

# --- 调试代码 ---
# print(f"DEBUG: Backend 路径设为: {backend_path}")
# print(f"DEBUG: Backend 目录下有哪些文件? {os.listdir(backend_path)}")
# -------------------------------------

# 指定 Django 的配置文件 (假设你的 Django 项目名叫 spiderscope)
os.environ['DJANGO_SETTINGS_MODULE'] = 'spiderscope.settings'

# 启动 Django
django.setup()


BOT_NAME = "crawler"

SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "crawler (+http://www.yourdomain.com)"

# 1. 遵守 Robots 协议设为 False (否则招聘网站什么都不让你爬)
ROBOTSTXT_OBEY = False

# 2. 爬取数量限制 (当抓取到 500 个职位后，爬虫自动停止)
CLOSESPIDER_ITEMCOUNT = 500

# 3. 下载延迟 (模拟人类慢速浏览)
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# 4. 默认请求头 (伪装成浏览器)
DEFAULT_REQUEST_HEADERS = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "crawler.middlewares.CrawlerSpiderMiddleware": 543,
#}

DOWNLOAD_HANDLERS = {
   "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
   "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
   "headless": True,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
