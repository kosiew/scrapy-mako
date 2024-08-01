# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class QuoteCrawlPipeline:
    def process_item(self, item, spider):
        return item


class FilterQuotesPipelineLoveOrLife:
    def process_item(self, item, spider):
        # Check if 'love' or 'life' is in the text
        if "love" in item["title"].lower() or "life" in item["title"].lower():
            return item
        else:
            raise DropItem(
                f"Quote without 'love' or 'life' in title text: {item['title']}"
            )
