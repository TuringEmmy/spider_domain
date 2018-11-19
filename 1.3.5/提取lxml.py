# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.6
# author    TuringEmmy
# time      18-11-14 上午11:01
# project   reptile
from lxml import etree


html_str = """<div> <ul> 
<li class="item-1"><a href="link1.html"></a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a> 
</ul> </div>"""

# 将html字符串转化为可以xpathde element对象
html = etree.HTML(html_str)

ret = html.xpath('//a/@href')
print(ret)

# lxml.etree.HTML()能够修改被转化的HTML_str
# 爬虫提取数据应该以stree.tostring()转化回来的html_str为准进行提取
new_html_str = etree.tostring(html).decode()
print(new_html_str)

print("*"*100)
# 把a标签的href和文本内荣作为一条数据进行提取

# 思路：先分组，再提取组装数据

# 返回的是element对象构成的List
li_list = html.xpath('//li')
print(li_list)
for li in li_list:
    item = {}

    text=li.xpath('./a/text()')[0] if li.xpath('./a/text()') != [] else ''

    href = li.xpath('./a/@href')[0] if li.xpath('./a/@href') != [] else ''

    item['text']  = text
    item['href'] = href

    print(item)

