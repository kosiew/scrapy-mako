<%!
from mako.template import Template
%>

import scrapy
from quote_crawl.items import QuoteCrawlItem
from quote_crawl.items_loader import QuoteLoader

class ${spiderclass}(scrapy.Spider):
    name = "${spidername}"
    allowed_domains = ["${allowed_domains}"]
    start_urls = [
        % for url in start_urls:
        "${url}",
        % endfor
    ]
    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        for main in response.css('${quote_div_main}'):
            quotes = main.css('${title_selector}::text').getall()
            authors = main.css('${author_selector}::text').getall()
            for quote, author in zip(quotes, authors):
                loader = QuoteLoader(item=QuoteCrawlItem())
                loader.add_value("title", quote)
                loader.add_value("author", author)
                yield loader.load_item()
