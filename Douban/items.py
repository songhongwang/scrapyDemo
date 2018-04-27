# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    star = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()


class Poem(scrapy.Item):
    type = scrapy.Field()
    name = scrapy.Field()
    dynasty = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    translation = scrapy.Field()
    
