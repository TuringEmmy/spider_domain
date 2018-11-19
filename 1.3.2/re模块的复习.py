# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.6
# author    TuringEmmy
# time      18-11-14 下午4:55
# project   reptile

import re

string_= '<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t\t<meta http-equiv="content-type" content="text/html;charset=utf-8">\n\t\t<meta content="always" name="referrer">\n        <meta name="theme-color" content="#2932e1">'

ret = re.match('<meta http-equiv="X-UA-Compatible"',string_).group()
print(ret)

ret = re.match('X-UA-Compatible',string_)
print(ret)

ret = re.search('"(.*?)"', string_).group()
print(ret)
# 上面的只能插叙第一个，因为首先使用了非贪婪，而且查询到的结果只有第一个

# 查询所有
ret = re.findall('"(.*?)"',string_)
print(ret)


p = re.compile('"(.*?)"')
ret = p.findall(string_)
print(ret)

# 替换
ret = re.sub('"(.*?)"','雍珑庚',string_)
print(ret)


title = u'您好，北京，welcome,china'
pattern = re.compile('[\u4e00-\u9fa5]+')
result = pattern.findall(title)
print(result)