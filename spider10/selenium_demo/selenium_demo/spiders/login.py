# -*- coding: utf-8 -*-
import scrapy


class LogoinSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/TuringEmmy']

    def parse(self, response):
        with open('check.html','w') as f:
            f.write(response.body.decode())
