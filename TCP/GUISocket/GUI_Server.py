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
"""
先这样吧，为了不耽误稍后的学习进程，这个聊天室先码到这里，不想继续填坑了。服务器端用TK实现了图形展示，客户端依然终端。具体如下图：

![]()

## Tk多线程中的坑

+ 在图形化后，主线程中开出一条线程，不要直接在主线程中进行通信，不然循环会卡死，专门处理创建socket线程的工作线程，记得self.t.setDaemon(True)#这里很重要，不加程序界面会卡死！
+ 客户端没有实现图形化，完全不知道怎么弄，只要一启动，窗口就会被线程卡死，暂时先终端吧。

## 多用户服务器端

每条连接都创建一个socket，这样每个线程处理自己的收发消息，但是这种架构如果在大量连接下会占用很大的系统资源，如果把socket放到一个容器里，然后使用生成器协程来轮循收发消息，
这样的话只需要一个线程即可，性能必会提高不少，这正是稍后要学习的任务，也是python中的难点。

关于服务器的命令及私聊功能，这些应该都是通过消息来判断，所以后续一定会把消息进行封装发送，一条消息中应该包括命令及消息正文，这样就可以通过命令来判断用户的需求了。

## 客户端


具体代码就不贴了，到git下载吧。

代码运行，请在终端中，不要在IDE中启动。代码运行，请在终端中，不要在IDE中启动。代码运行，请在终端中，不要在IDE中启动。





"""
import json
import socket
import sys
import threading
import time
import tkinter as tk

# 聊天协议常量

CHATCONTENT = 'chatcontent'  # 聊天内容
CHAT_EXIT = '|exit|'  # 退出聊天室
CHAT_USERS = 'chatusers'  # 聊天室用户列表
CHAT_REG_USERNAME = 'reg_username'  # 注册用昵称
CHAT_ONETOONE = 'onetoone' #私聊标识


class GuiServer:
    """
    聊天室服务器端GUI构建
    """

    def __init__(self):
        self.is_server_start = 0  # 服务器是否启动
        self.t = None

        self.root = tk.Tk()  # 整个服务器的窗口
        self.root.title("Python江湖大佬聊天室服务器管理器 1.0 By py_sky 学习交流群：217840699")
        self.info_frame = tk.Frame(self.root)  # 存放用户列表，聊天室交流信息部件
        self.info_frame.pack(fill=tk.X, side=tk.TOP)
        self.server_frame = tk.LabelFrame(
            self.root, text="聊天室设置", padx=5, pady=5)  # 存放聊天室服务器设置相关信息部件，服务器启动，暂停按钮。
        self.server_frame.pack(fill=tk.X, side=tk.TOP)

        # 用户列表框
        self.name_var = tk.StringVar()  # 绑定listbox的列表值
        self.lb = tk.Listbox(self.info_frame, listvariable=self.name_var, width=20, selectmode=tk.EXTENDED)
        self.lb.pack(fill=tk.Y, side=tk.LEFT)

        # 创建打印聊天信息的text
        self.ybar = tk.Scrollbar(self.info_frame)
        self.ybar.pack(fill=tk.Y, side=tk.RIGHT)
        # self.xbar = tk.Scrollbar(self.info_frame, orient=tk.HORIZONTAL)  # orient=tk.HORIZONTAL表示为坚向滚动
        # self.xbar.pack(fill=tk.X, side=tk.BOTTOM, )

        self.out = tk.Text(self.info_frame, width=80, font=("Symbol", 14), yscrollcommand=self.ybar.set, )
        insert_text(self.out,'欢迎光临Python江湖大佬聊天室！')
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
            self.top_server, text="启动服务器", width=18, command=self.server_start).pack(side=tk.LEFT)

        self.down_server = tk.Frame(self.server_frame, )
        self.down_server.pack(fill=tk.X, side=tk.BOTTOM)
        # 聊天窗口
        self.that_var = tk.StringVar()
        self.that_var.set('你好哈！！！！')
        self.that = tk.Entry(
            self.down_server, textvariable=self.that_var, width=40)
        self.that.pack(fill=tk.X, side=tk.LEFT)

        # 信息发送按钮
        self.end_btn = tk.Button(
            self.down_server, text="发送消息", width=18, command=self.sendmsg).pack(side=tk.LEFT)

        self.root.protocol('WM_DELETE_WINDOW', self.close_window)
        self.root.mainloop()

    def close_window(self):
        """

        窗口关闭，关闭所有连接
        :return:
        """
        print('窗口准备开始关闭************')
        if self.is_server_start:
            # 关闭所有客户端连接
            print('准备关闭的客户端连接')
            print(self.t.cs)

            if self.t.cs:
                for k, v in self.t.cs.items():
                    users_data = {'protocol': CHAT_USERS, 'data': []}
                    jsondata = json.dumps(users_data, ensure_ascii=False)
                    self.t.cs[k].send(jsondata.encode('utf-8'))
                    self.t.cs[k].close()
                    self.t.cts[k].stop_flag = True

            # 关闭当前服务器
            #
            # self.t.s.close()
            self.t.stop_flag = True
            self.root.destroy()
            print('服务器已关闭！——————————')
            sys.exit()

        else:
            self.root.destroy()
            print('程序退出，窗口关闭。')

    def server_start(self):
        """
        启动服务器
        """
        self.t = TcpServer(self.ip_var.get(), self.port_var.get(), self.name_var, self.out, )  # 创建一个聊天室服务器线程
        self.t.setDaemon(True)  # 这里很重要，不加程序界面会卡死！
        self.t.start()
        insert_text(self.out,'服务器开启————————————')
        print('服务器开启—————————————')
        self.is_server_start = 1

    def sendmsg(self):
        """
        这里发送消息，可以对消息进行判断
        """
        msg = '[都别装！我是管理员]说道：' + self.that.get()
        data = {'protocol': CHATCONTENT, 'data': msg}
        if self.t.cs:
            for k, v in self.t.cs.items():
                send_json(v, data)
        insert_text(self.out,msg)


