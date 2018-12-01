# -*- coding: utf-8 -*-
import scrapy

# 从哪里执行几从哪里导入
from Tencent.items import TencentItem


class BaseItemUseSpider(scrapy.Spider):
    name = 'baseItemUse'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath('//*[@class="tablelist"]//tr')[1:-1]

        for tr in tr_list:
            item = {}
            item['title'] = tr.xpath('.//a/text()').extract_first()

            detail_url = 'https://hr.tencent.com/' + tr.xpath('.//a/@href').extract_first()

            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={"item": item})

        next_href = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_href != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_href

            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        item =TencentItem()

        content = response.xpath('//*[@class="squareli"]/li/text()').extract()

        xx = response.meta['item']
        item['title']=xx['title']
        print(item['title'])
        item['content'] = content

        yield item
