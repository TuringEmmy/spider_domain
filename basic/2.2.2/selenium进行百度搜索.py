# life is short, i use python
# author    TuringEmmy
# time      11/17/18 7:45 PM
# project   reptile

from selenium import webdriver

driver = webdriver.Chrome('/home/worker/Desktop/driver/chromedriver')

driver.get('http://www.baidu.com')
# 返回标签对象
element = driver.find_element_by_xpath('//*[@name="wd"]')

element.send_keys('雍珑庚')

driver.find_element_by_id('su').click()
# input(111)
print('\n')
print('-' * 60)
print('查看网页的源代码')
print('-' * 60)

html_str = driver.page_source
print(html_str)

print('\n')
print('-' * 60)
print('获取cookies')
print('-' * 60)

print(driver.get_cookies())

driver.quit()


