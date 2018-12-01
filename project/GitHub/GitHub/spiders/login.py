# -*- coding: utf-8 -*-
import scrapy

'''
cookie参数的用法
'''


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/TuringEmmy']

    # 登陆之后才能访问，所以需要重写start_request函数, 构造对起始cookies参数
    def start_requests(self):
        cookies_str = '_octo=GH1.1.596230318.1536420006; _ga=GA1.2.448860518.1536421122; tz=Asia%2FShanghai; has_recent_activity=1; logged_in=no; _gh_sess=ZDJZQjlBbUdUeFhpS05sWlpNQ1FFSnRhTXZUT0hmWFY0VkJwQ2VNRks0NzM1SEF4MVRDUmhvdEY2MXQxaVBBU2lyY0ZSbTFlcWtVR3NWUWxqY3BLZlE0TmFqOFFKRjN4UXkzQ0VZM0hhOG5DZk1DdlBWQ3F6MXZjQWFoUVo0TjY0S092aVFvZzIvSThHSGw5RHlENEJwRGFKSzB5bDc5K21IZHdCUUNLRGNIQzVWSzErUEZrVXA1VXl4T251d0k4aytrVGJzZHZkY3dvT084RmJZY05vT3NCRUZvejc2YnU3Slp5T0wrOEpCdk1BQzdVRnNhOHRGRDI1N2FOSzRmaTNyQ0RGVURYbnBGTzJOQ1BNanJXWlRzdWtIZElLdWVUcks4MjJMVkRCUTJYcU54cVJJK0syWUp0N3lNUHRneEYrNWJzcHYramhkblRmVHM3eUhnajZCL3I2MTIzdWFZdG5OU0FkaW1EaWhOWjVwL2FVTCtualp6SEdETlZDQURvSWdBSDg1eGFDWENkNlcrOVpPTTZZaEk2R0Q0TWtjSjVTcmYzdUdlMk1pcGVHQk4vcHdqZml0MEZyTFFnMHd1ekYzZVFBNVczVEdReHBDUVJMNWZNZjlHZHNsQmVJZnhCblpkNkoyOG1RQWk3QU5jTXAwdE1BODJ6VHRBOC84V3R5d1J5WFVwWkpNeTNVbzRZenJBOWZyWWh4ejJEaEJyL3VOa3REWE5qZHlqYWVyNGtjcW1CNTFUL2tIbHV4V3dnU0dTOENRUkIrQm5zWnU3b1A5L3pWYnF2bHZscE0yZFptWnM3L3Z6MXdzOG9Wcm9rMkFWQ3JDVVBhTUJMKzZQWTdxWE9VcXFRZGx4ZDdHcVBKSVV0ZUE9PS0tdHBmeGo0UFNjSE1mcjJteVVZcnVJdz09--3bd3c57f3d675e86b76cb38ae6557465d808e9e2'

        # 转换为cookies_dict
        cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies_str.split('; ')}

        # 构造起始的request对象
        yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies=cookies_dict)

    def parse(self, response):
        # 检测是否成功，获取登录后才能访问的页面
        print(response.body.decode())
        with open('login.html', 'w') as f:
            f.write(response.body.decode())
