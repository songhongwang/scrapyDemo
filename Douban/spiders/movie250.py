import scrapy
from Douban.items import DoubanItem

import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

class Movie250Spider(scrapy.Spider):
  """docstring for Movie250Spider"""
  name = 'movie250'
  allowed_domains = ["douban.com"]
  start_urls = [
    "http://movie.douban.com/top250/"
  ]
  page = 0 # current spide page
  MAX_PAGE = 10 # max page

  def sumChildStr(self, child_list):
    all = ""
    for rate in child_list:
        all += str(rate).encode("utf8")
    return all

  def parse(self, response):
    for info in response.xpath('//div[@class="item"]'):
      item = DoubanItem()
      item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()[0].strip().encode("utf8").replace("\'","")
      item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()[0].strip().encode("utf8").replace("\'","")
      item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()[0].strip().encode("utf8").replace("\'","")
      item['star'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[1]/text()').extract()[0].strip().encode("utf8").replace("\'","")
      list_quote = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
      item['quote'] = self.sumChildStr(list_quote).replace("\'","")
      list_rate = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
      item['rate'] = self.sumChildStr(list_rate).replace("\'","")
 
      yield item

    
    next_page = response.xpath('//span[@class="next"]/a/@href')
    if next_page and self.page < self.MAX_PAGE:
      url = response.urljoin(next_page[0].extract())
      self.page += 1
      yield scrapy.Request(url, self.parse)
 