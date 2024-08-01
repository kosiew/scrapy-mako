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

    def parse(self, response):
        for quote in response.css('${quote_div_main}'):
            loader = QuoteLoader(item=QuoteCrawlItem(), selector=quote)
            loader.add_css("title", "${title_selector}::text")
            loader.add_css("author", "${author_selector}::text")
            yield loader.load_item()
