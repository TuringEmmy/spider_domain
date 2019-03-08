# -*- coding: utf-8 -*-
import json

import scrapy


class MedinceOtherSpider(scrapy.Spider):
    name = 'medince_other'
    # allowed_domains = ['medince.com']
    start_urls = ['https://ypk.familydoctor.com.cn/58543/instructions/']

    def parse(self, response):
        detail = response.xpath("//div/table[@class='table-1']")
        for i in range(58543, 248435):

            item = {}
            item["药品名称"] = detail.xpath("//tr[1]/td/text()").extract()
            item["生产企业"] = detail.xpath("//tr[2]/td/a/text()").extract()
            item["适应症"] = detail.xpath("//tr[3]/td/text()").extract()
            item["用法用量"] = detail.xpath("//tr[4]/td/text()").extract()
            item["成分"] = detail.xpath("//tr[5]/td/text()").extract()
            item["性状"] = detail.xpath("//tr[6]/td/text()").extract()
            item["药理作用"] = detail.xpath("//tr[7]/td/text()").extract()
            item["相互作用"] = detail.xpath("//tr[8]/td/text()").extract()
            item["不良反应"] = detail.xpath("//tr[9]/td/text()").extract()
            item["禁忌"] = detail.xpath("//tr[10]/td/text()").extract()
            item["注意事项"] = detail.xpath("//tr[11]/td/text()").extract()

            for i in range(58543, 248435):
                url = 'https://ypk.familydoctor.com.cn/' + str(i) + '/instructions/'

                yield scrapy.Request(url, callback=self.parse)
        # file = open('medince.json', 'wb')
        #
        #
        # content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # content = content.encode()
        # self.file.write(content)
        # file.close()

            yield item
        # for i in range(58543, 248435):
        #     url = 'https://ypk.familydoctor.com.cn/' + str(i) + '/instructions/'
        #
        #     yield scrapy.Request(url, callback=self.parse)