# Tcp服务器
class TcpServer(threading.Thread):
    def __init__(self, addr, port, name_var, out, ):
        threading.Thread.__init__(self)
        self.cts = dict()  # 存放客户端线程的字典 //todo
        self.cs = dict()  # 存放接入的socket客户端 以客户端用户名保存为字典
        self.namelist = list()  # 存放tk.listbox中的用户名称列表
        self.addr = addr
        self.port = port
        self.name_var = name_var
        self.out = out  # 服务器信息打印框
        self.s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象。
        self.s.bind((self.addr, self.port))  # 绑定IP及端口
        # self.setDaemon(True)
        self.s.listen(5)  # 设置最大连接数，超过后排队

        self.stop_flag = False  # 结束标识

        # 线程的任务，如果未结束一直循环任务

    def run(self):
        # 循环判断是否有客户端接入
        while not self.stop_flag:
            print('进入TcpServer聊天室服务器线程--------')
            self.recieve_msg()

    # 线程中的主要任务

    def recieve_msg(self):
        if not self.stop_flag:
            csock, car = self.s.accept()
            print(csock, car)
            print('发现用户连接,启动用户昵称验证线程.')
            vnt = VerifyNameT(csock, car, self.cts, self.cs, self.name_var, self.namelist, self.out)
            vnt.setDaemon(True)
            vnt.start()
            print("当前有{}位用户在线。".format(len(threading.enumerate())))

    # 关闭服务器标识

    def stop(self):
        self.stop_flag = True


# 多线程验证用户登陆线程
class VerifyNameT(threading.Thread):
    def __init__(self, csock, car, cts, cs, name_var, namelist, out):
        threading.Thread.__init__(self)
        self.csock = csock
        self.car = car
        self.cs = cs
        self.cts = cts
        self.name_var = name_var
        self.namelist = namelist  # 在线列表
        self.out = out  # 服务器信息打印框

    def additem(self, name):
        self.namelist.append(name)
        self.name_var.set(self.namelist)

    def run(self):
        """


        :return:
        """
        while True:
            print('开始验证昵称')
            username_json = self.csock.recv(1024).decode()
            name = rece_json(username_json)['data']
            # 验证用户昵称是否存在
            if name in self.cs:
                err = '昵称已经存在'
                err_json = {'protocol': CHAT_REG_USERNAME, 'data': err}
                send_json(self.csock, err_json)
            else:
                print('新建一个客户端线程，并加入客户端字典中--------------------')
                # 加入客户端线程列表
                self.additem(name)
                self.cs[name] = self.csock
                sendlisttousers(self.cs, self.namelist)  # 发送所用用户列表给所有人
                print('发送所用用户列表给所有人-------------------')
                st = SocketThread(self.csock, self.car, self.cts, self.cs, self.name_var, self.namelist, self.out,
                                  name)  #
                st.setDaemon(True)
                self.cts[name] = st  # 存放连接线程
                st.start()
                time.sleep(1)
                msg = '%s 大步流星的走进了聊天室，牛逼哄哄的问道：哪个不服？出来一战！\n' % name
                data = {'protocol': CHATCONTENT, 'data': msg}
                for k in self.cs:  # 循环字典每个socket打印消息，这样每个客户端都会得到消息。
                    # 把消息发给每个客户端
                    print(name, k)
                    if name != k:
                        send_json(self.cs[k], data)
                insert_text(self.out,msg)
                print('昵称验证完毕！')
                break


