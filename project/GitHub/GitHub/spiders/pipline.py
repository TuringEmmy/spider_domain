# -*- coding: utf-8 -*-
import scrapy


class PiplineSpider(scrapy.Spider):
    name = 'pipline'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath('//table[@class="tablelist"]//tr')[1:-1]
        # print(len(tr_list))

        for tr in tr_list:
            item = {}
            item['title'] = tr.xpath('.//a/text()').extract_first()
            # print(item['title'])
            yield item

        # 翻页
        # 下一页的url
        next_href = response.xpath('//a[text()="下一页"]/@href').extract_first()

        if next_href != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_href
            # 构造并返回下一页有的url的request
            yield scrapy.Request(next_url, callback=self.parse)
