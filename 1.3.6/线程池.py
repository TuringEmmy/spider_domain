# life is short, i use python
# author    TuringEmmy
# time      11/17/18 3:16 PM
# project   reptile

# life is short, i use python
# author    TuringEmmy
# time      11/16/18 10:26 PM
# project   reptile

# life is short, i use python
# author    TuringEmmy
# time      11/16/18 9:51 PM
# project   reptile

# url_list

# 遍历url_list
#  发送请求，获取参数
#  分组提取数据
#  保存数据
import requests
from lxml import etree

from queue import Queue
from multiprocessing.dummy import Pool


# 注意：dummy下面全是线程,默认是cpu个


class QiushiSpider():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

        # 开8个线程
        self.pool = Pool(8)

        # 存储url
        self.q = Queue()

        # 计数url的总数
        self.url_nums = 0
        # 处理完的响应数
        self.total_responses_nums = 0
        # 程序是否运行的标志
        self.is_running = True

    def get_url_list(self):
        # 把所有url放入url队列中
        for i in range(1, 14):
            self.q.put('https://www.qiushibaike.com/8hr/page/{}/'.format(i))
            self.url_nums += 1

    def get_html(self, url):
        resp = requests.get(url, headers=self.headers)
        return etree.HTML(resp.text)

    def get_items(self, html):
        """从响应的队列中取出数据"""
        div_list = html.xpath('//div[@class="article block untagged mb15 typs_recent"]')
        # 进行分组提取数据
        result_list = []

        for div in div_list:
            item = {}
            item['name'] = div.xpath('.//h2/text()')[0]
            item['content'] = div.xpath('.//div[@class="content"]/span/text()')[0]

            result_list.append(item)
            # print(len(result_list))

        return result_list

    def save_result(self, result_list):

        for item in result_list:
            print(item)

    def exetute_request_item_save(self):
        """从队列中去除一个url,发请求得响应，提取数据，并保存；完整处理一个URL"""
        url = self.q.get()
        html = self.get_html(url)
        result_list = self.get_items(html)

        self.save_result(result_list)
        # 处理完的响应数+1
        self.total_responses_nums += 1


    def _callback(self, temp):
        # apply_asybc中回调函数固定接受运行函数的返回值作为参数！不能省略
        # print(xxx)
        # print('\n')
        # print('-'*60)
        # print('这是一个而没有while循环')
        # print('-'*60)

        if self.is_running:
            self.pool.apply_async(self.exetute_request_item_save, callback=self._callback)

    def run(self):
        # 构造url队列
        self.get_url_list()

        # 控制并发规模
        for i in range(8):
            # 调用线程池的异步方法去不断的处理一个url直到处理完毕
            self.pool.apply_async(self.exetute_request_item_save, callback=self._callback)

        # 不断判断是否退出程序
        while True:
            if self.total_responses_nums >= self.url_nums:
                self.is_running = False
                break
        print('over')
        self.pool.close()


if __name__ == '__main__':
    import time

    start = time.time()
    spider = QiushiSpider()
    spider.run()
    end = time.time()
    print('TIME:', (end - start))