# 多线程处理客户端，如果创建了一个socket连接就会创建一个线程来处理。
class SocketThread(threading.Thread):
    def __init__(self, csock, car, cts, cs, name_var, namelist, out, name):
        threading.Thread.__init__(self)
        self.csock = csock
        self.car = car
        self.cs = cs
        self.cts = cts
        self.name_var = name_var  # listbox 数据
        self.namelist = namelist  # 在线用户列表
        self.out = out  # 服务器信息打印框
        self.name = name
        self.stop_flag = False

    def run(self):
        while True:
            try:
                json_data = self.csock.recv(1024).decode()  # 接收消息
            except Exception:
                print('服务器已关闭！，连接已释放')
                # 这个目前还没有适合的解决方式，每次关闭服务器都会引发 socket.error: [Errno 9] Bad file descriptor
                # 暂时先抛出错误。

            print("接收到用户{}的消息:{}".format(self.name, json_data))
            data = rece_json(json_data)
            # 如果接收到退出消息,这里负责处理客户端退出，应该删除用户列表中的socket关闭掉
            if data['protocol'] == CHAT_EXIT:
                break
            if data['protocol'] == CHATCONTENT:  # 如果聊天内容
                insert_text(self.out,self.name + ':' + data['data'])
                jsondata = {'protocol': CHATCONTENT, 'data': self.name + ':' + data['data']}
                for k in self.cs:  # 循环字典每个socket，这样每个客户端都会得到消息。
                    # 把消息发给每个客户端
                    # print(self.name, k)
                    if self.name != k:
                        send_json(self.cs[k], jsondata)
        if not self.stop_flag:
            msg1 = '{}已经离开了聊天室'.format(self.name)
            msg2 = '您已经与服务器断开！'
            jsondata1 = {'protocol': CHATCONTENT, 'data': msg1}
            jsondata2 = {'protocol': CHATCONTENT, 'data': msg2}
            # 服务器聊天窗口打印
            insert_text(self.out,msg1)
            # 发送给除了发送消息的用
            for k in self.cs:
                if self.name != k:
                    send_json(self.cs[k], jsondata1)
                if self.name == k:
                    send_json(self.cs[k], jsondata2)
            self.cs.pop(self.name)
            print(self.cs)

            self.namelist.clear()  # 清空用户列表数据
            for n in self.cs.items():
                self.namelist.append(n[0])
            self.name_var.set(self.namelist)  # 重新加载用户列表
            sendlisttousers(self.cs, self.namelist)  # 发送所用用户列表给所有人
            print('发送所用用户列表给所有人-------------------')
            self.csock.close()


def insert_text(out, msg1):
    out.insert(tk.END, msg1 + '\n')
    out.see(tk.END)


def rece_json(data):
    """
    :param data: 收到的json数据
    :return:python对象
    """
    jsondata = json.loads(data)
    return jsondata


def send_json(s, msg):
    """
    发送json格式的消息到客户端
    :param s: socket
    :param msg: str 消息内容
    :return: bool
    """

    data = json.dumps(msg)
    # noinspection PyBroadException
    try:
        s.send(data.encode('utf-8'))
        return 1
    except Exception:
        print("此用户的连接已断开！")
        return 0


def sendlisttousers(cs, namelist):
    """
    发送所用用户列表给所有人
    :param cs: 所有用户的连接
    :param namelist: 用户列表
    :return:
    """
    users_data = {'protocol': CHAT_USERS, 'data': namelist}
    jsondata = json.dumps(users_data, ensure_ascii=False)
    print(jsondata, type(jsondata))
    for k in cs:
        cs[k].send(jsondata.encode('utf-8'))


if __name__ == '__main__':
    GuiServer()
