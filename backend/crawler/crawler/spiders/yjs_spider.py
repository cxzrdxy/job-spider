import scrapy

class YjsSpider(scrapy.Spider):
    name = "yingjiesheng"
    allowed_domains = ["yingjiesheng.com"]
    start_urls = ["https://www.yingjiesheng.com/"]

    def parse(self, response):
        self.logger.info(f"访问应届生求职网: {response.url}")
