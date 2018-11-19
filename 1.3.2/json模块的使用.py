# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.6
# author    TuringEmmy
# time      18-11-14 下午4:16
# project   reptile

import json

mydict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
        ],
    }
}

# 把dict or list 转换为json字符串
json_str = json.dumps(mydict,ensure_ascii=False,indent=2)
print(json_str)

# json字符串--> dict or list

json_dict = json.loads(json_str)
print(json_dict)

# python数据类型 写入 类文件对象
with open('mydict.json', 'w') as f:
    json.dump(mydict,f,ensure_ascii=False,indent=4)

# 类文件对象 取出 python数据类型
with open('mydict.json','r') as f:
    # 从类文件对象中读出并转换为dict or list
    ret = json.load(f)

print("*"*50)
print(type(ret))

print(ret)
