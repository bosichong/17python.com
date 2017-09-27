#codeing=utf-8
# @Time    : 2017-09-26
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(7) Scrollbar
# @Url     : http://www.17python.com/blog/27
# @Details : Python TK和Tkinter的GUI编程(7) Scrollbar
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python TK和Tkinter的GUI编程(7) Scrollbar
###################################
"""
## Scrollbar

Scrollbar就是窗口中的滚动条，一般应用在文本框和列表框的外围，如果内容显示超出范围之外，就会显示滚动条。

## 创建及使用

+ 创建Scrollbar对象，通过orient设置他的滚动方向，HORIZONTAL or VERTICAL. 默认是VERTICAL。
+ 在部件中指定滚动条部件`yscrollcommand=ybar.set,xscrollcommand=xbar`
+ `ybar.config(command=t.yview) xbar.config(command=t.xview)` 设置滚动条事件，使滚动条交互起来。

"""

import tkinter as tk

root = tk.Tk()
root.title("Scrollbar 测试")
#分别创建一个横向，一个坚向的滚动条，
ybar = tk.Scrollbar(root)
ybar.pack(fill=tk.Y, side=tk.RIGHT)
xbar = tk.Scrollbar(root,orient=tk.HORIZONTAL)#orient=tk.HORIZONTAL表示为坚向滚动
xbar.pack(fill=tk.X, side=tk.BOTTOM,)
# 创建文本框，并设置横向及坚向的滚动条，wrap='none'表示文本不换
t = tk.Text(root,yscrollcommand=ybar.set,xscrollcommand=xbar.set, wrap='none')
t.pack(fill=tk.BOTH)
# 添加一些字符串
s = ""
for i in range(100):
    for j in range(100):
        s = s+str(i)+" "
    s = s+"\n"
t.insert(tk.END,s)
#为滚动条添加对应的函数，添加后，滚动条才会有效滚动
ybar.config(command=t.yview)
xbar.config(command=t.xview)

root.mainloop()