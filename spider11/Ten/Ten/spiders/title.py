# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TitleSpider(CrawlSpider):
    name = 'title'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (

        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'),
             follow=True),

        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = {}
        item['title'] = response.xpath('//td[@id="sharetitle"]/text()').extract_first()
        item['content'] = response.xpath('//ul[@class="squareli"]/li/text()').extract()
        return item


