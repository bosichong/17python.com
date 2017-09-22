#codeing=utf-8
# @Time    : 2017-09-20
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python random 随机数模块操作总结
# @Url     : http://www.17python.com/blog/20#
# @Details : Python random 随机数模块操作总结
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python TK和Tkinter的GUI编程
###################################
import tkinter #导入支持库


def callback():
    """一个简单的回调测试"""
    print ("called the callback!")

root = tkinter.Tk()#创建一个root窗口
root.title('我只是一个测试的窗口')#设置窗口标题
root.geometry('500x300+300+300')#设置窗口的大小及位置
m_frame = tkinter.Frame(root)
m_frame.pack(fill=tkinter.X, side=tkinter.TOP)

# 创建菜单
menu = tkinter.Menu(root)
root.config(menu=menu)
filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

root.mainloop() 

