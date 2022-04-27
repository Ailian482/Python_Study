# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/12/24 下午12:57
# 使用终端运行太麻烦，而且不能提取数据，可以写一个run.py文件，作为程序的入口，split 是必须写，目的是将字符串转换为列表形式，第一个参数是 scrapy，第二个参数是 crawl，第三个是 demo
from scrapy import cmdline
import os
# from my_scrapy.spiders.baidu_spider import DemoSpider


spider_name = 'douban'  # 爬虫名称
res_filename = os.path.dirname("/Users/developer/Documents/Python_Study/my_scrapy/my_scrapy/spiders/" + spider_name + "_spider.py") + '/' + spider_name
# print(res_filename)
# cmdline.execute(('scrapy crawl -o %s.json %s' % (res_filename, spider_name)).split())
cmdline.execute(('scrapy crawl -o %s.jl %s' % (res_filename, spider_name)).split())

# cmdline.execute(('scrapy crawl -o a.json %s' % spider_name).split())

# import sys
# sys.path.append('/Users/developer/Documents/Python_Study/my_scrapy/my_scrapy')
# print(sys.path)
# import items
#
# items = items.DemoItem()
# items["title"] = '小白猪'
#
# print(items)
#
#
# import scrapy
# print(scrapy.__all__)
# print(scrapy.__file__)