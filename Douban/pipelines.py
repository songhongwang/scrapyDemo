# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys, os, json
from Douban.test import Test

reload(sys)
sys.setdefaultencoding("utf-8")
base_dir = sys.path[0]

class DoubanPipeline(object):
    
    def __init__(self):
        test = Test()
        file_path =  os.path.split(os.path.realpath(__file__))[0] + "/spiders/list_json.txt"
        self.file = open(file_path, "w")
        '''开始中括号'''
        self.file.write("[" + "\n")

    def process_item(self, item, spider):

        #print("item ==== %s"%(item['name']))
        itemJson = json.dumps(dict(item), ensure_ascii = False)
        self.file.write(itemJson + "," + "\n")
        return item


    def close_spider(self, spider):
        '''结束中括号'''
        self.file.seek(-2, 2)
        self.file.write("\n" + "]")

        self.file.close()
