#codeing=utf-8
# @Time    : 2017-09-02
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python 采集数据三步曲之[Requests开源协议的HTTP 库]
# @Url     : http://www.17python.com/blog/10
# @Details : Requests开源协议的HTTP 库
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 如何用`Python`开始一个简单的正则表达式？
###################################

import requests
###################################
# 一分钟上手
###################################
r = requests.get('http://www.baidu.com')
print(r.status_code)# 返回状态码
r.encoding = 'utf-8'# 设置编码
print(r.text) #返回html代码

###################################
# 带参数请求
###################################
r = requests.get('http://dict.baidu.com/s', params={'wd':'python'})
r.encoding = 'utf-8'# 设置编码
print(r.text) #返回html代码


# r.status_code #响应状态码
# r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
# r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# #*特殊方法*#
# r.json() #Requests中内置的JSON解码器
# r.raise_for_status() #失败请求(非200响应)抛出异常