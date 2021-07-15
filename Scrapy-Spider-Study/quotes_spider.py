# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/7/12 下午4:50

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_url = ['http://quotes.toscrape.com/tag/humor/',
                 ]

    def  parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath('span/small/text()').get(),
                "text": quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
