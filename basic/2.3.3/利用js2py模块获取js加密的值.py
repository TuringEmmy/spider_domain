# life is short, you need use python to create something!
# author    TuringEmmy
# time      18-11-23 下午3:19
# project   spider_study

import requests
import json
import js2py

username = '15313088696'
password = '15313088696'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

session = requests.session()
session.headers = headers

# 获取rkey

url = 'http://activity.renren.com/livecell/rKey'

# 获取rKey和n的值
resp = session.get(url)
n = json.loads(resp.text)['data']

rKey = json.loads(resp.text)['data']['rkey']

print("*" * 100)
# 获取三个js文件=
url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js'
resp = session.get(url)
with open('RSA.js', 'w') as f:
    f.write(resp.text)

url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js'
resp = session.get(url)
with open('Barrett.js', 'w') as f:
    f.write(resp.text)

url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js'
resp = session.get(url)
with open('BigInt.js', 'w') as f:
    f.write(resp.text)

print("*" * 100)
# 利用js2py模块来获取加密后的密码
# 把js代码传入环境中,加载并执行
context = js2py.EvalJs()
with open('RSA.js', 'r') as f:
    context.execute(f.read())
with open('BigInt.js', 'r') as f:
    context.execute(f.read())
with open('Barrett.js', 'r') as f:
    context.execute(f.read())

# context.t就是js文件当中的那个t
context.t = {'password': password}
# 添加n的属性，直接添加即可
context.n = n
js = '''
    t.password = t.password.split("").reverse().join(""),
    setMaxDigits(130);
    var o = new RSAKeyPair(n.e,"",n.n)
    , r = encryptedString(o, t.password);
'''
"""
注意：前面打开是不执行代码，下面的js片段代码执行才生效，前面的只是与架子啊
"""
context.execute(js)
print(context.r)

# 获取登录之后的password

password = context.r
print(password)

# 发起登录请求
url = 'http://activity.renren.com/livecell/log'

data = {
    'phoneNum': username,
    'password': password,
    'c1': '-100',
    'rKey': rKey
}

print(data['password'])
resp = session.post(url, data=data)
# 再去范根登录以后的页面就可以了
print(resp)
