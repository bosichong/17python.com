#codeing=utf-8
# @Time    : 2017-09-01
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python3 函数学习笔记
# @Url     : http://www.17python.com/blog/15
# @Details : python3函数学习笔记简单总结
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1

###################################
# 函数的定义，Python 定义函数使用 def 关键字
###################################
def hello():
    '''定义一个hello打印的函数，\n
    返回字符串'''
    return 'hello world'




# 使用函数
print(hello())

###################################
# 有参数并有返回值的函数
###################################
def add(x, y):
    return x+y
print(add(2,5))
###################################
#多个返回值时，返回一个tuple
###################################
def rst(x,y):
    return x+y, x-y
print(rst(3,1))
###################################
# 任意参数有返回值 *为tuple **为list
###################################
def rst_a(*k, **s):
    rst = 0
    for v in k :
        rst += v
    return rst,s
print(rst_a(1,2,3,4,aa='aa',bb='bb'))
###################################
# 有意思的lambda
###################################
l = lambda x, y : x + y
print(l(2,8))
###################################
# 装饰器语法糖 在Python中，可以使用”@”语法糖来精简装饰器的代码
# 函数可以支持(*args, **kwargs)可变参数。
###################################
import time

def t(func):
    '''定义一个程序运行时间计算函数'''
    def wrapper(*args, **kwargs):
        start = time.time()#起始时间
        func(*args, **kwargs)#要执行的函数
        end = time.time()#结束时间
        print('程序运行时间:{:.2f}ms'.format((end-start)*1000))
    return wrapper

def log(fun):
    '''一个打印函数运行日志的方法'''
    def wrapper(*args, **kwargs):
        print(fun.__name__,'函数开始运行')
        fun(*args, **kwargs)
        print(fun.__name__,'函数运行结束')
    return wrapper


@t  #统计程序运行时间
@log #打印日志
def myfunc(x,y):
    '''打印从x到y的数值'''
    for i in range(x,y):
        print(i)

myfunc(3,6)
