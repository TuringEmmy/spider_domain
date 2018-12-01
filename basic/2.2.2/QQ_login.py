# life is short, i use python
# author    TuringEmmy
# time      11/17/18 10:16 PM
# project   reptile
import time

from selenium import webdriver

# ubutu16.04安装的浏览器是50的,所以更换驱动
driver = webdriver.Chrome(executable_path='/mnt/hgfs/WorkSpace/driver/chromedriver50')
driver.get('https://mail.qq.com')

# 切入iframe里面之后才能起效
frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(frame)

# 输入账号密码并登录
driver.find_element_by_xpath('//*[@id="u"]').send_keys('2117524839@qq.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="p"]').send_keys('XXXXXXXX')
time.sleep(1)
driver.find_element_by_id('login_button').click()
time.sleep(1)

# 登录不成功，在去去左边的文字
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_class_name('login_pictures_picture').get_attribute('style'))
driver.quit()
