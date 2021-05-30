#codeing=utf-8
# @Time    : 2017-12-22
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # Python生成器yield应用实例——监控日志
# @Url     : http://www.17python.com/blog/68
# @Details : # Python生成器yield应用实例——监控日志
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# Python生成器yield应用实例——监控日志
###################################

'''
Python生成器yield是编写基于处理管道，流或数据流程序的一种极其强大的方式，在《Python参考手册》中有一则实例非常简单实用，略加修改，分享一下给大家。

## 需要分析

假设服务器有一个日志文件，每隔一秒都会更新日志的内容，日志每行中都有一组类似：2017-12-21 14:07:26.471691 99123数据被写入日志。
我们的目的是分析日志中的数字如果大于5000就要打印出来。
这样来看，我们需要一个程序负责模拟日志写入，另一个程序负责分析日志打印数据。

## 模拟日志写入

'''

import random
from datetime import *
import os
import time


def server_log():
    # 生成模拟的日志数据
    server_int = random.randint(1,99999)#生成需要的随机数
    server_date = datetime.now()#获取当前系统时间
    return str(server_date) + ' ' + str(server_int)#拼装日志字符串


while True:
    #模拟系统写入日志
    #打开日志文件并写入日志
    with open(os.path.join(os.path.dirname(__file__),'server_log.log'),'at') as f :
        s = server_log()
        print(s)
        f.write(s + '\n')
    time.sleep(1)

'''
上边的代码我已经添加了相关的注释，这样我们就有了一个日志文件，每秒会有一第记录插入到日志中。

## 利用生成器yield解析日志

生成器可以返回一个迭代的流式的对象，我们可以通过这种方式便捷的获得相关数据，而且代码也更清晰易懂

tail.py 代码如下：


我们运行两个文件看下效果：


![]()

代码虽然简单，但值得细细品味，感受python的简约与强大吧。
'''