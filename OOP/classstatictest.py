#codeing=utf-8
# @Time    : 2017-09-30
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : python 类的静态方法和类方法
# @Url     : http://www.17python.com/blog/30
# @Details : python 类的静态方法和类方法
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# python 类的静态方法和类方法
###################################
'''
##静态方法和类方法的定义

`Python`中类的静态方法使用`@staticmethod`装饰器来定义
`Python`中类方法使用`@classmethod`装饰器来定义

'''

class Hello:
    k = 2
    #定义一个类的静态方法
    @staticmethod
    def add(x,y):
        return x + y
    #定义一个类方法
    @classmethod
    def mul(cls,x):
        return cls.k * x

print(Hello.add(999,1))#使用静态方法 结果为1000
print(Hello.mul(2))#使用类方法 结果为4


#类的静态方法使用和使用普通函数一样简单，但类方法确有些不同，她只能用于类本身，把自身做为对象进行操作。
#我们继承一下`Hello`这个类，看看静态方法和类方法是不是能被继承？

class World(Hello):
    k = 4

print(World.add(1,999))
print(World.mul(2))

# 通过上边的例子，我们可以发现子类可以继承使用父类方法和父类的静态方法，如果类变量值有所变化，结果也会有所不同。
