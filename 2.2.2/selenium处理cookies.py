# life is short, i use python
# author    TuringEmmy
# time      11/17/18 9:23 PM
# project   reptile

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')
driver.get('http://www.baidu.com')

cookies_list = driver.get_cookies()

cookies_dict = {cookie['name']:cookie['value'] for cookie in cookies_list}
print(cookies_dict)

driver.quit()
