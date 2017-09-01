#codeing=utf-8
# @Time    : 2017-09-01
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python 采集数据三步曲之（正则表达式 re.py）
# @Url     : http://www.17python.com/blog/9
# @Details : 有关python正则表达式学习笔记
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 如何用`Python`开始一个简单的正则表达式？
###################################
import re
p = re.compile(r'17python')#创建Pattern对象
m = p.match('17python.com')
if m :
    print(m.group())

#使用re模块方法代替实例方法
print(re.match('17python', '17python.com').group())


###################################
# re模块及正则实例常用方法演示
###################################
p = re.compile(r'17python')
s1 = '17python.com'
s2 = 'www.17python.com'
s3 = '17python.com17python.com'
s4 = 'abc.com'
p4 = re.compile('abc')
print(p.match(s1).group())
print(p.search(s2).group())
print(p.findall(s3))
print(p4.sub('17python', s4))
