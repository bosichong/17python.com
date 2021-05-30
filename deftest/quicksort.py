# codeing=utf-8
# @Time    : 2018-01-30
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 聊聊Python中的递归与快速排序那点事
# @Url     : http://www.17python.com/blog/79
# @Details : 聊聊Python中的递归与快速排序那点事
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# 聊聊Python中的递归与快速排序那点事
###################################

'''

最近买了两本算法相关的书，快速了翻看了一下，原来算法真是编程解决问题的最基础要素，以前很少关注算法这块，以为学了基础了解了一些框架包模块等就是学会了编程，请原谅我。。。

## 在Python中递归

递归比较简单的例子就是阶乘，看下递归的必要条件：

+ 边界条件：确定递归到何时终止，也称为递归出口。
+ 递归模式：大问题是如何分解为小问题的，也称为递归体。

阶乘中如果n=1那么就达到了边界条件，递归结束，如果大于1那么进入递归模式调用本体，具体看下代码：


'''


def f(n):
    if n == 1: return 1
    return n * f(n - 1)
print(f(5))

'''
上边就是一个简单的递归阶乘函数，很简单喽，不过在`Python`中，递归调用是有限制的，通过如下代码可以查看递归可以使用的层数:

'''
import sys
sys.setrecursionlimit(5000)  # 设置递归层数
print(sys.getrecursionlimit())  # 查看
'''
## Python中的快速排序

快速排序法是一个非常精典的递归例子，C语言标准库中的`qsort`函数的实现主是采用的快速排序法。
快速排序算法的边界条件是数组中只有一个成中了，即停止排序，否则继续递归模式。
具体看代码：

'''
def q_sort(arr):
    if len(arr) < 2 :
        return arr
    else:
        p = arr[0]
        print(p)
        l = [i for i in arr[1:] if i <= p]
        g = [i for i in arr[1:] if i > p]
        temp = list()
        temp.append(p)
        return q_sort(l) + temp  + q_sort(g)
print(q_sort([2,44,3,77,6,5,888,999]))

'''
上边代码如果直接`return q_sort(l) + p  + q_sort(g)`是会报错的，所以修改了使用list相加。
算法其实很有意思，程序都是有算法组成的，以后得多看看了。

'''