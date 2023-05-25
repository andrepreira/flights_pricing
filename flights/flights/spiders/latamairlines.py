import scrapy


class LatamairlinesSpider(scrapy.Spider):
    name = "latamairlines"
    allowed_domains = ["latamairlines.com"]
    start_urls = ["https://latamairlines.com"]

    def parse(self, response):
        pass
