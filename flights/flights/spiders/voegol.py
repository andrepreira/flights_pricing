import scrapy


class VoegolSpider(scrapy.Spider):
    name = "voegol"
    allowed_domains = ["voegol.com.br"]
    start_urls = ["https://voegol.com.br"]

    def parse(self, response):
        pass
