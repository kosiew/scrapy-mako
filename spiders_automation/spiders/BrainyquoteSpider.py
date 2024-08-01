

import scrapy

class BrainyquoteSpider(scrapy.Spider):
    name = "BrainyQuote"
    allowed_domains = ["www.brainyquote.com"]
    start_urls = [
        "https://www.brainyquote.com/topics/life-quotes",
    ]

    def parse(self, response):
        for quote in response.css('div.grid-item.qb.clearfix.bqQt'):
            yield {
                'title': quote.css('div').get(),
                'author': quote.css('a.bq-aut.qa_109542.oncl_a').get(),
            }
