#codeing=utf-8
# @Time    : 2017-12-24
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(10) filedialog 文件目录选择对话框
# @Url     : http://www.17python.com/blog/69
# @Details : Python TK和Tkinter的GUI编程(10) filedialog 文件目录选择对话框
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# Python TK和Tkinter的GUI编程(10) filedialog 文件目录选择对话框
###################################


'''

python中有没有文件目录选择对话框？答案是肯定的，这个可以有。tkinter.filedialog这个模块就是负责选择文件及目录的。

## tkinter.filedialog的测试

创建一个tk的窗口，包括一个文本框、按键及一个列表框，这些的创建都是很简单的，其中文本框及列表框中的关联数据我们采用tk中特有的绑定数据模式，具体可以查看代码。
测试代码中有一个是按键回调方法filedir，主要是用来弹出目录选择对话框的,filedialog中有很多比较用用的对话框：


    'askdirectory',
    'askopenfile',
    'askopenfilename',
    'askopenfilenames',
    'askopenfiles',
    'asksaveasfile',
    'asksaveasfilename'

以上是通过print(dir(filedialog))打印查看到的，也可以通过源码查看到，通过单词字面应该大体上可以了解到这些函数弹出的对话框是干什么用的。

好了，具体测试源码如下：

'''


import tkinter.filedialog as filedialog
from tkinter import *
import os

def filedir():
    print('按键已被点击')
    v.set('')#清空文本框里内容
    var.set((('')))
    path = filedialog.askdirectory()
    print(dir(filedialog))
    if path :
        v.set(path)
    getdir(path)

def getdir(p):
    #把目录中遍历出来的文件目录显示到列表框中
    fp = os.listdir(p)
    var.set(fp)

root = Tk()
root.title('文件目录选择对话框测试')
frame = Frame(root)
frame.pack(fill=X,side=TOP)
#加入一个文本框显示目录地址
v = StringVar()#绑定文本框的变量
ent = Entry(frame, width=50,textvariable = v).pack(fill=X,side=LEFT)
#加入一个按键，点击后弹出文件目录选择对话框
button = Button(frame, text='选择文件夹', command=filedir).pack(fill=X,side= LEFT)
#加入一个列表框，显示目录中的文件列表
listframe = Frame(root)
listframe.pack(fill=X,side=LEFT)
var = StringVar()#绑定listbox的列表值
var.set((''))
listbox = Listbox(listframe,width=60,listvariable = var).pack()
root.mainloop()