#codeing=utf-8
# @Time    : 2017-09-20
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python random 随机数模块操作总结
# @Url     : http://www.17python.com/blog/20#
# @Details : Python random 随机数模块操作总结
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python random 随机数模块操作总结
###################################
import random
# random，是Python中用于生成随机数模块，我们来了解一下这修模中几个常用的函数，这些随机函数可以应付一些日常应用了。

#random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
print(random.random())
# random.uniform(a,b) 用于生成 a-b 之间的随机浮点数。
print(random.uniform(1,5))
# random.randint(10,20) 生成随机整数
print(random.randint(10,20))
# 生成0-100之间的偶数。
print(random.randrange(0,100,2))
#choice()用来生成随机字符串，
print(random.choice(("a","b","c","d")))
print(random.choice(['ee','ff','gg','hh']))
# shuffle() 类似洗牌，每次刷新都会不一样的。
p = ['a','b','c','d']
random.shuffle(p)
print(p)
# 从一个列表中取出一个随机切片数据，原数据不变，结果刷新可见
l = [1,2,3,4,5,6,7,8,9]
sl = random.sample(l,3)
print(sl)
print(l)
