#codeing=utf-8
# @Time    : 2017-09-22
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(2) 菜单Menu
# @Url     : http://www.17python.com/blog/22
# @Details : Python TK和Tkinter的GUI编程(2) 菜单Menu
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python TK和Tkinter的GUI编程(2) 菜单Menu
###################################
import tkinter #导入支持库
'''
## Menu

菜单的创建是很简单的，先创建一个顶层的菜单加入顶层窗口root中，然后分别创建二级菜单就可以了。
几个比较重要的方法函数：

+ tkinter.Menu(root) 创建顶层菜单，root是你的顶层窗口。
+ root.config(menu=menu) 然后加入顶层窗口
+ menu.add_cascade() 添加二级菜单，label设置二级菜单名称，menu设置二级菜单对象。
+ filemenu.add_command() 添加一个普通的菜单项，label设置显示字符串，command设置回调函数
+ 关于右键菜单的实现，可以参考源码中的注释处。

还有很多功能，建议参考一下文档了了解，以上几个功能一般简单应用可以应付了。

'''

def callback():
    """一个简单的回调测试"""
    print ("called the callback!")

root = tkinter.Tk()#创建一个root窗口
root.title('我只是一个测试的窗口')#设置窗口标题
root.geometry('500x300+300+300')#设置窗口的大小及位置

# 创建菜单
menu = tkinter.Menu(root)#顶层菜单
root.config(menu=menu)#加入窗口
filemenu = tkinter.Menu(menu)#创建二级菜单File
menu.add_cascade(label="File", menu=filemenu)#加入menu
# 创建二级菜单下的功能键
filemenu.add_command(label="New", command=callback)#按钮
filemenu.add_command(label="Open...", command=callback)
filemenu.add_checkbutton(label="checkbutton",)#选择框，选中后会画一个对号。
filemenu.add_separator()#分隔线
filemenu.add_radiobutton(label="radiobutton",)#一旦勾选，无法取消
filemenu.add_separator()#分隔线
filemenu.add_command(label="Exit", command=callback)

helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

#####实现右键弹出菜单####
def popup(event):
    menu.post(event.x_root, event.y_root)
root.bind("<Button-2>", popup)
root.mainloop() 

