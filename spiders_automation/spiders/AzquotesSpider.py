

import scrapy

class AzquotesSpider(scrapy.Spider):
    name = "AzQuotes"
    allowed_domains = ["www.azquotes.com"]
    start_urls = [
        "https://www.azquotes.com/quotes/topics/life.html",
    ]

    def parse(self, response):
        for quote in response.css('div.wrap-block'):
            yield {
                'title': quote.css('p a.title').get(),
                'author': quote.css('div.author a').get(),
            }
