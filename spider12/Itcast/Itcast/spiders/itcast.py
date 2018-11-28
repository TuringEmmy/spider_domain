# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy_redis.spiders import RedisSpider

"""
启动scrapy_splash
sudo docker run -p 8050:8050 scrapyinghub/splash
redsi中输入其实的url
lpush turing 'http://www.itcast.cn/channel/teacher.shtml'
"""


class ItcastSpider(RedisSpider):
    """
    scrapy_redsi和scrapy_spalsh混合时使用
    """
    name = 'itcast'
    allowed_domains = ['www.itcast.cn']
    # start_urls = ['http://itcast.cn/']


    redis_key = 'turing'

    """
    注意重写start_url方法起始的url会从redis的数据库当中去寻找
    """

    def parse(self, response):
        url = 'http://www.itcast.cn/channel/teacher.shtml'
        yield SplashRequest(url,
                            callback=self.parse_item,
                            dont_filter=True,
                            args={'wait': 3},  # 最大超时时间，单位：秒
                            endpoint='render.html')  # 使用splash服务的固定参数

    def parse_item(self, response):
        with open("demo.html", 'w') as f:
            f.write(response.body.deconde())

        # 先分组
        li_list = response.xpath('//div[@class="tea_con"]/div//li')
        for li in li_list:
            # 组装数据
            item = {}
            item['name'] = li.xpath('.//h3/text()').extract_first()  # 返回第一个字符串
            yield item

"""""

注意：本机没有装docker的splash服务
"""