# life is short, i use python
# author    TuringEmmy
# time      11/17/18 9:33 PM
# project   reptile
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')
driver.get('http://www.taobao.com')

# 定位淘抢购

i=0
while True:
    i+=1
    js = 'document.documentElement.scrollTop={}'.format(i*500)
    try:
        # 定位到【淘抢购】
        ret = driver.find_element_by_xpath('//*[@title="淘抢购"]')
        # 图片标签的上一级
        href = driver.find_element_by_xpath('//*[@title="淘抢购"]/..').get_attribute('href')
        # print(ret.get_attribute('src'))
        print(href)
        driver.quit()
        break
    except:

        # print(js)
        driver.execute_script(js)
        # 强制等待1秒，让浏览器加载一会儿
        time.sleep(1)
        print('None')


