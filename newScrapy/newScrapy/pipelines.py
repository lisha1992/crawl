# -*- coding: utf-8 -*-

# Define your item pipelines here
# pipelines.py is used for further processing of data, such as type conversion, 
# restore in databases, write to local machine, and so on
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
## pipelines.py is called after the yield item in spider, it is used to process each single item
import json

class NewscrapyPipeline(object):
    def __init__(self):
        self.file = open('newScrapy.txt',mode='wb')  
        
    def process_item(self, item, spider):
        self.file.write(item['news_title'].encode("utf-8"))
        self.file.write("\n")
        self.file.write(item['news_date'].encode("utf-8"))
        self.file.write("\n")
        self.file.write(item['news_url'].encode("utf-8"))
        self.file.write("\n")
        return item
