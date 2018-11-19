requests模块课堂笔记

1. 发送简单的get请求
   response = requests.get('http://host:port')

   ​

2. 响应对象response的常用属性
   response.url
   response.status_code 状态码

   response.headers 响应头
   response.request.headers 请求头

   response.cookies 响应的cookie；cookiejar对象
   response.request._cookies 请求的cookie

   ​

3. 响应的文本内容
   response.text 返回str类型
   response.content 返回bytes类型

   ​

4. 解决响应内容中文乱码问题
   response.content.decode()

   ```
   # decode('ascii') 
   # gbk gb2312 iso8859-1
   ```

   ​

5. 保存流媒体文件到本地
   url对应的响应内容就是该文件的源码
   以bytes类型保存到文件中