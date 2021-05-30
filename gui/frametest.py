#codeing=utf-8
# @Time    : 2017-09-22
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python TK和Tkinter的GUI编程(1)
# @Url     : http://www.17python.com/blog/21
# @Details : Python TK和Tkinter的GUI编程(1)
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# Python TK和Tkinter的GUI编程(1)
###################################
import tkinter #导入支持库
'''
Python编程中有时我们需要一些可视化的操作，如果功能相对很简单，可以使用Python内置的GUI模块：tkinter
这个模块所提供的功能及部件不是很多，如果你用过java，和Swing、AWT相比，tk的所提供的确实是要少很多了。但是如果只是简单的显示或是数据展示，基本上还是够用的。

tk的组件不是很多，包括以下：
Button	按钮控件；在程序中显示按钮。
Canvas	画布控件；显示图形元素如线条或文本
Checkbutton	多选框控件；用于在程序中提供多项选择框
Entry	输入控件；用于显示简单的文本内容
Frame	框架控件；在屏幕上显示一个矩形区域，多用来作为容器
Label	标签控件；可以显示文本和位图
Listbox	列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
Menubutton	菜单按钮控件，由于显示菜单项。
Menu	菜单控件；显示菜单栏,下拉菜单和弹出菜单
Message	消息控件；用来显示多行文本，与label比较类似
Radiobutton	单选按钮控件；显示一个单选的按钮状态
Scale	范围控件；显示一个数值刻度，为输出限定范围的数字区间
Scrollbar	滚动条控件，当内容超过可视化区域时使用，如列表框。.
Text	文本控件；用于显示多行文本
Toplevel	容器控件；用来提供一个单独的对话框，和Frame比较类似
Spinbox	输入控件；与Entry类似，但是可以指定输入范围值
PanedWindow	PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
LabelFrame	labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
tkMessageBox	用于显示你应用程序的消息框。

之前在网上搜过，相关的教程不是很多，而且文档也写的算是很烂了，当然如果你英文不错，直接看源文件里的注释基本上就够用了，不过有的时候看py源文件还真是有点不太习惯，如果有示例或文档还好。
最近搜集了一下相关的文档及教程，虽然不是很多，但是基本上可以满足对tk学习及了解了，希望通过几篇简单的教程示例，帮助大家了解一下tk的用法，已来解决一些python编程中简单的GUI需求。
当然这些内容并不完整，我会在日常的应用中随时进行补充，也欢迎各位在评论中补充。

## 窗口

root = tkinter.Tk() 这里创建一个root窗口，可以看成是一个APP的最顶层。
顶层Tk对象一些方法，这里说一些实用的：

+ title() 这个用来设置窗口的标题
+ geometry('500x300+300+300') 设置窗口的大小及位置，如果省去后边的+300+300位置，只控制窗口的大小。

## Frame 

可以看成是一个可以装着众多部件的容器，他本身也可以容纳自己，嵌套自己。

+ fill=NONE or X or Y or BOTH - fill widget if widget grows 填充设置选项，可以设置无，x，y 或是都二者皆填充.
+ side=TOP or BOTTOM or LEFT or RIGHT 这里一共有四个选项，可以控制容器位置 


## Label

我觉得label中比较重要的就是内容字符串的修改，默认使用text="str"设置label的显示文字，但是如果程序中需要动态的修改，就需要另外一个属性方法了，
var = tkinter.StringVar() 会生成一个对象，用来存放label要显示的文字，然后可以通过函数动态的修改这个字符串，其使只需要在label创建的时候，为textvariable=var设置一个属性值，
这样就可以在程序中通过修改var来进行修改label显示的字符了。
其它比较常用的属性还用，fg="#c00"，字体颜色，bg="red"，背景颜色设置，当然还有很多属性，可以通过文档查看。

## Buttom
按钮，可以说是程序中最常用的部件了，其属性和label部分有些相似，比如动态修改按钮上的文字也是使用StringVar()。
按键程序员最关心的莫过于是按键的点击事件，Tk的按键点击事件通过command=def来进行设置，其中def为函数名称，如果设置关联了函数，点击按键就会运行相关的函数了。

mainloop() 个人理解为循环刷新渲染当前GUI窗口中的内容，如果没有这个函数，窗口是无法显示的。
'''

def def1():
    """按钮1"""
    var1.set('看，我变啦！')
    
def def2():
    '''按钮2'''
    var2.set("百叶窗折射的光影")

def def3():
    '''按钮3'''
    var3.set('因为中间空白的时光 如果还能分享 也是一种浪漫')

root = tkinter.Tk()#创建一个root窗口
root.title('我只是一个测试的窗口')#设置窗口标题
bt = tkinter.Button(root, text="我是来占位的").pack(fill=tkinter.X, side=tkinter.TOP)
# root.geometry('500x300+300+300')#设置窗口的大小及位置
m_frame = tkinter.Frame(root)# 一个部件容器
m_frame.pack(fill=tkinter.X, side=tkinter.TOP)
# 创建一个快捷方式,用来生成小部件。
LEFT, Label, Buttom = tkinter.LEFT, tkinter.Label, tkinter.Button
label_line = tkinter.Frame(m_frame, relief=tkinter.RAISED, borderwidth=1)# 创建一个容器放入info_frame中
label_line.pack(side=tkinter.TOP, padx=2, pady=2)
var1 = tkinter.StringVar()
var1.set('默认文字')
var2 = tkinter.StringVar()
var2.set('听见下雨的声音')
var3 = tkinter.StringVar()
var3.set("#眼角的泪这不是错觉")
# fg="red" 文字颜色,颜色可以接受"cc0000" WEB颜色值等。
l1 = Label(label_line, width=20, textvariable=var1, fg="#c00").pack(side=LEFT)
l2 = Label(label_line, width=20, textvariable=var2, bg="#c00").pack(side=LEFT)
# show='*' 可以使文本框内容显示为*****
e3 = tkinter.Entry(label_line, textvariable=var3).pack(side=LEFT)

buttom_line = tkinter.Frame(m_frame)
buttom_line.pack(side=tkinter.BOTTOM, padx=2, pady=1)
b1 = Buttom(buttom_line, text="点我试试1", width=18, command=def1).pack(side=LEFT)
b2 = Buttom(buttom_line, width=18, textvariable=var2, command=def2).pack(side=LEFT)
b3 = Buttom(buttom_line, text="点我试试3", width=18, command=def3).pack(side=LEFT)
root.mainloop() 

