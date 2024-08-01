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
        for quote in response.css('${quote_div_main}'):
            loader = QuoteLoader(item=QuoteCrawlItem(), selector=quote)
            loader.add_css("title", "${title_selector}::text")
            loader.add_css("author", "${author_selector}::text")
            yield loader.load_item()
