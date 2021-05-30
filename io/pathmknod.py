#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# @Time    : 2018-12-27
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python os.mknod 运行报错无法创建文件
# @Url     : http://www.17python.com/blog/95
# @Details : Python os.mknod 运行报错无法创建文件
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode

import os
file = os.path.join(os.path.dirname(__file__),'17python888.txt')
os.mknod(file)#运行到此处，就会报错

# 解开注释，用下边的方法试试
# with open(file, mode='a',encoding='utf-8') as f:
#     pass

'''
前几天因为要创建一个文件，但是osx下边却发生了错误，可以运行上边的代码试试

    os.mknod(file)#运行到此处，就会报错
    PermissionError: [Errno 1] Operation not permitted

这个错误是由于linux系统权限不够，这可真是一个坑。

那么怎么办?

网上查了一下，可以用`open()`方法，咱试试。

通过测试，使用`open()`方法`mode="a"`即可搞定文件的创建。

'''