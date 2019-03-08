# -*- coding: utf-8 -*-
import csv
from copy import deepcopy

import scrapy


class MedinceSpider(scrapy.Spider):
    name = 'medince'
    # allowed_domains = ['familydoctor.com']
    start_urls = ['https://ypk.familydoctor.com.cn/efficacys.html']

    def parse(self, response):
        li_list = response.xpath("//div[@class='seek-list']//ul/li")[0:-10]
        for li in li_list:
            item = {}
            item["b_cate"] = li.xpath("./h3/a/text()").extract_first()
            span_list = li.xpath("./div[@class='seek-cont clearfix']/span")
            for span in span_list:
                item["s_cate"] = span.xpath("./a/text()").extract_first()
                next_url = span.xpath("./a/@href").extract_first()
                print(next_url)
                # yield item
                yield scrapy.Request(
                    next_url,
                    callback=self.parse_medince_list,
                    meta={"item": deepcopy(item)}
                )
        # print(item)

    def parse_medince_list(self, response):
        item = response.meta["item"]
        # 药品列表页分组
        li_list = response.xpath("//div[@id='tabContent9_0']/ul/li")

        for li in li_list:
            item["medince_pic"] = li.xpath("./div[@class='pic']/a/@href").extract_first()
            item["medince_name"] = li.xpath("./div[@class='text']/h3/a/text()").extract_first()
            item['medince_detail_url'] = li.xpath("./div[@class='text']/h3/a/@href").extract_first()
            # print(medince_detail_url)
            yield scrapy.Request(
                item['medince_detail_url'],
                callback=self.parse_medince_detail,
                meta={"item": deepcopy(item)}
            )

        next_href = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_href != 'javascript:;':
            next_url = next_href

            yield scrapy.Request(next_url, callback=self.parse)


    def parse_medince_detail(self, response):
        item = response.meta["item"]
        div_info = response.xpath("//*[@class='table-1']")
        item["medince_enterprise"] = div_info.xpath("./tr[2]/td/a[1]/text()").extract_first()
        #
        # item["medince_enterprise"] = div_info.xpath("//tr[3]/td/a/text()").extract()
        item["medince_effect"] = div_info.xpath("./tr[3]/td/text()").extract()
        item["medince_consumption"] = div_info.xpath("./tr[4]/td/text()").extract()
        item["medince_component"] = div_info.xpath("./tr[5]/td/text()").extract()
        item["medince_character"] = div_info.xpath("./tr[6]/td/text()").extract()
        #
        # with open('medince.csv','a+') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(['大分类'],['小分类'],['图片'],['药品名称'],['详情页连接'],['生产企业'],['功效主治'],['用法用量'],['化学成分'],['性 状'])
        #
        #     for i in item:
        #         writer.writerow(i)

        # with open("medicine.txt",'a+') as f:
        #     f.write(item)

        yield item
