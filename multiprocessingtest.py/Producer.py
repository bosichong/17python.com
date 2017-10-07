#codeing=utf-8
# @Time    : 2017-10.07
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python并发编程（下）功能强大设置简单的分布式多进程生产者与消费者模式
# @Url     : http://www.17python.com/blog/35
# @Details : Python并发编程（下）功能强大设置简单的分布式多进程生产者与消费者模式
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Producer 生产者
###################################
import random, time
from multiprocessing.managers import BaseManager

# 注册一个管理器，负责管理调度网上注册的Queue队列
class ProducerMagager(BaseManager):
    pass
#获取网络上的Queue 生产者，只关心生产需要计算的数据即可。
ProducerMagager.register('pq')
# 注册生产者服务器，address 真写IP及端口，authkey是一个密码，如果需要访问此处必须与服务器一致。
pm = ProducerMagager(address=('192.168.0.88',5678), authkey=b'www.17python.com')
pm.connect()#连接服务器
print('生产者服务器已经准备就绪！')
task = pm.pq()#获取生产者的队列
k = 1
#
while True:
    for i in range(10):
        r = random.randint(0,999)
        task.put(r)
    print("第{0}轮任务完毕！稍后继续！".format(k))
    k += 1
    time.sleep(3)


