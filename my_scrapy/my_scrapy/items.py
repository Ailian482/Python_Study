# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # item 是保存爬取到的数据的容器；其使用方法和python字典类似。虽然可以直接在 Scrapy 中直接使用 dict，但是 Item 提供了额外保护机制来避免拼写错误导致的未定义字段错误
    # 首先根据需要从 网站中 获取到数据时对 Item 进行建模，我们需要从网站中获取 名字，url，以及网站的描述
    # 编辑 my_scrapy 项目目录下的 items.py 文件
    # 通过定义 item ，可以很方便的使用 Scrapy 的其他方法
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class TxmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # item 是保存爬取到的数据的容器；其使用方法和python字典类似。虽然可以直接在 Scrapy 中直接使用 dict，但是 Item 提供了额外保护机制来避免拼写错误导致的未定义字段错误
    # 首先根据需要从 网站中 获取到数据时对 Item 进行建模，我们需要从网站中获取 名字，url，以及网站的描述
    # 编辑 my_scrapy 项目目录下的 items.py 文件
    # 通过定义 item ，可以很方便的使用 Scrapy 的其他方法
    name = scrapy.Field()
    # link = scrapy.Field()
    desc = scrapy.Field()

class DoubanItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_url = scrapy.Field()
    movie_rate = scrapy.Field()