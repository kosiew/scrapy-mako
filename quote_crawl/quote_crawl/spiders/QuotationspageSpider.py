

import scrapy
from quote_crawl.items import QuoteCrawlItem
from quote_crawl.items_loader import QuoteLoader

class QuotationspageSpider(scrapy.Spider):
    name = "QuotationsPage"
    allowed_domains = ["www.quotationspage.com"]
    start_urls = [
        "http://www.quotationspage.com/qotd.html",
    ]
    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        for main in response.css('dl'):
            quotes = main.css('dt.quote a::text').getall()
            authors = main.css('dd.author b a::text').getall()
            for quote, author in zip(quotes, authors):
                loader = QuoteLoader(item=QuoteCrawlItem())
                loader.add_value("title", quote)
                loader.add_value("author", author)
                yield loader.load_item()
