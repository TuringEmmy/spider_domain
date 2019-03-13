# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class MedinceSpider(scrapy.Spider):
    name = 'medince'
    # allowed_domains = ['me.com']
    start_urls = ['https://www.yaozui.com/yaopin']

    def parse(self, response):
        div_list=response.xpath(r'/html/body/div[3]/div/div/div')
        #
        item={}
        for div in div_list:
            dd_llist = div.xpath(r'dl/dd')
            for dd in dd_llist:
                item['大分类'] = dd.xpath(r'./a/text()').extract_first()
                next_url = dd.xpath(r'./a/@href').extract_first()
                # print(next_url)
                # yield item
                yield scrapy.Request(
                    next_url,
                    callback=self.parse_medince_list,
                    meta={"item": deepcopy(item)}
                )


    def parse_medince_list(self,response):
        item = response.meta["item"]
        div_list = response.xpath(r'/html/body/div[3]/div/div/div[2]/div')[1:-1]
        for div in div_list:
            item['药品名称'] = div.xpath(r'./div/h5/a/text()').extract_first()
            next_url = div.xpath(r'./div/h5/a/@href').extract_first()
            # print(next_url)
            # yield item
            yield scrapy.Request(
                next_url,
                callback=self.parse_medince_detaill,
                meta={"item": deepcopy(item)}
            )
        next_href = response.xpath('/html/body/div[3]/div/div/div[2]/div[17]/nav/ul/li')
        if next_href.xpath(r'./a/@text()') != '...':
            next_url = next_href.xpath(r'./a/@href').extract_first()

            yield scrapy.Request(next_url, callback=self.parse_medince_list)


    def parse_medince_detaill(self,response):
        item = response.meta["item"]
        item['用法用量'] = response.xpath(r'//*[@id="tab-shuomingshu"]/p[1]').extract_first()
        item['不良反应'] = response.xpath(r'//*[@id="tab-shuomingshu"]/p[2]').extract_first()

        item['注意事项'] = response.xpath(r'//*[@id="tab-shuomingshu"]/p[3]/text()').extract_first()
        item['主要成分'] = response.xpath(r'/html/body/div[3]/div/div/div[1]/div[3]/text()').extract_first()
        yield item