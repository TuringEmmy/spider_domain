# life is short, i use python
# author    TuringEmmy
# time      11/17/18 10:09 PM
# project   reptile
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')
driver.get('http://www.taobao.com')
time.sleep(1)

js = 'window.open("https://www.sogou.com");'
driver.execute_script(js)
print(driver.current_url)  # https://www.taobao.com/

time.sleep(1)
print('\n')
print('-' * 60)
print('标签窗口切换')
print('-' * 60)

# 获取所有的标签页id的列表
windows_list = driver.window_handles
driver.switch_to.window(windows_list[1])
print(driver.current_url)  # https://www.sogou.com/

driver.quit()
