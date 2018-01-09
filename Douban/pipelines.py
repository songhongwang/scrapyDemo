# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import json
import os
reload(sys)
sys.setdefaultencoding("utf-8")

class DoubanPipeline(object):
    
    def __init__(self):
        self.file = open("spiders/list_json.txt", "w")
        '''开始中括号'''
        self.file.write("[")

    def process_item(self, item, spider):

        #print("item ==== %s"%(item['name']))
        itemJson = json.dumps(dict(item), ensure_ascii = False)
        self.file.write(itemJson + ",")
        return item


    def close_spider(self, spider):
        '''结束中括号'''
        self.file.seek(0, 2)
        self.file.write("]")

        self.file.close()
