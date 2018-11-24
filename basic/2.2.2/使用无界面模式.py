# life is short, i use python
# author    TuringEmmy
# time      11/17/18 10:46 PM
# project   reptile

import time

from selenium import webdriver


opation = webdriver.ChromeOptions()
# 开启无界面模式
opation.add_argument('--headless')
# 禁用显卡：防止各种硬件造成的意外异常发生
opation.add_argument('--disable-gpu')

# 替换ua
opation.add_argument('--user-agent=Mozilla/5.0 HAHA') # 替换ua
# ip_port='https://202.20.16.82:10152'
# option.add_argument('--proxy-server={}'.format(ip_port))
opation.add_argument('--proxy-server=https://14.204.20.95:8080') # 使用代理ip

driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver',chrome_options=opation)
driver.get('https://mail.qq.com')

# 切入iframe里面之后才能起效
frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(frame)

# 输入账号密码并登录
driver.find_element_by_xpath('//*[@id="u"]').send_keys('2117524839@qq.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="p"]').send_keys('2117524839@qq.com')
time.sleep(1)
driver.find_element_by_id('login_button').click()
time.sleep(1)



# 登录不成功，在去去左边的文字
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_class_name('login_pictures_picture').get_attribute('style'))
driver.quit()