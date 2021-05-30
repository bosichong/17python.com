#codeing=utf-8
# @Time    : 2017-10-09
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 聊聊Python闭包（Closure）的那点事。
# @Url     : http://www.17python.com/blog/36
# @Details : 聊聊Python闭包（Closure）的那点事。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1

###################################
# 聊聊Python闭包（Closure）的那点事。
###################################
'''
记得当年学`JavaScript`时，对闭包的认识那真是朦朦胧胧，后来接触到`jQuery`之后，对闭包的认识还是一知半解，可能之前一直学习本分的静态语言`java`给耽误了。。。。。。
好吧，闭包到是个什么？是一个让初学编程的人头疼的问题

## Pythib闭包

先来一个栗子，我们慢慢理顺一下。
'''

def callf():
    def hello():
        return "hello world"
    return hello

cf = callf() #创建一个callf函数，这时把hello()赋值给了cf
print(type(cf)) # 查看cf类型，证实上边的结论。
print(cf()) #打印最终结果。

# 在一个函数中，把这个函数内部的一个函数做为返回值，那个这个被返回的函数就可以叫做闭包。（这条是本人自己写的，和网上其它处的理论会有些出入或是不同）
# 上边就算是闭包最简单的例子，多看几次应该就理解了。

# 再看下边的例子,这是一个利用闭包设计的简单自减计数器，其实我第一眼看去的时候就觉得为什么要这么写？

def countdown(n):
    def next():
        nonlocal n 
        r = n 
        n -= 1
        return r
    return next

nt = countdown(5)
while True:
    v = nt()
    print(v)
    if not v :break

# 这个自减计数器的应该还有几种其它写法，而且加之使用nonlocal这个关键字，使人更加迷惑了，如果注释掉`nonlocal n`，程序运行就会抛出错误，可见nonlocal的使用使next()函数内部变量`n`的值可以修改。
# 本人对此得的理解也不是很好，希望有大侠给与指点，也许这个例子不太理想。

# 再看循环中的闭包：

def loop():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = loop()
print(f1())

#f1()的打印竟然9，这个有点出乎意料！我们修改一下这个函数

def loop(): 
    def f(j):
        return lambda: j*j
    fs = []
    for i in range(1,4):
        fs.append(f(i))       
    return fs
f1,f2,f3 = loop()
print(f1())
print(f2())
print(f3())

'''

对比上边的两段代码，第一段直接返回了三次循环的最终结果，而第二段代码，再循环中遇到了`f()`函数`return`所以暂停了程序的运行，直到第二个赋值时又循环了一次，然后继续，这也说明，闭包的函数不要放在循环体内，不然直接返回的是循环的最终结果。
有的同学会问，了解闭包有什么用？闭包是装饰器和生成器的基础，如果你应用`Python`函数的高级应用，不妨仔细的了解一下闭包吧。


'''