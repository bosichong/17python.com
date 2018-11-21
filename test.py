#codeing=utf-8
# @Time    : 2017-09-01
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python3学习
# @Url     : http://www.17python.com/
# @Details : python3学习中的一些记录与心得
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
# print(len('你好'))

from PIL import Image, ImageFilter

class HelloWorld:
    def __init__(self):
        print('hello world')

HelloWorld()

k = 0

for i in range(100):
    for i in range(5):
        print(k+i)
    k = k+1
    print()

