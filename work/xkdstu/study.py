# this virtualenv is used for spider 
# author    python
# time      18-11-14 下午7:42
# project   reptile


import requests



headers ={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
for i in range(10):
    ret = requests.get("https://www.xust.edu.cn/xyjj/xxgk.htm",headers=headers)
    print(i)

conten = ret.content.decode()

# print(conten)