#codeing=utf-8
# @Time    : 2017-10-12
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python中创建TCP服务器与客户端进行通信
# @Url     : http://www.17python.com/blog/40
# @Details : Python中创建TCP服务器与客户端进行通信
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python中创建TCP服务器与客户端进行通信（上）
###################################

'''
## 前言
学习套接字编程最好的方法就是从实际应用的开发中边学边用，这样对TCP服务器及客户端通信中遇到的知识点才会更加了解。
开发一个拥有服务器并且可以处理多客户端的聊天室应用程序，服务器有一定的管理权限，比如：群发消息，管理客户端可以限制连接及断开客户端连接等。
客户端可以在聊天室里群聊，私聊。

好吧，为了保证这个小小的应用开发跨度不会太大，我们采用循序渐进的方式，从基础代码上迭代开发，这里会用到的知识点有：
+ `Python`的socket套接字模块
+ `Python`的多线程模块
+ `Python Tk GUI`模块，后边有可能考虑做成可视化的聊天室。

## socket模块
关于套接字网络编程的理论知识，这里就不在重复了，网上有很多，大家自己搜索一下好了。
要创建套接字，使用`Python socket.socket()`函数即可，他有一些固定的方式：

    s = socket(AF_INET, SOCK_STREAM)# 创建TCP/IP套接字对象

获得了套接字对象后，就可以使用套接字对象的方法进行交互了。

## `socket`中一些常用方法

服务器套接字方法：

+ `s.bind()`这个方法，绑定服务器的IP及端口
+ `s.listen(int)`监听，可以设置一个整数限制客户端的连接。
+ `s.accpt()`被动接受TCP客户端的连接（阻塞）

客户端套接字方法：

+ `s.connect()` 连接服务器

其它方法：

+ `s.recv()` 接收TCP消息
+ `s.send()` 发送TCP消息
+ `s.close()` 关闭套接字。

## 关于消息

发送和接收消息时需要进行编码和解码，这里使用`data.encode('utf-8')`和`data.decode()`保证通信消息的正常发送，如果不使用会报错。


好了，先来个简单的例子，下边是代码，建议代码运行的时候不要在IDE里运行，请在终端中运行。

## 服务器端

'''

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)# IP 端口

tcpSerSock = socket(AF_INET, SOCK_STREAM)# 创建TCP/IP套接字服务器
tcpSerSock.bind(ADDR)#绑定IP及端口
tcpSerSock.listen(5)

while True:
    print("等待客户端连接=======")
    tcpCliSock, addr = tcpSerSock.accept()#被动接受客户端连接
    print("客户端已连接=====")

    while True:
        data = tcpCliSock.recv(BUFSIZ)#接收客户端发来的数据
        print(data.decode())
        if 'exit' == data.decode():break
        data = "{0}".format(ctime())+" "+data.decode()
        tcpCliSock.send(data.encode('utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
'''
## 客户端

代码

就目前这个聊天室只是完成了通信的最基本功能，只能由客户端发送一条消息，服务器端自动回应消息。之后的继续都是建立在这个基础模型之上了。

## 半双工的聊天室

如果稍加修改，我们就可以使这个服务器和客户端进行一对一的聊天了。

+ 服务器端添加判断，如果客户端发来的数据有内容，就进行输入，然后把数据发送给客户端。
+ 客户端连接后，先进行消息的发送，然后就一直等待服务器的消息回送，然后循环。

现在的这个聊天系统缺点就是，必须等待另一方发来消息，才能回复消息，稍后我们继续改进。

相关代码如下：

## 半双工服务器

## 半双式的客户端





'''