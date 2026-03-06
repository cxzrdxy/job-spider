import scrapy

class Job51Spider(scrapy.Spider):
    name = "job51"
    allowed_domains = ["51job.com"]
    start_urls = ["https://www.51job.com/"]

    def parse(self, response):
        self.logger.info(f"访问 51job: {response.url}")
