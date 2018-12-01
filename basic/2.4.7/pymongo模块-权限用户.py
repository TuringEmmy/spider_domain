# life is short, you need use python to create something!
# author    TuringEmmy
# time      18-11-23 下午6:34
# project   spider_study

from pymongo import MongoClient


'''
需要权限认证
'''

user = 'turing'
password = 'turing'

host = '127.0.0.1'
port = 27017

uri = 'mongodb://{}:{}@{}'.format(user, password, host)

client = MongoClient(uri, port=port)

col=client.turing.user
ret=col.insert({'name':'geng'})
print(ret)