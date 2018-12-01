# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


class Proxies():
    def process_request(self, request, spider):
        # 该带来ip并不是直接写进代码的
        # 正常应该是从带来ip池当中取随机取出一个
        proxy = 'http://183.129.207.73:14823'
        request.meta['proxy'] = proxy
