# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.6
# author    TuringEmmy
# time      18-11-14 下午5:26
# project   reptile

"""
帖子的标题，链接和帖子中图片的链接
"""
# 1. 确定贴吧名字，组装该贴的start_url
# 2. 队列表页，发送请求获取响应
# 3. 获取所有帖子的名字和链接
#     a. 对详情页 发送请求获取相应
#     b. 提取详情页面中所有的图片的链接
#     c. 获取详情页面的下一页的链接
#     d.重复a步骤，直到最后一页
# 4. 获取列表页下一页的链接，重复步骤2

import requests
from lxml import etree


# {
#     title
#     url
#     img:{
#         img_url_1,
#         img_url_2,
#         ...
#     }
# }

class TiebaSpider():
    def __init__(self, spider_name):
        self.start_url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}&lp=5011&lm=&pn=0'.format(
            spider_name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def get_html(self, url):
        """发送请求获取响应"""
        resp = requests.get(url, headers=self.headers)
        return etree.HTML(resp.content)

    def get_image_list(self, detail_url, img_list=[]):

        detail_html = self.get_html(detail_url)

        img_list += detail_html.xpath('//img[@class="BDE_Image"]/@src')

        # 获取下一页的链接
        detail_next_href = detail_html.xpath('//a[text()="下一页"]/@href')

        if detail_next_href != []:
            detail_next_url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/' + detail_next_href[0]  # 拼接详情页链接

            # 回调自己
            self.get_image_list(detail_next_url, img_list)

        return img_list

    def get_item(self, detail_html):
        """获取所有帖子的名字和链接"""
        div_list = detail_html.xpath('/html/body/div[1]/div')[1:21]  # 取第2个到地21个,,下表21代表地22 个
        print(len(div_list))
        for div in div_list:
            # 获取一个帖子的全部数据
            item = {}

            item['title'] = div.xpath('./a/text()')[0]  # 帖子的名称
            item['detail_url'] = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/' + div.xpath('./a/@href')[
                0]  # 帖子的链接
            item['image_list'] = self.get_image_list(item['detail_url'])

            print(item)

            # 组装数据

    def excute_item(self,item):
        """处理保存的数据"""

    def _main(self):
        html = self.get_html(self.start_url)
        self.get_item(html)

        next_list_href=html.xpath('//a[text()=""')


    def run(self):
        self._main()


if __name__ == '__main__':
    spider = TiebaSpider('美女')

    spider.run()
