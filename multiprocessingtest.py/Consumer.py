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
# Consumer 消费者
###################################
import time
from multiprocessing.managers import BaseManager

# 注册一个管理器，负责管理调度网上注册的Queue队列
class ConsumerMagager(BaseManager):
    pass

#获取网络上的Queue 消费者，需要获取任务，计算后发送任务。
ConsumerMagager.register('pq')
ConsumerMagager.register('cq')

m = ConsumerMagager(address=('192.168.0.88',5678),authkey=b'www.17python.com')
m.connect()#连接服务器
pq = m.pq()
cq = m.cq()
#开始计算任务
while True:
    if not pq.empty():#如果任务队列不为空
        n = pq.get(timeout=1)#如果超。
        print('收到计算任务{0}*{1}={2}'.format(n,n,n*n))
        cq.put('%d * %d = %d' %(n,n,n*n))
    else:
        time.sleep(1)
        print("好无聊，我在等待任务安排中")