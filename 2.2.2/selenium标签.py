# life is short, i use python
# author    TuringEmmy
# time      11/17/18 8:58 PM
# project   reptile

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')


driver.get('http://www.itcast.cn')

rets = driver.find_elements_by_partial_link_text('传智')


for ret in rets:
    print(ret.text)


print('\n')
print('-'*60)
print('提取属性的值的方法:get_attribute')
print('-'*60)

rets = driver.find_elements_by_partial_link_text("传智")
for ret in rets:
    print(ret.get_attribute('href'))




driver.quit()
