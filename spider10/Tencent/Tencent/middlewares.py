# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from Tencent.settings import USER_AGENTS_LIST


class User_Agent():
    # 随机的替换User-Agent
    def process_request(self, request, spider):
        if spider.name == 'tencent':
            # 随机获取一个ua
            UserAgent = random.choice(USER_AGENTS_LIST)
            # 给request对象替换UA
            request.headers['User-Agent'] = UserAgent

            # 不需要返回哦


# 检查UA是否奇效
class check_UA():
    # 检查UA设置是发成功
    def process_response(self, request, response, spider):
        if spider.name == 'tencent':
            # print(responses.request.headers['User-Agent'])
            print("*" * 100)
            print(request.headers['User-Agent'])
            print("*" * 100)

            # 必须要返回
            return response
