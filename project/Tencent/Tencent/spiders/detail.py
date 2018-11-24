# -*- coding: utf-8 -*-
import scrapy

"""
进入招聘页面，点击病获取详情页的内容
"""


class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath('//*[@class="tablelist"]//tr')[1:-1]

        for tr in tr_list:
            item = {}
            item['title'] = tr.xpath('.//a/text()').extract_first()

            # print("*" * 100)
            # 提取详情页的数据
            detail_url = 'https://hr.tencent.com/' + tr.xpath('.//a/@href').extract_first()

            # meta参数接受的十一个字典
            # request.meta=========>response.meta
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={"item": item})

        # 小不谨，则达是败矣,忘记洗而后面的大括号了
        next_href = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_href != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_href

            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        content = response.xpath('//*[@class="squareli"]/li/text()').extract()

        # 组装数据
        # 获取title,要求再上一级取title
        # 从response当中取出meta的参数
        item = response.meta['item']
        print(item['title'])
        item['content'] = content

        # 返回数据
        yield item
