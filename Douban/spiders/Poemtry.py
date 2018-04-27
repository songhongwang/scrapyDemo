# -*- coding: utf-8 -*-
import scrapy
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

from Douban.items import Poem 
import imp
SqlUtilsPoem = imp.load_source('SqlUtilsPoem', '../mysql/sqlutils_poem.py')

from SqlUtilsPoem import SqlUtilsPoem

import time


class PoemtrySpider(scrapy.Spider):
    name = 'Poemtry'
    allowed_domains = ['m.gushiwen.org']
    start_urls = [
        'https://m.gushiwen.org/gushi/tangshi.aspx'
    ]

    def __init__(self):
        self.arr = ['五言绝句','七言绝句','五言律诗','七言律诗','五言古诗','七言古诗','乐府']
        self.regex = "//div[@class='bookMl']//strong[.='@@']//../following-sibling::span//a/@href"
        self.current_type = self.arr[0]
 
    def parse(self, response):
        poem = Poem() 
        name = response.xpath('//div[@class="sons"][1]//div[@class="cont"]/h1/text()').extract()
        if len(name) > 0: # 避开首轮循环
            poem['type'] = response.meta['item_type'] # 首轮循环没有此参数 因为首轮循环的是首页
            poem['name'] = name[0].strip().encode("utf8").replace("\'","")

            dynasty_map = response.xpath('//div[@class="sons"][1]//div[@class="cont"]/p/a/text()').extract()
            poem['dynasty'] = dynasty_map[0].encode("utf8").replace("\'","")
            poem['author'] = dynasty_map[1].encode("utf8").replace("\'","")

            content_node = response.xpath('//div[@class="sons"][1]//div[@class="cont"]//div[@class="contson"]')
            poem['content'] = content_node.xpath('string(.)').extract()[0].strip().encode("utf8").replace("\'","")

            poem['translation'] = response.xpath('//div[@class="contyishang"]//p[1]').extract()[0].strip().encode("utf8").replace("\'","").replace('</p>','').replace('<p>','').replace('<br>','@')
            
      
            print("=============== complete poem " + poem['type'])
            # time.sleep(2)
            # 存盘
            mysql = SqlUtilsPoem()
            mysql.insert(poem)

            yield poem


        # 相当于分页
        for item in self.arr:
            result = self.regex.replace("@@", ""+item)
            urls = response.xpath(u""+result).extract()
            for url in urls:
                url = "http://m.gushiwen.org" + url
                #print("******" + url)
                request = scrapy.Request(url, self.parse) 
                # 传递参数给下一轮循环 
                request.meta['item_type'] = item
                # 开启下一轮循环
                yield request


        
        
        



 
