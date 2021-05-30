#codeing=utf-8
# @Time    : 2017-09-27
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python tk Checkbutton、Radiobutton和LabelFrame的使用。
# @Url     : http://www.17python.com/blog/26
# @Details : Python tk Checkbutton、Radiobutton和LabelFrame的使用。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python tk Checkbutton、Radiobutton和LabelFrame的使用。
###################################
'''
Checkbutton和Radiobutton单选和多选按钮在GUI编程中是经常使用的选项选择方法，tk提供的单选与多选按钮功能虽然简约，但功能上也是足够应付日常应用了。

## Checkbutton

多选按钮，因为是选择按钮，所以我们需要判断当这个按钮被点击后，应该属于选择状态，然后根据状态的选择状态返回值进行相关操作。
`variable`是多选按钮的一个属性，这个属性的值用来显示当前多选择按钮的状态，1时为选中，2时为释放。
`select() deselect() toggle()`这三个方法用来切换多选择按钮的选择状态。

## Radiobutton
单选选按钮一般都是二个以上成组显示，一般最需要的就是获取单选按钮的返回值，tk中先设置一组包括属性及显示字符串的list，然后用for循环来创建多选按钮。
`variable=v, value=mode,`这二个属性配合使用，当使用`get()`方法返回值的时候，返回的是value上的这个值（这里的原因我也没明白，希望高人指点一下。），所以设置单选按钮值的时候，记得设置value。

## LabelFrame 

LabelFrame 是一个带线的部件容器，具体效果请看下边的截图：







'''


import tkinter as tk

def cdef():
    if var.get():
        strvar.set("看，我改变了！")
    else:
        strvar.set("有种你点我试试")

def rdoprt():
    print(v.get())
    r_frame['bg']=v.get()

root = tk.Tk()
root.title("Checkbutton和Radiobutton")

c_frame = tk.LabelFrame(root,text="Checkbutton", padx=5, pady=5)
c_frame.pack(fill=tk.X, side=tk.TOP)

var = tk.IntVar()
strvar = tk.StringVar()
strvar.set("有种你点我试试")
cbt = tk.Checkbutton(c_frame,textvariable=strvar, variable = var,command= cdef,)
# cbt.select()#选中
# print(var.get())
# cbt.deselect()#取消选中
# print(var.get())
# cbt.toggle()#切换选中开关
# print(var.get())
cbt.pack(side=tk.LEFT)
cbt1 = tk.Checkbutton(c_frame,text="Checkbutton", variable = var, command=cdef)
cbt1.pack(side=tk.LEFT)

r_frame = tk.LabelFrame(root,text="Radiobutton", padx=5, pady=5)
r_frame.pack(fill=tk.X, side=tk.TOP)
v = tk.StringVar()
v.set("L") # initialize
MODES = [
        ("#c00", "#c00"),
        ("#fff", "#fff"),
        ("#000", "#000"),
        ("#ccc", "#ccc"),
    ]

for text, mode in MODES:
        b = tk.Radiobutton(r_frame, text=text,variable=v, value=mode,command=rdoprt)
        b.pack(anchor=tk.W)


# comvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
# comboxlist = ttk.Combobox(c_frame, textvariable=comvalue,state='readonly')  # 初始化
# comboxlist["values"] = ("加法", "减法", "乘法", "除法")
# comboxlist.current(0)  # 选择第一个
# comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
# comboxlist.pack()
# print(comboxlist.get())



root.mainloop()

