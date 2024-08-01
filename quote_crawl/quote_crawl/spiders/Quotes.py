import scrapy

from quote_crawl.quote_crawl.items import QuoteCrawlItem


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # each quote is within <div class="quote" ...>
        quotes = response.css("div.quote")
        for quote in quotes:
            quote_item = QuoteCrawlItem()
            # each quote text is within <span class="text" ...>
            title = quote.css("span.text::text").get()
            # each author info is within <small class="author" ...>
            author = quote.css("small.author::text").get()
            quote_item["title"] = title
            quote_item["author"] = author
            yield quote_item
