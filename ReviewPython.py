#codeing=utf-8
# @Time    : 2017-11-07
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 如何快速的复习学习过的Python
# @Url     : http://www.17python.com/blog/51
# @Details : 如何快速的复习学习过的Python
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 如何快速的复习学习过的Python
###################################

'''
最近老妈骨折住院，在医院护理了有8天，终于回出院回家了。回到家第一件事就是想到之前学习了python，如何快速的复习一下曾经学过的`python`呢？

## 语法/变量/表达式

也许我们能找到一个小小例子来快速的复习一下基本语法，那么这种例子有很多，比如：打印九九乘法表/斐波那契数列/排序法等等。

## 九九乘法表

快速复习`for`及`print format`等函数的用法。
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("{}X{}={}".format(i,j,i*j), end=' ')
    print()
'''
## 一摞`Python`风格的纸牌

在看《流畅Python》那本书的时候，第一章第一个小例子非常吸引人，具体代码如下
'''


'''
Python3 扑克牌
`collections.namedtuple`这个函数可以快速创建一个只有属性的类，我们通过这个方法来创建一张扑克牌的类
rank 和 suit 分别代表牌面数值和花色
'''
import collections
from random import choice
Card = collections.namedtuple('Card',['rank','suit'])
#创建一副扑克牌的类
class Cards:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')#从2-10的数字
    suits = 'spades clubs diamonds clubs'.split()# 黑桃 方块 草花 红桃

    def __init__(self):
        '''创建一副扑克牌'''
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks] + ['King','Queen']
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,position):
        return self._cards[position]

deck = Cards()#创建一副扑克牌
print(len(deck))#打印有多少张
#打印所有纸牌
for i in range(len(deck)):
    print(deck[i])
print(choice(deck))#随机抽取一张纸牌

'''
我觉得这个纸牌的小例子很有意思，复习了类及列表推导等一些小概念。当然快速复习的小例子还有很多的，比如下边的例子

## 简单的复利计算
'''
p = 200000 #初始金额
rate = 0.02/365 #利率 例如余额宝的年化收益为4%，那么每天的这里计算每天的收益
days = 365*30

day = 1
while day <= days :
    p = p * (1+rate)#复利，余额宝是每天的利滚利
    print('%s天：%2.2f' % (day,p)) #打印当前年份及金额
    day += 1
'''
通过以上三个小例子，是不是又引起了你对Python的兴趣？温故而知新，大家加油哦！
'''