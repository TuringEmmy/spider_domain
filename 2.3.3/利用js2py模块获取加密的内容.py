# life is short, i use python
# author    TuringEmmy
# time      11/19/18 9:48 PM
# project   reptile

import requests

# 提前准备账号和密码
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

sesssion = requests.session()


# 获取key
url = 'http://activity.renren.com/livecell/rKey'
response= sesssion.get(url)
n = json.loads(url)
rkey=json.loads(response.text)['data']['rkey']
print(rkey)
url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js'
url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js'
# 获取三个js文件

# 发登录请求