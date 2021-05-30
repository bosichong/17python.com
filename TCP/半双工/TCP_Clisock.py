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
HOST = '127.0.0.1'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST,PORT)
# 创建客户端，并连接服务器
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input("> ")
    tcpCliSock.send(data.encode('utf-8'))
    if 'exit' == data :break
    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if data:
            print(data)
            break
tcpCliSock.close()