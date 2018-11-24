# life is short, i use python
# author    worker
# time      11/16/18 4:40 PM
# project   reptile
# name
# content

# url_list

# 遍历url_list
#  发送请求，获取参数
#  分组提取数据
#  保存数据
import requests

from lxml import etree


class QiushiSpider():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

    def get_url_list(self):
        # for i in range(1,14):
        #     url_list=[]
        #     url = 'https://www.qiushibaike.com/8hr/page/{}/'.format(i)
        #     url_list.append(url)
        # return url_list

        # return ['https://www.qiushibaike.com/8hr/page/{}/'.format(i) for i in range(1, 14)]
        return ['https://www.qiushibaike.com/8hr/page/1/']

    def get_html(self, url):
        """
        获取具体这一页的html
        :param url: 当前也的链接
        :return:
        """
        resp = requests.get(url, headers=self.headers)
        return etree.HTML(resp.text)

    def get_item(self, html):

        with open('qiushi.html','w') as f:
            f.write(etree.tostring(html).decode())

        # div_list = html.xpath('//div[@id="content-left"]')
        div_list = html.xpath('//div[@class="article block untagged mb15 typs_recent"]')
        # 进行分组提取数据
        print(len(div_list))

        result_list = []
        # i = 0

        for div in div_list:
            item = {}
            item['name'] = div.xpath('.//h2/text()')[0]
            item['content'] = div.xpath('.//div[@class="content"]/span/text()')[0]

            result_list.append(item)
            print(len(result_list))
            # i += 1
            # print(i)

        return result_list

    def save_result(self, result_list):
        for item in result_list:
            print(item)
        pass

    def run(self):
        # url_list
        url_list = self.get_url_list()

        # 遍历url_list
        for url in url_list:
            #  发送请求，获取参数
            html = self.get_html(url)
            #  分组提取数据(是一整页的数据)
            result_list = self.get_item(html)
            #  保存数据
            self.save_result(result_list)
        pass


if __name__ == '__main__':
    import time

    start = time.time()
    spider = QiushiSpider()
    spider.run()
    end = time.time()
    print('TIME:', (end - start))
