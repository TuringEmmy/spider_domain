# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-12 上午11:13 GMT+8


# 获取百度首页的html保存到本地
import requests

# url
url = 'https://www.baidu.com/'

# 发送请求获取响应
response = requests.get(url)

# 对响应进行处理:保存到本地
# print(response)
#
# # 获取响应的文本内容
# print(response.text) # str
# print(response.content) # bytes

# print(response.content.decode())
#
# with open('baidu.html', 'w') as f:
#     f.write(response.content.decode())


# 响应的url
print(response.url) # 会有响应的url和请求的url不一致的情况

# 响应的状态码
print(response.status_code) # int

# 响应的头信息
print(response.headers) # dict

# 响应的请求的头信息
print(response.request.headers) # dict

# 响应的cookie
print(response.cookies) # CookieJar对象

# 响应的请求的cookie
print(response.request._cookies) # CookieJar对象