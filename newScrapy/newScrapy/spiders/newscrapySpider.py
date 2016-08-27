# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:47:38 2016

@author: ceciliaLee
"""

# -*- coding: utf-8 -*-
import scrapy
from newScrapy.items import NewscrapyItem
import logging
class newscrapySpider(scrapy.Spider):
    name = "newScrapy"  ## the name of the crawler
    allowed_domains = ["njupt.edu.cn"]  # the range of crawling domain
    start_urls = [
        "http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/1/list.htm",
        ]  ## The starting url to visie, the result will return to parse() function
    
    def parse(self, response): ## Deal with the returned response after requesting for start_urls
        news_page_num = 14  ## The number of pieces of news in each page
        page_num = 423  ## Total pages of news
        if response.status == 200:
            for i in range(2,page_num+1):
                for j in range(1,news_page_num+1):
                    item = NewscrapyItem() ## using the defined item to store the title, url, time of news
                    item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                    "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                    "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()
                  
                    yield item  ## deliver the stored item to pipelines for subsequent processing
                ## Crawling the news of next pages   
                next_page_url = "http://news.njupt.edu.cn/s/222/t/1100/p/1/c/6866/i/"+str(i)+"/list.htm"
                yield scrapy.Request(next_page_url,callback=self.parse_news)
        
    def parse_news(self, response):
        news_page_num = 14
        if response.status == 200:
            for j in range(1,news_page_num+1):
                item = NewscrapyItem()
                item['news_url'],item['news_title'],item['news_date'] = response.xpath(
                "//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/font/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//td[@class='postTime']/text()"
                "|//div[@id='newslist']/table[1]/tr["+str(j)+"]//a/@href").extract()
                yield item
