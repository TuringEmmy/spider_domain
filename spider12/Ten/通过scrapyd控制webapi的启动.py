# life is short, you need use python to create something!
# author    TuringEmmy
# time      11/28/18 4:41 PM
# project   spider_study


import requests

# ======================================================================================
# # 启动爬虫
# # curl http://localhost:6800/schedule.json -d project=default -d spider=somespider
#
# url = 'http://localhost:6800/schedule.json'
#
# data = {
#     'project': 'Ten',
#     'spider': 'title'
# }
# resp = requests.post(url, data=data)
# print(resp.text)
# ========================================================================================

# 停止爬虫
# curl http://localhost:6800/cancel.json -d project=project_name -d job=jobid
url = 'http://localhost:6800/cancel.json'
data = {
    'project': 'Ten',
    'job': 'c9118830f2e911e8b5ff000c29ff341f'
}
resp=requests.post(url,data)
print()