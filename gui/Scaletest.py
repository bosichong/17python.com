#codeing=utf-8
# @Time    : 2017-09-28
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(8) Scalet和Spinbox的简单使用
# @Url     : http://www.17python.com/blog/28
# @Details : Python TK和Tkinter的GUI编程(8) Scalet和Spinbox的简单使用
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
# print(len('你好'))
###################################
# Python TK和Tkinter的GUI编程(8) Scalet和Spinbox的简单使用
###################################

'''
Scalet和Spinbox 是tk中用来调节刻度的小部件。

## Scalet 滑动模块部件

Scalet 在使用中有几个必要的地方：

+ 设置刻度，`from_=0, to=1000,`还可以`from_=0, to=10,resolution=0.1`,设置每次调结刻度值
+ 滑块滑动事件，当滑动时，返回当前的刻度，有二种方法，无论哪种方法，需要先绑定回调函数`command=prtsa`
+ 取回当前刻度值，回调函数包括一个text字符串参数，通过这个参数可以直接返回当前的刻度值，另外还可以通过绑定变量来返回刻度值。

## Spinbox 

+ 绑定回调函数，然后通过`get()`方法返部件当前值。

'''
import tkinter as tk

def prtsa(text):
    print("v text="+text)
    print("v="+v.get())
def prtsp():
    print("v1="+sp.get())
root = tk.Tk()
root.geometry('500x300+300+300')#设置窗口的大小及位置
root.title("Scale的使用示例。。。")
#创建scale及绑定变量
v = tk.StringVar()
sa = tk.Scale(root,from_=0, to=1000,orient=tk.HORIZONTAL, command=prtsa, variable=v, label='刻度选择:')
sa.pack(fill=tk.X)
# 创建spinbox及绑定变量
sp = tk.Spinbox(root, from_=0, to=100, command=prtsp,)
sp.pack()


root .mainloop()