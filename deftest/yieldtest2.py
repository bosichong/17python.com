#codeing=utf-8
# @Time    : 2017-10-15
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 浅谈Python中的协程及利用协程代替多线程及多进程并发编程。
# @Url     : http://www.17python.com/blog/43
# @Details : 浅谈Python中的协程及利用协程代替多线程及多进程并发编程。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 浅谈Python中的协程及利用协程代替多线程及多进程并发编程。
###################################

'''
协程定义说的清楚明了的文章不是很多，手头上有几本Python相关的书籍，其中流畅的Python一书中解释协程的定义是我认为最简单明了的。

## 生成器如何演变成协程？

乍看生成器和协程长的可真象，因为都用到了yield关键字，那么问题来了，如何区分二者？

'''

def cd(n):
    print("Counting down from %s" % n)
    while n > 0:
        yield n
        n -= 1
c = cd(10)
next(c)
for i in c :
    print(i,end=' ')

'''
上边是一个典型的生成器函数，我们稍加变化使之成为协程。
'''

def cd1():
    n = yield
    while n > 0:
        print("Counting down from %s" % n)
        n -= 1

c1 = cd1()
next(c1)
c1.send(10)
#运行到这里应该抛出一个异常

'''
生成器和协程的不同有没有看出来？很明显的有两处：
+ yield的位置
+ next()和send()函数的用法
通过运行结果我们可以到最后抛出了一个异常`StopIteration`,结束了这个协程。我们可以考虑一下：用装饰器省略掉next()这步，然后捕获抛出的异常，优雅的关闭掉协程函数。
'''
from functools import wraps
def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer
@coroutine
def cd2():
    n = yield
    while n > 0:
        print("Counting down from %s" % n)
        n -= 1
try:
    cd2().send(10)
except Exception as e:
    print('协程任务终止')

'''
带上了装饰器，就更简便一些了，最后捕获异常，就可以优雅的结束这个协程了。

## 利用协程代替线程或进程进行并发编程

我们想用生成器（协程）作为系统线程的替代方案来实现并发。协程有时也称为用户级线程或绿色线程。————引自《Python Cookbook》
这里的协程用到了asyncio模块，利用asyncio模块实现了一个协程的并发。关于asyncio的实现原理，稍后再研究一下。

'''
import asyncio
import time
import threading
def tn(func):
    '''定义一个程序运行时间计算函数'''
    def wrapper(*args, **kwargs):
        start = time.time() # 起始时间
        func(*args, **kwargs) # 要执行的函数
        end = time.time() # 结束时间
        print('程序运行时间:{:.2f}ms'.format((end-start)))
    return wrapper

def loop1(tname):
    print(tname+"循环loop1打印时间======" + time.ctime())
    time.sleep(1)

# @asyncio.coroutine
async def loop2(tname):# async等同于@asyncio.coroutine
    print(tname+"循环loop1打印时间======" + time.ctime())
    # yield from asyncio.sleep(1)
    await asyncio.sleep(1)  # 等同于yield from

@asyncio.coroutine
def loop3(tname):# async等同于@asyncio.coroutine
    print(tname+"循环loop1打印时间======" + time.ctime())
    yield from asyncio.sleep(1)
    # await asyncio.sleep(1)  # 等同于yield from

@tn
def main():
    print('多线程任务开始执行=====')
    threads = []#定义一个线程队列
    for i in range(5):
        t = threading.Thread(target=loop1, args=("thread"+str(i),))
        threads.append(t)
    for i in range(5):
        threads[i].start()
    for i in range(5):
        threads[i].join()

    #协程并发测试
    print('协程并发测试开始======')
    loop = asyncio.get_event_loop()# 获取一个event_loop
    #任务列表
    tasks = [
        asyncio.ensure_future(loop2('11111')),
        asyncio.ensure_future(loop2('22222')),
        asyncio.ensure_future(loop2('33333')),
        asyncio.ensure_future(loop3('44444')),#loop3
        asyncio.ensure_future(loop3('55555'))]#loop3
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
if __name__ == '__main__':
    main()

'''
上边这组代码稍稍有点乱，可能你需要认真的理下思绪，对比一下结果，你会发现虽然后边执行的代码没有利用多线程，但打印结果上的时间和多线程的执行结果是一样的。
这就是协程的魅力所在，一条线程搞定多线程任务。
'''