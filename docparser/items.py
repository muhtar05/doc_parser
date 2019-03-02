# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DOCParserItem(scrapy.Item):
    url = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    related_items = scrapy.Field()
    price_mrc = scrapy.Field()