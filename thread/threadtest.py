#codeing=utf-8
# @Time    : 2017-09-29
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python多线程编程（1）多线程创建的几种方法
# @Url     : http://www.17python.com/blog/32
# @Details : Python多线程编程（1）多线程创建的几种方法
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python多线程编程（1）多线程创建的几种方法
###################################

'''
## Python多线程
在编程的日常中，如果遇到大量相同并且重复的计算任务时，我们考虑使用多线程，多线程可以并发的执行程序中的函数，这样就可以更快的利用CPU计算结果，结省时间成本。
`Python`中创建线程的方法有很多，可以通过`thread threading.Thread`或是线程池提供的方法来创建线程,这节我们主要讨论如何创建线程。

## 单线程时的操作

我们定义一些操作，先用单线顺序操作。
'''
# import time
# def loop():
#     print("循环loop1打印时间======",time.ctime())
#     time.sleep(3)   
# loop()
# loop()
# print("loop1打印结束时间======",time.ctime())
'''
循环loop1打印时间====== Mon Oct  2 07:59:17 2017
循环loop1打印时间====== Mon Oct  2 07:59:20 2017
loop1打印结束时间====== Mon Oct  2 07:59:23 2017

顺序执行程序后，共花掉6秒时间，如果我们可以并发执行这个打印，或许我们能节约一些时间。

## thread

`thread`提供了一些线程创建与操作的方法，但官方文档及各类参考书中均有提到，`_thread`是一个比较低级的线程操作模块不建使用，这里我们也只是带过。

'''


# import _thread
# from utils import tn # 导入工具类中计算程序执行时间的函数
# def loop():
#     print("循环loop1打印时间======",time.ctime())
#     time.sleep(3)  
# @tn
# def main():
#     _thread.start_new_thread(loop, ())
#     _thread.start_new_thread(loop, ())
#     time.sleep(3)
#     print("如果上边没有sleep()，程序会没有运行完打印直接退出")
# if __name__ == '__main__':
#     main()

'''
循环loop1打印时间====== Mon Oct  2 14:24:49 2017
循环loop1打印时间====== Mon Oct  2 14:24:49 2017
如果上边没有sleep()，程序会没有运行完打印直接退出
程序运行时间:3.01ms

这次程序的运行我节省了3秒钟的宝贵时间！但也发现了`thread`模块的一些缺点，比如主线程结束时不会等待其它线程，这将导致程序没有打印结果直接退出了，这是我们不想看到的。
所以，由于`thread`模块的功能缺陷，通常不推荐使用`thread`,我们将继续讨论更高级的线程模块`threading`和其它线程相关模块。


## threading模块 Thread类

创建一个`Thread`实例，其中`target`这个参数可以接受一个函数.
我们先来试试，代码如下：
'''
# import time
# import threading
# from utils import tn # 导入工具类中计算程序执行时间的函数
# def loop1(tname):
#     print(tname+"循环loop1打印时间======" + time.ctime())
#     time.sleep(2)
# @tn
# def main():
#     print('程序开始执行，耐心等待几秒。')
#     threads = []#定义一个线程队列
#     for i in range(5):
#         t = threading.Thread(target=loop1, args=("thread"+str(i),))
#         threads.append(t)
#     for i in range(5):
#         threads[i].start()
#     for i in range(5):
#         threads[i].join()
# if __name__ == '__main__':
#     main()

# 通过继承`Thread`类派生子类并创建线程的对象。

# import time
# import threading
# from utils import tn # 导入工具类中计算程序执行时间的函数
# class MyThread(threading.Thread):
#     def __init__(self, func, name=''):
#         threading.Thread.__init__(self) # 这里必须添加父类的构器方法
#         self.func = func
#         self.name = name
#     #此方法必须实现
#     def run(self):
#         self.func(self.name)

# def loop1(tname):
#     print(tname+"循环loop1打印时间======" + time.ctime())
#     time.sleep(2)
# @tn
# def main():
#     print('程序开始执行，耐心等待几秒。')
#     threads = [] #定义一个线程队列
#     for i in range(5):
#         t = MyThread(loop1, "thread"+str(i))
#         threads.append(t)
#     for i in range(5):
#         threads[i].start()
#     for i in range(5):
#         threads[i].join()
# if __name__ == '__main__':
#     main()

'''
注意：`run()`此方法必须实现;`threading.Thread.__init__(self)` 必须添加父类的构器方法

二种方法相比较起来，通过继承`Thread`类来创建线程的实例更直观灵活一些，通过以上例子的对比来看，多线程并发执行程序要比单线程执行节约很多时间。
关于多线程实例的创建还有其它方法，比如`Thread`构建方法中target参数也可以传入一个实例，不过个人感觉没有继承`Thread`类创建的实例更直观些，这里也就不举例了，
另外还可以通过线程池创建一组线程用来执行任务。

## threadpool Python线程池

`Python3`下载安装模块

    pip3 install threadpool

用线程池测试一下刚才的打印，代码如下：
'''
import time
import threadpool
from utils import tn # 导入工具类中计算程序执行时间的函数
def loop1(tname):
    print(tname+"循环loop1打印时间======" + time.ctime())
    time.sleep(2)
@tn
def main():
    l = ['11111','22222','33333','44444','55555']
    pool = threadpool.ThreadPool(5)# 创建一个线程池
    requests = threadpool.makeRequests(loop1, l) #传入函数 及函数需要的参数
    [pool.putRequest(req) for req in requests]# 不理角这段代码，猜测是循环创建线程 分配任务。
    pool.wait()#设置池内所有线程等待。

if __name__ == '__main__':
    main()

'''
`Python`线程的创建方法应该还有很多种，这里就不在介绍了，博主感觉继承`Thread`类创建实例的方法比较经典可行，代码直观，其次是创建`Thread`对象传参进去也是简单到家了。
有关`Python`线程的创建就先聊到这里，稍后再研究一下线程锁，这几天正值国庆节，祝大家玩的开心！

'''