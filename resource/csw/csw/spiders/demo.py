# -*- coding: utf-8 -*-
import scrapy


class MedinceSpider(scrapy.Spider):
    name = 'medince1'
    # allowed_domains = ['me.com']
    start_urls = ['https://www.yaozui.com/yaopin/174-bingbofenzhusheye']

    def parse(self, response):
        item = {}
        item['用法用量']=response.xpath(r'//*[@id="tab-shuomingshu"]/p[1]').extract_first()
        item['不良反应'] = response.xpath(r'//*[@id="tab-shuomingshu"]/p[2]').extract_first()


        item['注意事项'] = response.xpath(r'//*[@id="tab-shuomingshu"]/p[3]/text()').extract_first()
        item['主要成分'] = response.xpath(r'/html/body/div[3]/div/div/div[1]/div[3]/text()').extract_first()

        yield item
        # # 小不谨，则达是败矣,忘记洗而后面的大括号了
        # next_href_list = response.xpath('/html/body/div[3]/div/div/div[2]/div[17]/nav/ul/li').extract_first()
        # for next_href in next_href_list:
        #     url = next_href.xpath(r'/a/@href').extract_first()
        # if next_href != 'javascript:;':
        #     next_url = 'https://hr.tencent.com/' + next_href
        #
        #     yield scrapy.Request(next_url, callback=self.parse)
        #
        # next_href = response.xpath('/html/body/div[3]/div/div/div[2]/div[17]/nav/ul/li')
        # if next_href.xpath(r'./a/@text()') != '...':
        #
        #     next_url = next_href.xpath(r'./a/@href').extract_first()
        #
        #     yield scrapy.Request(next_url, callback=self.parse)
