#codeing=utf-8
# @Time    : 2017-09-19
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python 对象引用与复制 (Python参考手册读书笔记)
# @Url     : http://www.17python.com/blog/19
# @Details : Python 对象引用与复制 (Python参考手册读书笔记)
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1

###################################
# Python 对象引用与复制 (Python参考手册读书笔记)

# 通过赋值创建一个副本
a = [1,2,3,4,5]
b = a
print(b is a )
b[2] = -99
print(a)

#通过控制台打印，我们修改list b中的值，打印a发现值也跟着变化了，说明a与b的引用是同一个对象

## 浅复制 通过结果可以发现一些不同

c = [11,22,]
d = list(c)
print(c is d)
d.append(33)
print(c)
print(d)
d[1] = 00
print(c)
print(d)
## 深复制 

import copy
e = [11,12,13]
f = copy.deepcopy(e)
print(e is f)
f[1] = 78
print(e)
print(f)