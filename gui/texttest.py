#codeing=utf-8
# @Time    : 2017-09-26
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(4) Entry Text 文本框控件
# @Url     : http://www.17python.com/blog/24
# @Details : Python TK和Tkinter的GUI编程(4) Entry Text 文本框控件
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python TK和Tkinter的GUI编程(4) Entry Text 文本框控件
###################################
import tkinter as tk
"""
Tk的功能不多，但应付一般应用还是足够了，Entry和Text是Tk下边显示及处理文本的小部件。
涉及到文本，从使用角度来说，有几个功能是必须的：

+ 设置文本框的内容`insert()`
+ 删除文本框的内容`delete()`
+ 获得文本框的内容`get()`
+ show="*"这个可以设置密码框用***来显示密码

关于布局，和其它部件基本上是一样的，前边的章节有过介绍。

本次使用tk制作了一个用户登陆验证用户名和密码的小例子。

演示图如下：
~[演示图](http://www.17python.com/media/upload/2017/09/Snip20170926_4.png)

"""


def isLogin(uname,pword):
    """验证用户登陆函数"""
    if uname == "17python" and pword == "17python":
        print("登陆成功！")
        out.insert(tk.END,"登陆成功！\n")
    else:
        print("用户名或密码错误！")
        out.insert(tk.END,"用户名或密码错误！ \n")

root = tk.Tk()
root.title('文本框的测试')
userinfo_frame = tk.Frame(root)
userinfo_frame.pack(fill=tk.X, side=tk.TOP)
########
user_frame = tk.Frame(userinfo_frame, )
user_frame.pack(fill=tk.X, side=tk.TOP)
user_label = tk.Label(user_frame, text="username:",font=("Symbol", 14)).pack(side=tk.LEFT)
username = tk.Entry(user_frame, width=40)
username.pack(fill=tk.X, side= tk.LEFT)

#######
pass_frame = tk.Frame(userinfo_frame)
pass_frame.pack(fill=tk.X, side=tk.TOP)
pass_label = tk.Label(pass_frame, text="password:",font=("Symbol", 14)).pack(side=tk.LEFT)
password = tk.Entry(pass_frame, width=40, show="*")
password.pack(fill=tk.X, side= tk.LEFT)
########
btn_frame = tk.Frame(userinfo_frame)
btn_frame.pack(fill=tk.X, side=tk.TOP)
btn = tk.Button(btn_frame, text='登陆', command= lambda isLogin = isLogin : isLogin(username.get(), password.get())).pack(fill=tk.X)
out = tk.Text(btn_frame,width=40,font=("Symbol", 14))
out.insert(tk.END, "world \n")
out.pack(fill=tk.X)

root.mainloop()