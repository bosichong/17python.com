

'''
环境配置
IDE vscode pycharm

代码仓库 github gitee

python 官方文档中文 
https://docs.python.org/zh-cn/3.8/

程序的基本编写方法 IPO

I:Input 输入，程序的输入，数据机构。
P:Process 处理 程序的主要逻辑，算法。
O:Output 输出，程序的输出。


print([n*n for n in range(1,9)]) 列表推导
(n*n for n in range(9)) 生成器表达式


函数的复用




'''

# def getadd():
#     return 

# def add():
#     pass

# add()



# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# print(fact(2))



# 斐波那契数
a, b = 0, 1
while b < 20:
    print(b)
    a, b = b, a+b




import threading
import time
def pp(key):
    while True:
        print(key)
        time.sleep(1)


t1 = threading.Thread(target=pp,args=("haha",))
t1.start()

t2 = threading.Thread(target=pp,args=("lailai",))
t2.start()


# a,b = map(int,input("请输入两个值','号分隔：").split(','))

# print(a+b)

# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def say(self):
#         print("我叫{},我已经{}".format(self.name,self.age))

# p = Person("张三",18)
# p.say()

