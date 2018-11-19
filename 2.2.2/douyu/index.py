# life is short, i use python
# author    TuringEmmy
# time      11/18/18 12:06 AM
# project   reptile
import time

import requests
from selenium import webdriver



class Douyu:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')


    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')

        content_list = []

        for li in li_list:
            item={}
            item['title'] = li.find_element_by_xpath('./a').get_attribute("title")
            item['anchor']=self.driver.find_element_by_xpath('//*[@id="live-list-contentbox"]/li[1]/a/div/p/span[@class="dy-name ellipsis fl"]').text
            item['number']=self.driver.find_element_by_xpath('//*[@id="live-list-contentbox"]/li[1]/a/div/p/span[@class="dy-num fr"]')

            content_list.append(item)

            # 提取下一页url链接
            next_url = self.driver.find_element_by_xpath('//*[@id="J-pager"]/a[11]')
            next_url=next_url[0] if len(next_url)>0 else None


            return content_list,next_url


    def save_content_list(self, content_list):
        for content in content_list:
            print(content_list)

    def run(self):
        # 1. 获取start_url
        start_url = self.start_url
        # 2. 发送请求，获取响应
        self.driver.get(self.start_url)
        # 3. 提取数据
        content_list, next_url = self.get_content_list()
        # 4. 保存
        self.save_content_list(content_list)
        # 5. 下一页数据提取

        while next_url is not None:
            next_url.click()
            time.sleep(0.1)
            content_list,next_url=self.get_content_list()
            self.save_content_list()

if __name__ == '__main__':
    spier = Douyu()
    spier.run()



driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver')

driver.get('https://www.douyu.com/')

print(driver.current_url)


# 热门分类
img_list = driver.find_elements_by_xpath('//*[@id="mainbody"]/div[3]/div[1]/div[2]/ul/li/a/img')
print(img_list)

driver.quit()