# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrapyItem(scrapy.Item):  ## the class name "NewscrapyItem" is generated automatically
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title = scrapy.Field() # The titles of news
    news_date = scrapy.Field()     # time of news
    news_url = scrapy.Field()   # the detailed links of news
    
