#codeing=utf-8
# @Time    : 2017-09-26
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(5) messagebox tk的弹出对话框
# @Url     : http://www.17python.com/blog/25
# @Details : Python TK和Tkinter的GUI编程(5) messagebox tk的弹出对话框
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python tk messagebox tk的弹出对话框
###################################
"""
messagebox 弹出提示框 一共有七种常用方法，基本上可以应付一般简单的程序需求了：
showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, or askretrycancel.
其中askquestion, askokcancel, askyesno, or askretrycancel这4个方法，应该注意一下点击按钮的返回值。


"""



import tkinter as tk
from tkinter import messagebox  # 导入提示窗口包

str1=("showinfo","showwarning","showerror","askquestion","askokcancel","askyesno","askretrycancel")
def showMsg(str):
    """弹出窗口设置函数"""
    print(str)
    if str == str1[0]:
        messagebox.showinfo("showinfo","信息提示框！")
    elif str == str1[1]:
        messagebox.showwarning("showwarning","警告框！")
    elif str == str1[2]:
        messagebox.showerror("showerror","错误信息框！")
    elif str == str1[3]:
        if messagebox.askquestion("askquestion","askquestion提示框") == messagebox.YES:
            messagebox.showinfo("yes","你点了yes!")
        else:
            messagebox.showinfo("no","你点了no")
    elif str == str1[4]:
        if messagebox.askokcancel("askokcancel","askokcancel提示框"):
            messagebox.showinfo("OK","你点Ok")
        else:
            messagebox.showwarning("cancel","你点了cancel")
    elif str == str1[5]:    
        print(messagebox.askyesno("askyesno","askyesno提示框"))
    elif str == str1[6]:    
        print(messagebox.askretrycancel("askretrycancel","askretrycancel提示框"))

root = tk.Tk()
root.title("messagebox 弹出对话框使用例子")

show_frame = tk.Frame(root)
show_frame.pack(fill=tk.X, side=tk.TOP)
btn1= tk.Button(show_frame, text=str1[0],command=lambda showMsg = showMsg : showMsg(str1[0]) ).pack(side=tk.LEFT)
btn2= tk.Button(show_frame, text=str1[1],command=lambda showMsg = showMsg : showMsg(str1[1]) ).pack(side=tk.LEFT)
btn3= tk.Button(show_frame, text=str1[2],command=lambda showMsg = showMsg : showMsg(str1[2]) ).pack(side=tk.LEFT)

asky_frame = tk.Frame(root)
asky_frame.pack(fill=tk.X,side=tk.TOP)
bt4 = tk.Button(asky_frame,text=str1[3],command=lambda showMsg = showMsg : showMsg(str1[3]) ).pack(side=tk.LEFT)
bt5 = tk.Button(asky_frame,text=str1[4],command=lambda showMsg = showMsg : showMsg(str1[4]) ).pack(side=tk.LEFT)
bt6 = tk.Button(asky_frame,text=str1[5],command=lambda showMsg = showMsg : showMsg(str1[5]) ).pack(side=tk.LEFT)
bt7 = tk.Button(asky_frame,text=str1[6],command=lambda showMsg = showMsg : showMsg(str1[6]) ).pack(side=tk.LEFT)
root.mainloop()