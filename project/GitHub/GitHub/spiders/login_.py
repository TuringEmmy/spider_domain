# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login_'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)

    def parse(self, response):
        # 1. 对登录页进行解析,然后提取authenticity_token, 并春送到下一个解析函数当中去
        authenticity_token = response.xpath('//*[@name="authenticity_token"]/@value').extract_first()
        print(authenticity_token)

        # 构造post登录请求的data
        data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': authenticity_token,
            'login': 'TuringEmmy',
            'password': '258467Ylg2018'
        }
        # 2. 发送post请求,进行登录
        url = 'https://github.com/session'
        # yield scrapy.Request(url, method='POST', body=data, callback=self.check)
        yield scrapy.FormRequest(url, formdata=data, callback=self.check)

    def check(self, response):
        url = 'https://github.com/TuringEmmy'
        yield scrapy.Request(url, callback=self.save)

    def save(self, response):
        with open("code_login_by_it_self.html", 'w') as f:
            f.write(response.body.decode())

# 不光能够自带cookie,还能自己重定向
