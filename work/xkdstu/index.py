# this virtualenv is used for spider 
# author    python
# time      18-11-14 下午7:36
# project   reptile

import requests

proxies = {
    "http":"http://163.125.65.187:9797",
    "http":"http://119.31.210.170:7777"
}

headers ={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
for i in range(10):
    ret = requests.get('https://blog.csdn.net/sinat_26745777/article/details/83983670',headers=headers,proxies=proxies)

conten = ret.content.decode()

print(conten)

