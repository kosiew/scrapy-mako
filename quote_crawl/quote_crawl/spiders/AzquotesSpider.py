

import scrapy
from quote_crawl.items import QuoteCrawlItem
from quote_crawl.items_loader import QuoteLoader

class AzquotesSpider(scrapy.Spider):
    name = "AzQuotes"
    allowed_domains = ["www.azquotes.com"]
    start_urls = [
        "https://www.azquotes.com/quotes/topics/life.html",
    ]

    def parse(self, response):
        for quote in response.css('div.wrap-block'):
            loader = QuoteLoader(item=QuoteCrawlItem(), selector=quote)
            loader.add_css("title", "p a.title::text")
            loader.add_css("author", "div.author a::text")
            yield loader.load_item()
