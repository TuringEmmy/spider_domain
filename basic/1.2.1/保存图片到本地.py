# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-12 下午12:05 GMT+8

# 保存baidu首页的图片到本地
import requests

# url
url = 'https://www.baidu.com/img/bd_logo1.png?where=super'

# 发送请求获取响应
resp = requests.get(url)

# print(resp.text)
# print('=')
# print(resp.content)
# 保存

# 以什么方式打开文件? wb
# 以什么方式写入文件? bytes
with open('baidu.png', 'wb') as f:
    f.write(resp.content)

