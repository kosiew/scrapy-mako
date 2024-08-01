from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


# define your methods to apply on item value
def to_title_case(title):
    return title.title()


# define your loader class
class QuoteLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(str.strip, to_title_case)
    author_in = MapCompose(str.strip, to_title_case)