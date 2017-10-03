#codeing=utf-8
# @Time    : 2017-09-29
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : python面向对象编程（OOP）初探
# @Url     : http://www.17python.com/
# @Details : python面向对象编程（OOP）初探
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
import time
def tn(func):
    '''定义一个程序运行时间计算函数'''
    def wrapper(*args, **kwargs):
        start = time.time() # 起始时间
        func(*args, **kwargs) # 要执行的函数
        end = time.time() # 结束时间
        print('程序运行时间:{:.2f}ms'.format((end-start)))
    return wrapper