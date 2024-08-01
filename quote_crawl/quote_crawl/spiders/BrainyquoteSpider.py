

import scrapy
from quote_crawl.items import QuoteCrawlItem
from quote_crawl.items_loader import QuoteLoader

class BrainyquoteSpider(scrapy.Spider):
    name = "BrainyQuote"
    allowed_domains = ["www.brainyquote.com"]
    start_urls = [
        "https://www.brainyquote.com/topics/life-quotes",
    ]

    def parse(self, response):
        for quote in response.css('div.grid-item.qb.clearfix.bqQt'):
            loader = QuoteLoader(item=QuoteCrawlItem(), selector=quote)
            loader.add_css("title", "div::text")
            loader.add_css("author", "a.bq-aut.qa_109542.oncl_a::text")
            yield loader.load_item()
