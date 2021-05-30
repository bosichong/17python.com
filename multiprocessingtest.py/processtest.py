#codeing=utf-8
# @Time    : 2017-10.06
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python并发编程（上）进程模块multiprocessing模块和Process类
# @Url     : http://www.17python.com/blog/34
# @Details : Python并发编程（上）进程模块multiprocessing模块和Process类
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python并发编程（上）进程模块multiprocessing模块和Process类
###################################
'''
## Python中为什么要用多进程编程？

由于`Python`解释器中使用了内部的GIL全局解释器锁，使得`Python`多线程的并发在任意时刻只允许单个CPU来运行，这样的运行方式会影响程序的并发。
当程序是在I/O密集时，CPU可能会有更多的空闲处理多线程的并发，这种情况下一般是没有问题的。如果是大量计算密集型的应用，如果使用多线程来并发，性能会大大降低，
这个时候，我们就得考虑使用进程`Process`来进行编程及通信了。

## 创建进程Process
'''
###################################
# 第一种方法
###################################
# import time, os
# from multiprocessing import Process
# def clock(x,y):
#     for i in range(x):
#         print('当前时间=={0}'.format(time.ctime()))
#         time.sleep(y)
# if __name__ == '__main__':
#     p = Process(target=clock,args=(5,1))
#     p.start()
#     p.join()
###################################
# 第二种方法
###################################
# import time, os
# from multiprocessing import Process
# class ClockProcess(Process):
#     def __init__(self,x,y):
#         Process.__init__(self)
#         self.x=x
#         self.y=y

#     def run(self):
#         for i in range(self.x):
#             print('{0}=={1}'.format(os.getpid(),time.ctime()))
#             time.sleep(self.y)
# if __name__ == '__main__':
#     p = ClockProcess(5,1)
#     p1= ClockProcess(5,1)
#     p.start()
#     p1.start()
#     p.join()
#     p1.join()

# 通过`Process`类创建实例，然后传函数创建进程，另一种是继承`Process`类，然后重写`run()`方法创建要执行的任务。

###################################
# 第三种方法 进程池 Pool
###################################       
# from multiprocessing import Pool
# import os

# def clock(k):
#     for i in range(k):
#         print('{0}当前时间=={1}'.format(os.getpid(),time.ctime()))
#         time.sleep(k)
# if __name__ == '__main__':
#     l = [1 for i in range(20)]# 列表推导出一个列表对象
#     with Pool(5) as p:
#         p.map(clock,l)
'''
进程池方便创建多进程进行操作，创建使用也是比较简单的，使用时可以根据应用场景对线程的控制要求来选择线程的创建方式。

## 线程间的通信

`Python`为线程提供了`Queue、Pipes`等多种方式来交换数据，我们以`Queue`为例来演示学习一下进程间的通信及协作，稍后我们还要做分布式多进程的演示。

`Queue`进程间通信演示：
'''
###################################
# Queue进程间通信演示
################################### 
import multiprocessing as mp
import time, os
from queue import Queue

def prt_q(q):
    '''消费者打印数据'''
    while True:
        v = q.get()
        print(v)
        time.sleep(0.1)
def wrt_q(q):
    '''生产者添加数据'''
    for k in ['aa','bb','cc','dd','ee','ff','gg']:
        print("{0}已经加入到队列中".format(k))
        q.put(k)
        time.sleep(0.2)
if __name__ == '__main__':
    q = Queue()
    wrt_q(q)
    p = mp.Process(target=prt_q, args=(q,))
    p.start()
    p.join()

'''
`Queue`的使用其实就是生产者与消费者的模式，上边的代码运行后会有死锁，请按`ctrl+c`强制停止程序运行。
`Python`的进程有个很强大的地方，就是通过简单的配置就可以进行分布式多进程，这点是很吸引人的，稍后我会有一个篇幅来介绍一下分布式多进程。

'''