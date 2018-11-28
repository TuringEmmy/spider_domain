1. scrapy的概念 Scrapy是爬虫框架，少量的代码，就能够快速的抓取

2. scrapy的工作流程
	```
3个内置数据类型
	a. request请求对象:
		url
		headers
		method
		post_data
	b. response响应对象：
		url
		headers
		status_code
		content
	c. item数据: 本质是dict

	5大模块
	a. spider爬虫：提取url、item，构造request对象，组织抓取逻辑
	b. scheduler调度器：把request放入请求队列中
	c. downloader下载器：发送请求，获取response响应对象
	d. item pipeline管道：保存处理item数据
	e. scrapy engine引擎：组织scrapy的运行逻辑

	2个中间件：对request、response进行预处理
	a. 下载中间件
	b. 爬虫中间件

	scrapy的逻辑流程：
	a. spider对start_url构造request
	b. request--爬虫中间件--引擎--调度器，放入请求队列
	c. 调度器从请求队列取出一个request--引擎--下载中间件--下载器，发送请求获取response
	d. response--下载中间件--引擎--爬虫中间件--爬虫，解析提取
	e. 爬虫对response提取，提取的是url，构造成request-->重复b步骤
	f. 爬虫对response提取，提取的是item--引擎--管道，处理保存
	```

3. 简单使用scrapy
	```
创建scrapy项目 scrapy startproject 项目名
	在项目路径下创建爬虫 scrapy genspider 爬虫名字 允许爬取的域名
	完善spider
	在项目路径下运行scrapy项目 scrapy crawl 爬虫名
	```

4. response响应对象的常用属性
    ```
# print(response.body) # 响应内容 bytes
    # print(response.url) # 响应的url地址
    # print(response.request.url) # 响应对应请求的url
    # print(response.headers) # 响应的头信息
    # print(response.request.headers) # 响应对应请求的headers
    # print(response.status) # 状态码
    ```