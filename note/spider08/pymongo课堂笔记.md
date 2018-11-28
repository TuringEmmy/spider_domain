1. 权限认证的方式
   ```
   from pymongo import MongoClient
   uri = 'mongodb://账号:密码@ip'
   client = MongoClient(uri, port=27017)
   col = client.db.col
   col.insert({数据}) # 返回_id中OId的值
   ```
2. 无需权限认证的方式
   ```
   from pymongo import MongoClient
   client = MongoClient(host='127.0.0.1', port=27017)
   col = client.db.col
   col.insert({数据}) # 返回_id中OId的值
   ```

3. 插入
   ```
   col.insert({一条数据}/[{},{},...]) # 返回objectid中的值
   ```

4. 查询
   ```
   查询一个col.find_one({})
   查询多个col.find() # 返回可迭代的cursor游标对象,只能遍历一次
   ```

5. 更新
   ```
   col.update({条件},
   {'$set':{指定的kv/完整的doc}},
   multi=False/True, # 默认False只更新一条
   upsert=False/True) # 默认False，改为True表示没有就插入，存在就更新
   ```
6. 删除
   ```
   删除一个col.delete_one({条件})
   删除多条col.delete_many({条件})
   ```


​	