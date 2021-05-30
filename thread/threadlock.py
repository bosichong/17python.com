#codeing=utf-8
# @Time    : 2017-10.04
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python多线程编程（2）多线程锁 threading.Lock
# @Url     : http://www.17python.com/blog/33
# @Details : Python多线程编程（2）多线程锁 threading.Lock
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python多线程编程（2）多线程锁 threading.Lock
###################################

'''
在多线程任务中，线程对数据的操作是随机的，这个先后次序无法预测，如果利用多线程修改唯一数据，由于对数据操作的随机性，必会影响到数据结果的准确性，所以在多线程的任务的编码中，我们必须使用线程锁。

## Python的多线程锁 threading.Lock

通过下边的例子，我们来看看多线程锁的重要性，定义两个数据，同时利用多线程对其+ -相同的数值，
如果操作次序是正常的，一加一减，那个数据应该是没有变化的，但是因为多线程操作没有加锁时对数据的操作是随机争抢资源的，
多线程操作时会发生，多加或是多减的结果，我们看下边的例子：
'''
import threading

data = 0
lock_data = 0
lock = threading.Lock()#创建一把线程锁

lock.acquire()
lock.release()

def change_d(n):
    '''修改无锁数据的函数'''
    global data
    data += n
    data -= n

def change_l_d(n):
    '''修改有锁数据的函数'''
    global lock_data
    lock_data += n
    lock_data -= n

def myfun(n):
    for i in range(500000):
        change_d(n)
        #lock.acquire()
        #change_l_d(n)
        #lock.release()
        #与下边的with语句处相同
        with lock:
            change_l_d(n)

def main():
    threads = []
    k = 5
    for i in range(k):
        t = threading.Thread(target=myfun, args=(10,))
        threads.append(t)
    for i in range(k):
        threads[i].start()
    for i in range(k):
        threads[i].join()
    print("无锁数据最终结果=={0}".format(data))
    print("有锁数据最终结果=={0}".format(lock_data))

if __name__ == '__main__':
    main()

'''
多次运行后我们会发现，无锁数据的最终结果会出现不同，因为可以证明，无锁的时候多线程操作是随机性的。
所以在多线程操作中，如果存在多线程操作唯一数据时，一定要加锁保证每次只有一个线程对基进行操作。

除了对多唯一数据进行加锁这种方法以外，在`Python`中还可以使用信号量或是事件对线程进行控制，但笔者认为，还是使用Lock对象比较方便。


'''