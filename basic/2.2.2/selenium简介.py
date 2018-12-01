# life is short, i use python
# author    TuringEmmy
# time      11/17/18 9:16 AM
# project   reptile

from selenium import webdriver
#
driver = webdriver.PhantomJS(executable_path='/mnt/hgfs/WorkSpace/driver/phantomjs')
# driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')

driver.get("http://www.baidu.com")
# 最新Google70版本不好使
driver.save_screenshot('chrome.png')

driver.quit() # 一定要退出！不退出会有残留进程！