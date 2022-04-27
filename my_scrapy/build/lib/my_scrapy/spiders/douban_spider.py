import scrapy
import json
from ..items import DoubanItem

class DoubaiSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0']

    def parse(self, response):
        """获取想要的数据"""
        # 获取热门电影 的
        movies = response.xpath('//p/text()').extract_first()
        # print(type(movies))
        # print(json.loads(movies))
        movies_list = json.loads(movies)['subjects']
        # print(movies_list)
        for movie in movies_list:
            item = DoubanItem()
            item['movie_name'] = movie['title']
            item['movie_url'] = movie['url']
            item['movie_rate'] = movie['rate']

            yield item