from ..items import DemoItem
import scrapy
import os


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['scrapy-chs.readthedocs.io']
    # 初始 url
    # start_urls = ['https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html#id2',
    #               "https://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/commands.html#id1"]
    # start_urls = ['https://api.bilibili.com/x/web-interface/cdn/report?from=report']
    start_urls = ['https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html#id2']

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'  # 定义文件名
        # with open("/Users/developer/Documents/Python_Study/my_scrapy/my_scrapy/spiders/" + filename, 'wb') as f:
            # f.write(response.body)  # 将响应数据保存到文

        # print(response.json())

        # 通过查看网页的源代码，发现网站的信息是被包含在 <ul> 元素中。
        # 我们可以通过下面这段代码选择该页面中网站列表里面所有 <li> 元素
        for sel in response.xpath('//ul/li'):  # 获取网站列表里面所有的 <li> 元素
            item = DemoItem()
            item['title'] = sel.xpath('a/text()').extract()  # 获取网站的 标题，返回的是 list
            item['link'] = sel.xpath('a/@href').extract()  # 获取网站的 链接，返回的是 list
            item['desc'] = sel.xpath('text()').extract()  # 获取网站的 描述，返回的是 list
            yield item

