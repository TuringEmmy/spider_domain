# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TitleSpider(CrawlSpider):
    name = 'title'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 列表页的
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'),
             follow=True),
        # 详情页的
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = {}
        item['title'] = response.xpath('//td[@id="sharetitle"]/text()').extract_first()
        item['content'] = response.xpath('//ul[@class="squareli"]/li/text()').extract()
        # from pymongo import MongoClient
        # client =MongoClient()
        # col = client.turing.tencent
        # col.insert(item)
        return item

        import csv
        # f = open('dict.csv', 'wb')
        # w = csv.DictWriter(f, mydict.keys())
        # w.writerow(mydict)
        # f.close()






    """
    # Rule是规则对象,LinkExtractor是必要参数!
        # LinkExtractor链接提取器:按照参数规则来提取url,自动构造request;框架会自动发送获取响应
            # 链接提取器中的参数规则:
                # allow:正则匹配a标签中href属性的值
                # deny:会排除正则匹配a标签中href属性的值
                # allow_domains:接收list,按其中的域名提取url
                # deny_domains:接收list,排除其中的域名的url
                # restrict_xpaths:xpath定位标签范围内的url会被提取
                    # restrict_xpaths='//div[@class="pagenav"]'
                # 最终会提取以上所有参数共同作用之后的url
        # callback:链接提取器提取的url对应的响应会进入callback指定的解析函数进行处理
        # follow=True:链接提取器提取的url对应的响应还会进入rules被各个Rule规则进行处理
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/')),
            # 按照参数规则来提取url,自动构造request;框架会自动发送获取响应
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item'),
            # 按照参数规则来提取url,自动构造request;框架会自动发送获取响应
            # 链接提取器提取的url对应的响应会进入callback指定的解析函数进行处理
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
            # 按照参数规则来提取url,自动构造request;框架会自动发送获取响应
            # 链接提取器提取的url对应的响应会进入callback指定的解析函数进行处理
            # 链接提取器提取的url对应的响应还会进入rules规则集合中被各个Rule规则对象进行处理
        #以上是说明,下边是代码中的具体规则

        # 提取列表页的url并处理
        
    """


