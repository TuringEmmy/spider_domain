# life is short, you need use python to create something!
# author    TuringEmmy
# time      18-11-23 下午6:57
# project   spider_study

from pymongo import MongoClient

client = MongoClient()

col = client.turing.user

print("*" * 100)
# 插入多条数据
queue_list = [{'id': i} for i in range(3)]
rets = col.insert(queue_list)

for ret in rets:
    print(ret)

print("*" * 100)
# 查找一条数据
ret = col.find_one({'id': 2})
# 单引号，是字典哦
# ObjectId这个是mongodb自带的字典
print(ret)

# import json
# print(json.dumps(ret))
# 注意：自带的对象不能dumps
# 如果吧这个对象去掉，可以使用投影
# ret=col.find({'id':3},{"_id":0})

# del ret['_id']
ret.pop('_id')
print(ret)

print("*" * 100)
# 查询多条数据
rets = col.find()

for ret in rets:
    del ret['_id']
    print(ret)
# 注意:带游标的可迭代对象只能迭代一次
# 最好的办法就是提前使用一个列表,将结果存入,方便下次进行接待
print("*" * 100)
"""更新"""
ret = col.update({'turing': 0}, {'$set': {'name': 'emmy'}}, multi=False, upsert=True)
print(ret)

# 更新多条
rets = col.update({}, {'$set': {'name_id': "long"}}, multi=True, upsert=True)
print(rets)

print("*" * 100)
# 删除数据
ret = col.delete_one({"id": 0})
print(ret)

# 删除多个
# col.delete_many({'name_id': 'long'})
# col.delete_many({})

