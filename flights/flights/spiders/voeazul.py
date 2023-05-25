import scrapy


class VoeazulSpider(scrapy.Spider):
    name = "voeazul"
    allowed_domains = ["voeazul.com.br"]
    start_urls = ["https://voeazul.com.br"]

    def parse(self, response):
        pass
