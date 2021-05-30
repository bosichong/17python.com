#codeing=utf-8
# @Time    : 2017-09-28
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(9) Event 键盘鼠标事件
# @Url     : http://www.17python.com/blog/29
# @Details : Python TK和Tkinter的GUI编程(9) Event 键盘鼠标事件
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python TK和Tkinter的GUI编程(9) Event 键盘鼠标事件
###################################


'''
## Event鼠标事件

+ <Button-1>：鼠标左击事件  
+ <Button-2>：鼠标右击事件  
+ <Button-3>：鼠标中击事件  
+ <Double-Button-1>：双击事件  
+ <Triple-Button-1>：三击事件  
+ <Bx-Motion>：鼠标移动事件,x=[1,2,3]分别表示左、中、右鼠标操作。  
+ <ButtonRelease-x>鼠标释放事件,x=[1,2,3],分别表示鼠标的左、中、右键操作  
+ <Leave>：鼠标离开时产生此事件  

## Event键盘事件
bing<Key>和事件函数来触发，其中Key 可以换成对应的键值，也可以是组合键。

## 程序事件

程序退出`root.protocol('WM_DELETE_WINDOW', printProtocol)  `


'''


import tkinter as tk

root = tk.Tk()

###################################
# 鼠标事件
###################################
def printroot(event):
    print(event.x,event.y)

bt = tk.Button(root, text="<Double-Button-1>：双击事件 ")
bt1 = tk.Button(root, text="<Triple-Button-1>：三击事件  ")
bt2 = tk.Button(root, text="<Leave>：鼠标离开时产生此事件")
bt3 = tk.Button(root, text="<Button-1>：鼠标左击事件")
bt4 = tk.Button(root, text="<Button-2>：鼠标右击事件")
bt5 = tk.Button(root, text="<Button-3>：鼠标中击事件")
bt6 = tk.Button(root, text="<B1-Motion>：鼠标移动事件,x=[1,2,3]分别表示左、右、中鼠标操作。  ")
bt7 = tk.Button(root, text="<ButtonRelease-2>鼠标释放事件,x=[1,2,3],分别表示鼠标的左、右、中键操作  ")
bt.grid()
bt1.grid()
bt2.grid()
bt3.grid()
bt4.grid()
bt5.grid()
bt6.grid()
bt7.grid()
bt.bind("<Double-Button-1>",printroot)
bt1.bind("<Triple-Button-1>",printroot)
bt2.bind("<Leave>",printroot)
bt3.bind("<Button-1>",printroot)
bt4.bind("<Button-2>",printroot)
bt5.bind("<Button-3>",printroot)
bt6.bind("<B1-Motion>",printroot)
bt7.bind("<ButtonRelease-2>",printroot)


###################################
# 键盘事件
###################################
def printkey(event):
    print("event.char = " + event.char)
    print('event.keycode = ', event.keycode)  


root.bind("<Shift_R>",printkey)
root.bind("<Shift_L>",printkey)
root.bind("<Return>",printkey)
root.bind("<Key>",printkey)


###################################
# 程序退出
###################################
def printProtocol():  
    print('WM_DELETE_WINDOW')  
    root.destroy() 

root.protocol('WM_DELETE_WINDOW', printProtocol)  
root.mainloop()