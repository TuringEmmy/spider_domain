# life is short, i use python
# author    TuringEmmy
# time      11/17/18 8:29 PM
# project   reptile

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/mnt/hgfs/WorkSpace/driver/chromedriver50')


driver.get('http://www.itcast.cn')

print('\n')
print('-'*60)
print('定位方法')
print('-'*60)

ret = driver.find_element_by_xpath('//div[@class="city"]/h3')

print(ret.text)

driver.quit()

