1) "title:requests"
Scheduler队列，存放的待请求的request对象，获取的过程是pop操作, 即获取一个踢去一个
2) "title:dupefilter"
指纹集合，存放的是已经进入scheduler队列的request对象的指纹，指纹默认有请求方法，url, 和请求体组成
3) "title:items"
存放获取到的item信息，在piplines中开启RedisPipeline才会存入
