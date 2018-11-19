# life is short, i use python
# author    TuringEmmy
# time      11/19/18 5:54 PM
# project   reptile

"""
1. rewuests.session
2. 向首页、登录页发送请求
3. 向图片发送请求
4. 发送登录请求
"""


import requests

session = requests.session()

session.headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# 登录页
url= 'http://oa.itcast.cn/seeyon/index.jsp'
session.get(url)

# 验证码
verify_image_url = 'http://oa.itcast.cn/seeyon/verifyCodeImage.jpg'
resp = session.get(verify_image_url)

with open('captcha.jpg','wb') as f:
    f.write(resp.content)

# 输入验证码
verify_image_code = input('请输入验证码:')

# 登录请求
log_url = 'http://oa.itcast.cn/seeyon/main.do?method=login'
data = {
    'authorization': '',
    'login.timezone': 'GMT+8:00',
    'login_username': 'yaoxiangyu@itcast.cn',
    'login_password': 'yao556696',
    'login_validatePwdStrength': '1',
    'login.VerifyCode': verify_image_code,
    'random': '',
    'fontSize': '12',
    'screenWidth': '1920',
    'screenHeight': '1080',
}

session.post(log_url,data=data)
# 注意：post之后没有返回值

# 登录验证
resp = session.get('http://oa.itcast.cn/seeyon/main.do?method=main')
print(resp.text)