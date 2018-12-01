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
from threading import Thread


class QiushiSpider():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

        self.URL_q = Queue()
        self.HTML_q = Queue()
        self.RESULT_q = Queue()

    def get_url_list(self):
        # 把所有url放入url队列中
        for i in range(1, 14):
            self.URL_q.put('https://www.qiushibaike.com/8hr/page/{}/'.format(i))

    def get_html(self):
        while True:
            url = self.URL_q.get()
            resp = requests.get(url, headers=self.headers)
            self.HTML_q.put(etree.HTML(resp.text))

            self.URL_q.task_done()      # 计数-1


    def get_item(self):
        """从响应的队列中取出数据"""
        while True:
            html = self.HTML_q.get()
            div_list = html.xpath('//div[@class="article block untagged mb15 typs_recent"]')
            # 进行分组提取数据
            result_list = []

            for div in div_list:
                item = {}
                item['name'] = div.xpath('.//h2/text()')[0]
                item['content'] = div.xpath('.//div[@class="content"]/span/text()')[0]

                result_list.append(item)
                print(len(result_list))

            self.RESULT_q.put(result_list)
            self.HTML_q.task_done()


    def save_result(self):
        while True:
            result_list = self.RESULT_q.get()
            for item in result_list:
                print(item)
            self.RESULT_q.task_done()


    def run(self):
        self.get_url_list()

        # t_html = Thread(target=self.get_html)
        # t_html.setDaemon(True)  # 设为守护线程结束,子线程随之结束
        # t_html.start()
        #
        # t_result = Thread(target=self.get_item)
        # t_result.start()
        #
        # t_save = Thread(target=self.save_result)
        # t_save.start()

        t_list = []
        for i in range(3):
            t_html = Thread(target=self.get_html)
            t_list.append(t_html)
        for i in range(10):
            t_result = Thread(target=self.get_item)
            t_list.append(t_result)
        t_save = Thread(target=self.save_result)
        t_list.append(t_save)

        for t in t_list:
            # 设为守护线程，子线程结束，子线程随之结束
            t.setDaemon(True)
            t.start()

        for q in [self.URL_q,self.HTML_q,self.RESULT_q]:
            q.join()    # 当前线程（主线程）阻塞，



if __name__ == '__main__':
    import time

    start = time.time()
    spider = QiushiSpider()
    spider.run()
    end = time.time()
    print('TIME:', (end - start))
