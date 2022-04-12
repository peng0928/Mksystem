# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MkspideItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    people = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    mark = scrapy.Field()
    text_data = scrapy.Field()
