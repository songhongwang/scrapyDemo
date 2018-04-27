# /usr/bin/env python
# -*- coding: utf-8 -*-

arr = ['五言绝句','七言绝句','五言律诗','七言律诗','五言古诗','七言古诗','乐府']

regex = "//div[@class='bookMl']//strong[.='@@']//../following-sibling::span//a/@href"


for item in arr:
    result = regex.replace("@@", item)
    print(result)
 