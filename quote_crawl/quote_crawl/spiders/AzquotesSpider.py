

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
        for main in response.css('div.wrap-block'):
            quotes = main.css('p a.title::text').getall()
            authors = main.css('div.author a::text').getall()
            for quote, author in zip(quotes, authors):
                loader = QuoteLoader(item=QuoteCrawlItem())
                loader.add_value("title", quote)
                loader.add_value("author", author)
                yield loader.load_item()
