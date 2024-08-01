<%!
from mako.template import Template
%>

import scrapy

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
            yield {
                'title': quote.css('${title_selector}').get(),
                'author': quote.css('${author_selector}').get(),
            }
