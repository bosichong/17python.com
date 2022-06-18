# codeing=utf-8
# @Time    : 2017-10-12
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python中创建TCP服务器与客户端进行通信(中)Tk、thread与socket组合。
# @Url     : http://www.17python.com/blog/41
# @Details : Python中创建TCP服务器与客户端进行通信(中)Tk、thread与socket组合。
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python中创建TCP服务器与客户端进行通信(中)Tk、thread与socket组合。
###################################
# coding=utf-8
import random
import socket
import threading
import tkinter as tk
from tkinter import messagebox  # 导入提示窗口包


class Gui_Client:
    '''
    聊天室客户端GUI构建
    '''

    def __init__(self):
        self.clist = {}  # 存放接入的socket客户端 以客户端用户名保存为字典
        self.go()

    def go(self):
        '''
        构建GUI
        '''
        self.root = tk.Tk()  # 整个窗口
        self.root.title("欢迎光临Python江湖大佬聊天室客户端 1.0 By py_sky 学习交流群：217840699")
        self.info_frame = tk.Frame(self.root)  # 存放用户列表，聊天室交流信息部件
        self.info_frame.pack(fill=tk.X, side=tk.TOP)
        self.server_frame = tk.LabelFrame(
            self.root, text="聊天室设置", padx=5, pady=5)  # 存放聊天室服务器设置相关信息部件，服务器启动，暂停按钮。
        self.server_frame.pack(fill=tk.X, side=tk.TOP)

        # 用户列表框
        self.lb = tk.Listbox(self.info_frame, width=20, selectmode=tk.EXTENDED)
        self.lb.pack(fill=tk.Y, side=tk.LEFT)

        # 创建打印聊天信息的text
        self.out = tk.Text(self.info_frame, width=80, font=("Symbol", 14))
        self.out.insert(tk.END, "欢迎光临Python江湖聊天室！ \n")
        self.out.pack(fill=tk.Y, side=tk.LEFT)

        self.top_server = tk.Frame(self.server_frame, )
        self.top_server.pack(fill=tk.X, side=tk.TOP)

        # 设置IP文本框
        self.ip_var = tk.StringVar()
        self.ip_var.set('192.168.0.88')
        self.ip_entry = tk.Entry(
            self.top_server, textvariable=self.ip_var, width=12)
        self.ip_entry.pack(fill=tk.X, side=tk.LEFT)
        # 设置端口文本框
        self.port_var = tk.IntVar()
        self.port_var.set(18888)
        self.port_entry = tk.Entry(
            self.top_server, textvariable=self.port_var, width=5)
        self.port_entry.pack(side=tk.LEFT)

        self.start_btn = tk.Button(
            self.top_server, text="连接服务器", width=18, command=self.client_Start).pack(side=tk.LEFT)

        self.down_server = tk.Frame(self.server_frame, )
        self.down_server.pack(fill=tk.X, side=tk.BOTTOM)
        # 聊天窗口
        self.that_var = tk.StringVar()
        self.that_var.set('拜见各位python江湖大佬!')
        self.that = tk.Entry(
            self.down_server, textvariable=self.that_var, width=40)
        self.that.pack(fill=tk.X, side=tk.LEFT)

        # 信息发送按钮
        self.end_btn = tk.Button(
            self.down_server, text="发送消息", width=18, command=self.sendMsg).pack(side=tk.LEFT)

        self.root.mainloop()

        self.t = 0

    def client_Start(self):
        '''
        启动客户端
        '''

        try:
            self.t = TcpClient(self.ip_var.get(), self.port_var.get(), self.lb, self.out, self.clist, getName())
            self.t.setDaemon(True)  # 这里很重要，不加程序界面会卡死！
            self.t.start()
            self.out.insert(tk.END, "线程开始————————————\n")
            print('线程开始————————————')
        except Exception as e:
            messagebox.showinfo("提示", "服务器没有开启或无法连接!")
            print(e, '服务器没有开启或无法连接')

    def sendMsg(self):
        '''
        这里发送消息，可以对消息进行判断
        '''
        try:
            msg = self.t.name + ':' + self.that.get()  # 获取聊天窗口里的消息
            self.t.s.send(msg.encode('utf-8'))
            self.out.insert(tk.END, msg + '\n')  # 聊天窗口里添加本次聊天的内容
        except:
            messagebox.showinfo("提示", "请先连接服务器再尝试聊天.")


class TcpClient(threading.Thread):
    def __init__(self, addr, port, lb, out, clist, name):
        threading.Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.lb = lb
        self.out = out
        self.clist = clist
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.addr, self.port))
        self.stop_flag = False
        self.name = name
        self.msgdata = ''
        self.isOk = 1

    def run(self):
        self.inThat()  # 进入聊天室

    # 发送客户端用户名，保存在服务器端列表中
    # 此处还有修改昵称等功能,若昵称相同服务器则会返回一个新昵称,然后用户自己可以再次修改
    def inThat(self):
        while not self.stop_flag:
            if self.isOk:
                self.isNameOk()

            try:
                msg = self.s.recv(1024)
                if msg:
                    self.out.insert(tk.END, msg.decode() + '\n')
            except Exception as e:
                print('收消息线程已关闭')

    def isNameOk(self):
        '''
        用户昵称验证方法
        '''
        # 发送昵称到服务器
        print('验证昵称')
        while True:
            if self.isOk:
                self.s.send(self.name.encode('utf-8'))  # 发送到服务器
                self.isOk = 0

            name_msg = self.s.recv(1024)
            if name_msg == '昵称已经存在':  # 昵称正常的话跳出昵称验证的循环,开始正常接收消息
                self.name = getName()
                self.isOk = 1
                print('验证昵称失败，重新发送了新昵称验证')
            else:
                print('验证昵称成功')
                break

    # # 发送消息线程方法
    # def sendMsgThread(self):
    #     print('发消息线程启动------------', self.stop_flag)
    #     while not self.stop_flag:
    #         # if self.msgdata == 'exit':#输入exit退出客户端
    #         #     msg = self.name + '好象有什么急事！一路小跑的离开了聊天室'
    #         #     self.s.send(msg.encode('utf-8'))
    #         #     self.out.insert(tk.END,msg + '\n')
    #         #     time.sleep(1)
    #         #     self.stop()  # 中止线程
    #         #     print('发消息线程已关闭')
    #         #     sys.exit()

    #         if self.msgdata:
    #             tempdata = '[{0}]说道：{1}'.format(self.name,self.msgdata)
    #             self.s.send(tempdata.encode('utf-8'))
    #             self.out.insert(tk.END,tempdata + '\n')

    # # 接收消息线程方法
    # def recvMsgThread(self):
    #     print('收消息线程启动-------------', self.stop_flag)
    #     while not self.stop_flag:
    #         try:
    #             msg = self.s.recv(1024)
    #             if msg:
    #                 self.out.insert(tk.END, msg.decode()+'\n')

    #         except Exception as e:
    #             print('收消息线程已关闭')

    def stop(self):
        self.s.close()
        self.stop_flag = True


def main():
    c = Gui_Client()


def getName():
    '''
    生成聊天室的昵称
    '''
    n = 'python大佬'
    id = random.randint(999, 9999)
    name = n + str(id)
    return name


if __name__ == '__main__':
    main()
