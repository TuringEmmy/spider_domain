# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-14 上午11:40 GMT+8

"""
帖子的标题，连接和帖子中图片的链接

# 先确定最终数据的结构
{
    title
    url
    img: [
        img_url_1,
        img_url_2,
        ...
    ]
}

# 确定url
http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={贴吧名字}&lp=5011&lm=&pn={页码数} #
pn = 0 第一页
pn = 20 第二页
pn = 40 第三页

# 确定流程
# 1. 确定贴吧名字,组装该贴吧的start_url
# 2. 对列表页 发送请求获取响应
# 3. 获取所有帖子的名字和链接
    # img_list = []
    # a. 对详情页 发送请求获取响应
    # b. 提取详情页中所有图片的链接
        # 把获取的图片链接添加到img_list中
    # c. 获取详情页的下一页的链接
    # d. 重复a步骤,直到最后一页
    # 组装完整数据,并处理或保存
# 4. 获取列表页下一页的链接,重复步骤2
"""

import requests
from lxml import etree


class TiebaSpider():
    def __init__(self, spider_name):
        # 1. 确定贴吧名字,组装该贴吧的start_url
        self.start_url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}&lp=5011&lm=&pn=0'.format(spider_name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }

    def _get_html(self, url):
        """发送请求获取响应,返回可以xpath的页面对象"""
        resp = requests.get(url, headers=self.headers)
        return etree.HTML(resp.content)

    def _get_img_list(self, detail_url, img_list=[]):
        """获取一个帖子的全部图片链接"""
        # a. 对详情页 发送请求获取响应
        detail_html = self._get_html(detail_url)
        # b. 提取详情页中所有图片的链接
        # 把获取的图片链接添加到img_list中
        img_list += detail_html.xpath('//img[@class="BDE_Image"]/@src')
        # c. 获取详情页的下一页的链接
        detail_next_href = detail_html.xpath('//a[text()="下一页"]/@href')
        if detail_next_href != []:
            detail_next_url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/' + \
                              detail_next_href[0]  # 拼接详情页下一页的url
        # # d. 重复a步骤,直到最后一页
            """其实就是回调自己"""
            self._get_img_list(detail_next_url, img_list)
        return img_list


    def _get_list(self, html):
        """获取当前列表页所有帖子的名字和链接"""
        div_list = html.xpath('/html/body/div[1]/div')[1:21]  # 取第二个到第21个
        return div_list

    def _get_item(self, div):
        """获取一个帖子的全部数据"""
        item = {}
        item['title'] = div.xpath('./a/text()')[0]  # 贴子名字
        item['detail_url'] = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/' + \
                             div.xpath('./a/@href')[0]  # 帖子的链接
        item['img_list'] = self._get_img_list(item['detail_url'])
        return item

    def _excute_item(self, item):
        """处理或保存数据"""
        print(item)

    def _excute_list_page_and_return_next_url(self, list_url):
        """完整的处理完一个列表页!并返回一下页的url,没有没有就返回None"""
        # 2. 对列表页 发送请求获取响应
        html = self._get_html(list_url)
        # 3. 获取所有帖子的名字和链接
        div_list = self._get_list(html)
        # print(len(div_list))
        for div in div_list:
            # 4.获取数据 组装完整数据,并处理或保存
            item = self._get_item(div)
            # 5. 处理或保存数据
            self._excute_item(item)

        # 6. 获取列表页下一页的链接,重复步骤2
        next_list_href = html.xpath('//a[text()="下一页"]/@href')
        if next_list_href != []:
            next_list_url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/' + next_list_href[0]
            return next_list_url

        else:
            return None


    def _main(self, page):
        """贴吧爬虫运行的逻辑流程"""
        next_list_url = self.start_url

        i = 0
        while i<page:
            """不断处理每一页的列表页,并返回列表页的下一页的url"""
            next_list_url = self._excute_list_page_and_return_next_url(next_list_url)
            if next_list_url is None:
                break

            if page == 0:  # 要爬取全网站的数据
                i -= 1
            else: # 爬取指定页数的数据
                i += 1

    def run(self, page=0):
        """对外调用的接口"""
        self._main(page)



if __name__ == '__main__':

    spider = TiebaSpider('lol')
    spider.run(page=2)
