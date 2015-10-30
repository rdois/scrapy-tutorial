# -*- coding: utf-8 -*-


import scrapy

class DmozItem(scrapy.item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()