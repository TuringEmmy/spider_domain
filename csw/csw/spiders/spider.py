import requests


url = 'https://ypk.familydoctor.com.cn/58543/instructions/'
ret = requests.get(url,timeout=0.001,verify=False)


print(ret)