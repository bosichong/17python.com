# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :json_test.py
@time     :2022/06/19

"""

import json

d = {'one':1,'two':2,'hello':'world'}
print(type(d))
l = [1,2,3,4,5,6]

data = json.dumps(d)
data1 = json.dumps(l)

print(data,type(data))
print(data1)

j = json.loads(data)
j1 = json.loads(data1)


print(data,type(j))
print(data1)