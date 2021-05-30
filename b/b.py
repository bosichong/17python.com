#codeing=utf-8
# @Time    : 2017-10-27
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : python中导入不同目录中的自定义模块/class/函数/方法
# @Url     : http://www.17python.com/blog/50
# @Details : python中导入不同目录中的自定义模块/class/函数/方法
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# python中导入不同目录中的自定义模块/class/函数/方法
###################################

'''
前几天在封装`PY_RPGP`框架时，需要导入一些自定义的类、函数、常量的时候，发现始终找不到相关模块，后来参考书籍及网络上的一些经验终于解决了这个问题。

## 包和模块导入的需求

假设有一个项目，有a/a.py（此为工具类提供一些简单的方法和常量），b/b.py（需要调用a/a.py）项目文件，我们先在a.py中定义一些函数及常量一会引入使用。

    M_TEST = 888
    def print_text():
        print('这a.py下的一个打印文字函数')

现在我们引入测试

    import a.a
    a.print_text()

ModuleNotFoundError: No module named 'a'  很显然这样是找不到正确目录的，那么问题来了，
如果是在同一目录，我们直接`import a`就搞定了，但实际工作中我们不可能把所有文件都放在一个目录中，如果需要导入其它目录的中.py文件，这时我们就需要用到`sys.path.append()`


'''
import sys
print(sys.path)

'''

    ['/Users/mac/PycharmProjects/PythonStudy/b', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Users/mac/Library/Python/3.6/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/beautifulsoup4-4.6.0-py3.6.egg', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyMySQL-0.7.11-py3.6.egg', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/xadmin-0.6.1-py3.6.egg', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/django_formtools-2.0-py3.6.egg']

打印后，我们会发现很多目录，`python`加载包模块的目录就都在上边了，他会从这些目录中搜索需要加载内容的名称，如果有就加载进来。
那么我们如何把自己的文件加到上边的目录里？有几种方法：

+ 通过修改环境变量，这个不环保，而且文件多了，不可能都去修改。
+ 复制文件到上边的目录中，有些不方便，不推荐
+ `sys.path.append()`把目录加进索引，方便python搜索，推荐

那么我们来试试吧

## 如何优雅的获得目录地址？

如果需要把目录加进到索引中，我们只需要一个绝对地址即可，但是这种方法如果我们复制工程到其它目录后，我们还需要修改这个索引，很不方便不科学。
这时我想到了`Django`配置文件中有一段代码

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

我们理解一下这段代码，`__file__ `表示当前.py文件，`os.path.abspath(__file__)` 表示当前.py文件的绝对地址，`dirname`获得上一层目录地址，
那么如果我们当前的文件在根目录下的一个目录下边，那么上条语句正好获得了根目录的地址。我们来打印试试

    /Users/mac/PycharmProjects/PythonStudy/b/b.py
    /Users/mac/PycharmProjects/PythonStudy/b
    /Users/mac/PycharmProjects/PythonStudy

可以看到根目录地址已经得到了，然后通过`os.path.join()` 就可以拼装到工具类目录地址了，到这里我们的所有功能基本上可以实现了，具体实现请看下边的代码。


'''

import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取根目录
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
T_DIR = os.path.join(BASE_DIR,'a')#拼装工具类地址
print(T_DIR)
sys.path.append(T_DIR)
import a
print(a.M_TEST)
a.print_text()
