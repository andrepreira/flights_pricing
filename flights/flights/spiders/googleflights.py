import scrapy


class GoogleflightsSpider(scrapy.Spider):
    name = "googleflights"
    allowed_domains = ["www.google.com"]
    start_urls = ["https://www.google.com/travel/flights"]

    def parse(self, response):
        pass
