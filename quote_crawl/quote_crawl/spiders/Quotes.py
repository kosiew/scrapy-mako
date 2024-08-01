import scrapy
from quote_crawl.items import QuoteCrawlItem
from quote_crawl.items_loader import QuoteLoader


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # each quote is within <div class="quote" ...>
        quotes = response.css("div.quote")
        for quote in quotes:
            loader = QuoteLoader(item=QuoteCrawlItem(), selector=quote)
            loader.add_css("title", "span.text::text")
            loader.add_css("author", "small.author::text")
            yield loader.load_item()
