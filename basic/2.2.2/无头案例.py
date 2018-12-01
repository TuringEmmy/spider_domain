# life is short, i use python
# author    TuringEmmy
# time      11/17/18 11:53 PM
# project   reptile

from selenium import webdriver

opation = webdriver.ChromeOptions() # 实例化配置对象
opation.add_argument('--headless') # 开启无界面模式
opation.add_argument('--disable-gpu') # 禁用显卡:防止各种硬件造成的意外异常发生

opation.add_argument('--user-agent=Mozilla/5.0 HAHA') # 替换ua
opation.add_argument('--proxy-server=https://202.20.16.82:10152') # 使用代理ip

driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver', chrome_options=opation)

driver.get('http://www.taobao.com')

print(driver.current_url)

driver.quit()