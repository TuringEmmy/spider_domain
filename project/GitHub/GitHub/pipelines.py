# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from pymongo import MongoClient


class GithubPipeline1(object):
    """
    写入文件
    """

    def open_spider(self, spider):
        # 爬虫只执行一次
        self.f = open('name.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(json.dumps(item, ensure_ascii=False, indent=2) + '\n')
        # 必须return item , 为了其他后执行的管道能够收到item数据!
        return item

    def close_spider(self, spider):
        self.f.close()


class GithubPipeline2(object):
    """mongodb的存储"""

    def open_spider(self, spider):
        client = MongoClient()
        self.col = client.turing.name

    def process_item(self, item, spider):
        self.col.insert(item)
        return item
