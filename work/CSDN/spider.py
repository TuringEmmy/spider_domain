# this virtualenv is used for spider 
# author    python
# time      18-11-15 下午4:29
# project   reptile
from bs4 import BeautifulSoup
import requests
import time


url =('https://blog.csdn.net/sinat_26745777/article/details/83983670')



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
for i in range(10000):
    time.sleep(2)
    req = requests.get(url,headers =headers )
    soup = BeautifulSoup(req.text,'lxml')
    rank =  soup.select('#blog_rank')
    view = soup.select('.article_manage .link_view .title')
    print (view)
    print (i)
