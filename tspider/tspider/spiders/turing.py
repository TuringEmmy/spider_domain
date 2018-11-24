# -*- coding: utf-8 -*-
import scrapy


class TuringSpider(scrapy.Spider):
    # 爬虫名
    name = 'turing'
    # 爬去范围域名，可以是多个
    allowed_domains = ['itcast.cn']
    # 可以是多个，元组或者列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):

        print("*"*100)
        print("*"*100)
        # 响应的内容 bytes
        print(response.url)
        print("*"*100)
        print(response.request.url)
        print("*"*100)
        print(response.headers)
        print("*"*100)
        print(response.request.headers)
        print("*"*100)
        print(response.status)
        print("*"*100)
        print("*"*100)

    def parse_demo(self, response):
        # print(response.body.decode())
        li_list = response.xpath('//div[@class="tea_con"]/div/ul/li')
        print(len(li_list))
        for li in li_list:
            # 提取name
            # name=li.xpath(".//h3")      # 返回的是iselecter的对象

            # print("*" * 100)
            # 返回list里面所有的字符串
            # name = li.xpath(".//h3/text()").extract()
            # print(name)
            name = li.xpath(".//h3/text()").extract_first()

            # 组装数据
            item = {}
            item['name'] = name

            # 如果使用管道就必须yield  每一条数据  日志中会显示item

            # 传递的对象只有四中东西，BaseItem,Resuest,dict,None
            yield item
