# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver


def getCookies():
    # 获取账号 密码

    user = input('账号输入:')
    pwd = input('密码输入:')

    # 实例化无界面模式的driver
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')

    driver = webdriver.Chrome('/home/worker/Desktop/spider_study/data/driver/chromedriver', chrome_options=option)

    # 模拟登录
    driver.get('https://github.com/login')

    driver.find_element_by_id('login_field').send_keys(user)
    driver.find_element_by_id('password').send_keys(pwd)

    driver.find_element_by_name('commit').click()

    # 获取并返回cookies
    cookies_list = driver.get_cookies()

    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies_list}

    driver.quit()
    return cookies_dict


class LoginMid():
    def process_request(self, request, spider):
        # 给request.cookies一个登录的cookie
        request.cookies = getCookies()
