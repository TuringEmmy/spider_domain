# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# 将redis转换为指纹
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


print("*" * 100)
# 添加数据库的连接地址
REDIS_URL = "redis://127.0.0.1:6379"  # 或者使用下面的方式
# REDIS_HOST = "127.0.0.1"
# REDIS_PORT = 6379
print("*" * 100)

# request调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 表示是否持久化request队列和request指纹
SCHEDULER_PERSIST = True






# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# 开启两个数据管道
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1


