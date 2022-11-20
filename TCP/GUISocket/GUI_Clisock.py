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
import json
import random
import socket
import sys
import threading
import tkinter as tk
from tkinter import messagebox  # 导入提示窗口包

CHATCONTENT = 'chatcontent'  # 聊天内容
CHAT_EXIT = '|exit|'  # 退出聊天室
CHAT_USERS = 'chatusers'  # 聊天室用户列表
CHAT_REG_USERNAME = 'reg_username'  # 注册用昵称
CHAT_ONETOONE = 'onetoone' #私聊标识


class Gui_Client:
    '''
    聊天室客户端GUI构建
    '''

    def __init__(self):
        self.clist = {}  # 存放接入的socket客户端 以客户端用户名保存为字典
        self.namelist = list()  # 存放tk.listbox中的用户名称列表
        self.t = 0
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
        self.name_var = tk.StringVar()  # 绑定listbox的列表值
        self.lb = tk.Listbox(self.info_frame, listvariable=self.name_var, width=20, selectmode=tk.EXTENDED)
        self.lb.bind('<ButtonRelease-1>', self.onetoonethat)  # 绑定鼠标左键点击事件。
        self.lb.pack(fill=tk.Y, side=tk.LEFT)

        # test 测试列表用
        self.name_var.set(('aa', 'bb', 'cc', 'dd', 'ee'))

        # 创建打印聊天信息的text
        # 分别创建一个横向，一个坚向的滚动条，
        self.ybar = tk.Scrollbar(self.info_frame)
        self.ybar.pack(fill=tk.Y, side=tk.RIGHT)
        # self.xbar = tk.Scrollbar(self.info_frame, orient=tk.HORIZONTAL)  # orient=tk.HORIZONTAL表示为坚向滚动
        # self.xbar.pack(fill=tk.X, side=tk.BOTTOM, )

        self.out = tk.Text(self.info_frame, width=80, font=("Symbol", 14), yscrollcommand=self.ybar.set, )
        insert_text(self.out,'欢迎光临Python江湖聊天室！')
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

        self.root.protocol('WM_DELETE_WINDOW', self.close_window)
        self.root.mainloop()

    def close_window(self):
        """
        窗口关闭，关闭所有连接
        :return:
        """
        print('窗口准备开始关闭************')
        if self.t:
            data = {'protocol': CHAT_EXIT, 'data': '|exit|'}
            data1 = json.dumps(data)
            try:
                self.t.s.send(data1.encode('utf-8'))
                self.root.destroy()
            except:
                self.root.destroy()
                sys.exit()
            # if self.t.send_json(data):
            #     print('已发送退出聊天室的申请')
            # else:
            #     print("提示", "请先连接服务器再尝试聊天.")
            # self.root.destroy()
        else:
            self.root.destroy()

    def client_Start(self):
        '''
        启动客户端
        '''

        try:
            self.t = TcpClient(self.ip_var.get(), self.port_var.get(), self.name_var, self.namelist, self.out,
                               self.clist, getName())
            self.t.setDaemon(True)  # 这里很重要，不加程序界面会卡死！
            self.t.start()
            insert_text(self.out,"线程开始————————————\n")
            print('线程开始————————————')
        except Exception as e:
            messagebox.showinfo("提示", "服务器没有开启或无法连接!")
            print(e, '服务器没有开启或无法连接')

    def sendMsg(self):
        '''
        这里发送消息，可以对消息进行判断
        '''
        msg = self.that.get()  # 获取聊天窗口里的消息
        # //todo 私聊判断
        data = {'protocol': CHATCONTENT, 'data': msg}
        if self.t:
            if self.t.send_json(data):
                insert_text(self.out,msg)
            else:
                print("提示", "请先连接服务器再尝试聊天.")
        else:
            messagebox.showinfo("提示", "请先连接服务器再尝试聊天.")
            print("提示", "请先连接服务器再尝试聊天.")

    def onetoonethat(self,event):
        items = self.lb.curselection()
        for k in items:
            print(self.lb.get(k))
            firstmsg = '@'+self.lb.get(k)+' ' #私聊标识 @昵称+空格
            msg = '你好，可以私聊一会吗？'
            self.that_var.set(firstmsg+msg)


class TcpClient(threading.Thread):
    def __init__(self, addr, port, name_var, namelist, out, clist, name):
        threading.Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.name_var = name_var
        self.namelist = namelist  # 在线列表
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
                msg = self.rece_json(self.s.recv(1024).decode())
                print(type(msg))
                if msg['protocol'] == CHAT_EXIT:  # 退出断开连接
                    insert_text(self.out,msg)
                    break
                if msg['protocol'] == CHAT_USERS:  # 接收新的用户列表
                    print('接收用户列表')
                    self.namelist.clear()
                    self.namelist = msg['data']
                    self.name_var.set(self.namelist)
                    print('保存用户列表成功')
                if msg['protocol'] == CHATCONTENT:  # 接收聊天内容
                    insert_text(self.out,msg['data'])
                    print('接收服务器的消息：', msg['data'])
            except Exception as e:
                print('收消息线程已关闭', e)
                break
        msg = '服务器已断开，或是您已退出聊天室。'
        insert_text(self.out,msg)
        self.stop()

    def isNameOk(self):
        '''
        用户昵称验证方法
        '''
        # 发送昵称到服务器
        print('验证昵称')
        while True:
            if self.isOk:
                usernamedata = {'protocol': CHAT_REG_USERNAME, 'data': self.name}
                self.send_json(usernamedata)  # 发送昵称到服务器验证
                self.isOk = 0

            tempjson = self.rece_json(self.s.recv(1024))
            if tempjson['protocol'] == CHAT_REG_USERNAME:  # 昵称正常的话跳出昵称验证的循环,开始正常接收消息
                self.name = getName()
                self.isOk = 1
                print('验证昵称失败，重新发送了新昵称验证')
            elif tempjson['protocol'] == CHAT_USERS:  # 接收用户列表并展示
                print('接收用户列表')
                self.namelist.clear()
                self.namelist = tempjson['data']
                self.name_var.set(self.namelist)
                print('验证昵称成功，保存用户列表成功')
                break

    def send_json(self, msg):
        '''
        发送json格式的消息到服务器
        :param msg: str 消息内容
        :return: bool
        '''

        data = json.dumps(msg)
        try:
            self.s.send(data.encode('utf-8'))
            return 1
        except:
            messagebox.showinfo("提示", "请先连接服务器再尝试聊天.")
            return 0

    def rece_json(self, data):
        '''
        :param data: 收到的json数据
        :return:python对象
        '''
        jsondata = json.loads(data)
        print(jsondata, type(jsondata))
        return jsondata

    def stop(self):
        self.s.close()
        self.stop_flag = True


def insert_text(out, msg):
    '''
    添加聊天记录到text部件。
    :param msg: str
    :return:
    '''
    out.insert(tk.END, msg + '\n')
    out.see(tk.END)


def main():
    Gui_Client()


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
