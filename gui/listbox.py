#codeing=utf-8
# @Time    : 2017-09-23
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(3) 列表框 Listbox
# @Url     : http://www.17python.com/blog/23
# @Details : Python TK和Tkinter的GUI编程(3) 列表框 Listbox
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
# print(len('你好'))
###################################
# Python TK和Tkinter的GUI编程(3) Listbox
###################################
import tkinter as tk


'''
## listbox 列表框
列表框的日常使用的场景：
+ 获取列表项中的内容lb.curselection()
+ selectmode=tk.EXTENDED 这个属性设置listbox可以选择多个选项
+ 添加列表项 lb.insert(tk.END,v.get()) END代表最后一个位置，第二个参数是要添加的字符串值。
+ 删除列表中选中的项 command = lambda lb=lb:lb.delete(tk.ANCHOR)
+ lb.bind() 用来绑定列表的事件，比如删除列表中选中的项。


'''

root = tk.Tk()
root.title("Listbox 测试。")
# 存放list的容器
list_frame = tk.Frame(root)
list_frame.pack(fill=tk.X, side=tk.TOP)
#存放按钮文本框的容器
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, side=tk.TOP)
# 获取当前listbox中item值，并在控制台打印值
def print_item(event):
    items = lb.curselection()
    for k in items:
        print(lb.get(k))
var = tk.StringVar()#绑定listbox的列表值
var.set(('aa','bb','cc','dd','ee'))
lb = tk.Listbox(list_frame, listvariable = var, selectmode=tk.EXTENDED)#创建一个listbox
lb.bind('<ButtonRelease-1>',print_item)#绑定鼠标左键点击事件。
lb.pack(fill=tk.X)
# 添加listbox item的方法
def additem():
    lb.insert(tk.END,v.get())
    v.set('')
v = tk.StringVar()#绑定文本框的变量
en = tk.Entry(button_frame, textvariable = v).pack()
b1 = tk.Button(button_frame, text="添加", command=additem).pack(side=tk.LEFT)#添加一个item
b2 = tk.Button(button_frame, text="删除", command= lambda lb=lb:lb.delete(tk.ANCHOR)).pack(side=tk.LEFT)#删除一个listbox中选中的item
root.mainloop()

