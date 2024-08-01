

import scrapy
from quote_crawl.items import QuoteCrawlItem
from quote_crawl.items_loader import QuoteLoader

class AzquotesSpider(scrapy.Spider):
    name = "AzQuotes"
    allowed_domains = ["www.azquotes.com"]
    start_urls = [
        "https://www.azquotes.com/quotes/topics/life.html",
    ]
    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        for quote in response.css('div.wrap-block'):
            loader = QuoteLoader(item=QuoteCrawlItem(), selector=quote)
            loader.add_css("title", "p a.title::text")
            loader.add_css("author", "div.author a::text")
            yield loader.load_item()
