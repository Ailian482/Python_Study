import scrapy
from ..items import TxmoviesItem

class TxmsSpider(scrapy.Spider):
    name = 'txms'
    allowed_domains = ['v.qq.com']
    start_urls = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset={}&pagesize=30'
    offset = 0

    def start_requests(self):
        """改写 Spider 类的 start_requests 方法"""
        for i in range(0, 121, 30):
            url = self.start_urls.format(i)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        items = TxmoviesItem()
        movie_lists = response.xpath('//div[@class="list_item"]')
        for movie in movie_lists:
            items["name"] = movie.xpath('./a/@title').get()  # 获取电影的名字
            items["desc"] = movie.xpath('./div/div/@title').get()  # 获取电影的简介，获取字符串里的第一个数据

            yield items

        # 获取跟进链接
        # open_movie_url = response.xpath('//div[@class="list_item"]/a/attr(href)')

        # if self.offset < 120:
        #     self.offset += 30
        #     url = self.start_urls.format(str(self.offset))
        #
        #     yield scrapy.Request(url=url, callback=self.parse)