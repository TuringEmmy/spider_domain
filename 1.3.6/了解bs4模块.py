# this virtualenv is used for spider 
# author    python
# time      18-11-16 上午9:15
# project   reptile

from bs4 import BeautifulSoup
import re

html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 实例化soup对象
soup = BeautifulSoup(html_str, 'lxml')
print(soup.prettify())

# =============================find_all函数================================
# name参数
print('*' * 50)
# 字符串
ret = soup.find_all('a')
print(ret)

print('*' * 50)
# 正则表达式
rets = soup.find_all(re.compile('^b'))
for ret in rets:
    # ret是标签，打印的是标签的名字
    print(ret.name)

print('*' * 50)
# 传入列表
rets = soup.find_all(['b', 'body'])
print(rets)

print('*' * 50)
# 根据属性定位
print(soup.find_all(class_="sister"))

# find函数是找一个
print('-' * 50)
print('通过css, 使用select函数')
print('-' * 50)
print(soup.select('a'))

print('+' * 50)
print('通过类link3来查询找')
print(soup.select('#link3'))

print('+' * 30)
print('通过编号title进行查找')
print(soup.select('.title'))

print('+' * 30)
print('层级选择器')
print(soup.select('p #link1'))

print('+' * 30)

print('根据属性值定位')
print(soup.select('a[class="sister"]'))

print('\n')
print('-' * 60)
print('提取数据的方法')
print('-' * 60)
print(soup.select('a[class="sister"]')[0].get_text())
# 上面的代码是对的，因为第一个里面的注释的了
for a in soup.select('a[class="sister"]'):
    print(a)

    print('\n')
    print('+' * 30)
    print('提取文本')
    print(a.get_text())

    print('\n')
    print('+' * 30)
    print('提取属性')

    print(a.get('href'))
