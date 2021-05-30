#codeing=utf-8
# @Time    : 2017-11-08
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 实战：利用Django开发部署自己的个人博客（1）
# @Url     : http://www.17python.com/blog/52
# @Details : 实战：利用Django开发部署自己的个人博客（1）
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（1）
###################################
'''
## 写在开篇

很早就想写一个有关`Django`相关的系列博文，因为通过`Django`开发本博客的过程中有很多感触，深深的体会到`Python Django`的强大与灵活，
所以，是时候写下这些从开发到上线部署过程中遇到的坑与灵光闪现的点滴。

## 为什么要自己开发部署一个线上博客？

从需求的角度上来说，自己开发一个博客纯属重复造轮子，因为现成的功能丰富的博客系统网上有很多了，比如一些程序员喜欢的博客网站：

+ csdn
+ oschina
+ 简书
+ 新浪博客

。。。。。。

很多很多，还有一些现在的框架程序比如php下大名鼎鼎的`WordPress`等，都可以快速的搭建一个功能丰富的博客。
那么为什么我们还要自己利用`python django`搭建一个线上博客呢？
答案很简单，我们需要实践，需要更多的敲打代码的机会，更多程序构建思考的机会。

## 需要的知识点。

首先这并不是一篇给无`python`基础人看的博文，你必须已经拥有`python`相关的基础知识，并且你需要了解`html css js`及有一些相关框架的知识。
另外，还需要对数据库有一定了解，至少需要明白一些常用的增删改查操作。
因为这是一个需要上线部署的博客，你还需要有一些服务器维护的经验，当然这个后期我会介绍一些的。
美工？需要一个美工吗？如果一个博客打开后没有一点个性的话，估计是没什么人愿意看的。
当然，最重要的还是需要有一颗耐心细心爱学的心，一种编程的态度。

## 博客搭建环境

这个是开发阶段的运行环境，部署时我会说明部署环境的。

    OS X 10.11.6 
    Python 3.6.1
    VSCode 1.15.1
    Django 尽量用最新版。

关于程序环境我想说，不建议新手使用什么多个虚拟环境，你只在这一个环境下操作即可，重点放在博客的开发测试过程中来。
有关`python VSCode` 安装配置，网上有很多教程，这里不在重复介绍了，`Django`在win与osx下边的运行基本上差不多，
所以你使用win10或xp也适用本教程，只是安装配置你需要按着自己的环境来操作，Djaogn中的代码是一至的。

## Django 安装

    pip3 install Django

如果你需要指定版本

    pip3 install Django == 1.1X

如果无法在线安装，请下载安装 [https://www.djangoproject.com/download/](https://www.djangoproject.com/download/)
下载后，解压并进入目录：

    python setup.py install

查看是否安装成功？

<pre><code>
➜  ~ python3                                                    
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.VERSION)
(1, 11, 3, 'final', 0)

</code></pre>

如果报错则是安装失败，成功显示和上边略同。

## 第一个Django项目

我们来创建第一个项目，进入你要创建项目的目录，终端下输入：

    django-admin startproject blog01

然后进入目录：
    python3 manage.py startapp myblog

运行项目：

    python3 manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.

    November 08, 2017 - 03:22:17
    Django version 1.11.3, using settings 'blog01.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

好啦，大功告成！

![]()

'''