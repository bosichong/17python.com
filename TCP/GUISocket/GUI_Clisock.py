#codeing=utf-8
# @Time    : 2017-10-12
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python中创建TCP服务器与客户端进行通信(中)Tk、thread与socket组合。
# @Url     : http://www.17python.com/blog/40
# @Details : Python中创建TCP服务器与客户端进行通信(中)Tk、thread与socket组合。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python中创建TCP服务器与客户端进行通信(中)Tk、thread与socket组合。
###################################
#coding=utf-8
import threading, socket, time
import tkinter as tk


class TcpClient(threading.Thread):
    def __init__(self, addr, port):
        threading.Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.addr, self.port))
        self.stop_flag = False
        self.name = ''

    def run(self):
        self.sendName()#发送昵称验证
        t1 = threading.Thread(target=self.recvMsgThread)
        t2 = threading.Thread(target=self.sendMsgThread)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

#发送客户端用户名，保存在服务器端列表中
    def sendName(self):

        while True:
            self.name = input('请输出昵称：')
            self.s.send(self.name.encode())  # 发送到服务器
            msg = self.s.recv(1024)
            if msg.decode('utf-8') == '用户名已经存在':
                print(msg.decode('utf-8'),'请重新输入昵称！')
            else:
                break



    # 发送消息线程方法
    def sendMsgThread(self):
        print('发消息线程启动------------', self.stop_flag)
        while not self.stop_flag:
            data = input('>>>')
            if data == 'exit':#输入exit退出客户端
                msg = self.name + '好象有什么急事！一路小跑的离开了聊天室'
                self.s.send(msg.encode())
                time.sleep(1)
                self.stop()  # 中止线程
                print('发消息线程已关闭')
                
            elif data:
                data = '[{0}]说道：{1}'.format(self.name,data)
                self.s.send(data.encode())


    # 接收消息线程方法
    def recvMsgThread(self):
        print('收消息线程启动-------------', self.stop_flag)
        while not self.stop_flag:
            try:
                msg = self.s.recv(1024)
                if msg: print(msg.decode())

            except Exception as e:
                print('收消息线程已关闭')

    def stop(self):
        self.s.close()
        self.stop_flag = True


def main():
    ip = '192.168.0.88'
    port = 18888
    t3 = TcpClient(ip, port)
    print('正在进入聊天室，请先起个牛逼的名字！')
    t3.start()
    t3.join()


if __name__ == '__main__':
    main()
    print('客户端退出')

