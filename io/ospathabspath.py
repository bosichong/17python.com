#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-11-21
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python 
# @Url     : http://www.17python.com/blog/86
# @Details : Python os.path.dirname(__file__) 在终端命令行下报错
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.29.1
import os
###################################
# Python os.path.dirname(__file__) 在终端命令行下报错
###################################

"""
最近在写程序中用到了`os.path.dirname(__file__)`，在PyCharm中启动程序调试的时候，是没有问题的，但是如果在终端命令行下运行程序时就会报错


    FileNotFoundError: [Errno 2] No such file or directory

我们先来测试一下，看看报错是什么样的？
"""

print(os.path.dirname(__file__))

'''
如果在终端运行当前程序就会报错：

    >>> print(os.path.dirname(__file__))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'os' is not defined

如何使之正确运行呢？如果你用过`Django`，就会想到`BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`,
这个是`Django`里用来定义当前文件所属目录的一行代码，后来我查询了一下，其中`os.path.abspath(__file__)`这条是返回当前文件的绝对地址，
而`os.path.dirname(os.path.abspath(__file__))`就是返回当前文件所在的目录的绝对地址，这样我们就轻松的得到当前文件所属目录了。
困扰人生的小问题就这样绝对喽！
'''
