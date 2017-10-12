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
# Python中创建TCP服务器与客户端进行通信
###################################

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 6666
BUFSIZ = 1024
ADDR = (HOST, PORT)# IP 端口

tcpSerSock = socket(AF_INET, SOCK_STREAM)# 创建TCP/IP套接字
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
        if data:
            data = input("> ")
            data = "{0}".format(ctime())+" "+data
            tcpCliSock.send(data.encode('utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
