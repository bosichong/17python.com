#codeing=utf-8
# @Time    : 2017-12-19
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # 实战：利用Django开发部署自己的个人博客（15）Ubuntu+apache部署Django
# @Url     : http://www.17python.com/blog/67
# @Details : # 实战：利用Django开发部署自己的个人博客（15）Ubuntu+apache部署Django
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 实战：利用Django开发部署自己的个人博客（15）Ubuntu+apache部署Django
###################################
'''
到目前为止，我们基本利用`Django`基本上完成了blog的骨架搭建，当然blog功能依然只是最最最基础，相信各位朋友通过不断的学习可以扩展出来功能更强的blog。
从这节我们开始部署`Django`搭建的blog，说到部署与后期的网站维护，工作还是很大的，网站的运维其实和研发设计一样的重要的，如果说博客的功能基本上做好，
那么离网站上线运行还差一半的工作量，而且对待网站的运维我们需要更加认真仔细，因为本地调试的时候可以出错，但上线运行，我们需要的是安全与稳定。
说了这么多只是希望大家能把网站的运维工作当作一件大事来对待，如果我们确定自己要开发一个博客并上线运行，那么研发设计博客其实只占了一小部分，
我们大多时候都是要写博客，维护博客，备份博客数据，保护网站的安全，对于部署这里，我尽可能写的细致一些，把自己的经验写给大家，当然我也是一边学习一实践，欢迎各位大侠指正。

## Django Blog 服务器的选择

服务器选择阿里云是不会错的，另外关于服务器的配置512M内存对于新站绝对够用了，平时我观察内存只在30%左右使用率。。。大约300M+
硬盘一般40G起，如果你是以文字为主少许图片，这容量绝对够了。
服务器开始的时候够用即可，如果你人气很旺，再扩容就行了。**土豪随意**
如果你着急，可以点击下边的连接开始购买了。
[阿里云服务器全系列产品优惠卷领取！！！](https://promotion.aliyun.com/ntms/act/ambassador/sharetouser.html?userCode=cnafsz3c&utm_source=cnafsz3c)

## 部署前的准备

blog真正上线之前我们应该模拟一次甚至多次模拟线上的部署，直到比较熟悉那些流程之后再去真正的服务器上操作。
关于Django部署的一些配置这里列个简明的列表：

1. VirtualBox 5.0.X
2. ubuntu server 16.04
3. Apache 2.4.18
4. libapache2-mod-wsgi-py3
5. python 3.5.2
6. Django (1.11.3)

**另外因为我虚拟机没有固定IP，所以IP可能是`192.168.0.XXX`，所以大家在复制命令时根据自己的实际情况更换一下IP**
还有vim中的操作，我这里简单的介绍一下：

1. 插入字符 先按i  然后移动光标在需要的位置添加字符即可
2. 编辑状态下按esc键退出编辑状态
3. 非编辑状态 保存文件 :wq
4. 退出不保存  :q

这些基本上够用了，更详细的建议百度了解一下。

##如何在VirtualBox上安装ubuntu-16.04？

我觉得安装应该还算挺简单的，下载`ubuntu server`镜像，然后创建`VirtualBox`虚拟机，一路回车，有几个地方需要注意一下。

1. 用英文不要安装中文版。
2. 记好创建的用户名和密码。
3. 安装靠后边有个选择安装`Openssh server`，方便使用ssh远程连接。
4. 关于虚拟机中服务器的网络连接，请百度搜一下，因为环境不同，连接方法太多，所以大家自行研究一下吧。

如果你运气好的话，基本上一次即可搞定，SSD硬盘上安装的时间应该不会超过10分钟。

第一步应该是获取root的权限，修改root的密码：

    bosi@ubuntu:~$ sudo passwd root
    [sudo] password for bosi: 
    Enter new UNIX password: 
    Retype new UNIX password: 
    passwd: password updated successfully

虽然我们以后不会用root在服务器上操作部署，但root的权限我们必须掌握，而且给他修改一个非常复杂的密码，后边会介绍禁止root ssh远程登陆。

启用root用户：`sudo passwd root`      //修改密码后就启用了。
对`openssh server`进行配置,这样就可以使用root进行远程SSH登陆进行管理了。

    $ sudo vi /etc/ssh/sshd_config

找到`PermitRootLogin no`一行，改为`PermitRootLogin yes` 重启 `openssh server`

    $ sudo service ssh restart

然后就可以用root进行ssh登陆进行服务器配置管理了，这里有一个坑:**就是直接用安装时创建的用户来进行服务器配置，这个注册用户的权限不够，
配置后的Django程序会出现403的错误，这个坑网上没有人说明的，至少我没搜到。。。**我也是测试了几次才发现这个问题，解决方法就是提权注册的用户为系统管理员，
我们这里为了方便测试直接使用root管理员进行测试了，这个在服务器上一定不要用root来进行一些远程操作的，root都是禁止远程的，因为root的权限太大了。。
至此`ubuntu server`安装算是完毕了。

## 检察python3的运行环境

    root@ubuntu:~# python3
    Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.

## 检察pip3

    root@ubuntu:~$ pip3 list
    The program 'pip3' is currently not installed. You can install it by typing:
    sudo apt install python3-pip

提示我们没有安装pip3 好吧，我们按提示安装一下。

    sudo apt install python3-pip

一阵巴拉巴拉小魔仙的魔法之后，我们再检测一下：

    root@ubuntu:~$ pip3 list
    Traceback (most recent call last):
    File "/usr/bin/pip3", line 11, in <module>
        sys.exit(main())
    File "/usr/lib/python3/dist-packages/pip/__init__.py", line 215, in main
        locale.setlocale(locale.LC_ALL, '')
    File "/usr/lib/python3.5/locale.py", line 594, in setlocale
        return _setlocale(category, locale)
    locale.Error: unsupported locale setting

还是有错误，提示locale设置错误，`sudo locale-gen zh_CN.UTF-8`一下，之后正常了。

    root@ubuntu:~$ sudo locale-gen zh_CN.UTF-8
    Generating locales (this might take a while)...
    zh_CN.UTF-8... done
    Generation complete.
    root@ubuntu:~$ pip3 list
    chardet (2.3.0)
    command-not-found (0.3)
    language-selector (0.1)
    pip (8.1.1)
    You are using pip version 8.1.1, however version 9.0.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.rootrrrr

pip正常了，我们就可以安装`Django`及需要支持的模块了。回忆一下我们需要的模块。

1. Django (1.11.3)
2. Markdown (2.6.8)
3. Pillow (4.2.1)

那么我们通过`pip3`进行安装

    pip3 install django==1.11.3
    pip3 install markdown
    pip3 install pillow

![]()

我这边网络还可以，依次安装，如果网络很差，请下载安装包进行安装。
最后检测一下`Django`是否安装成功，可以打印一下`django`版本，或进直接创建一个`Django`项目来测试一下，

    root@ubuntu:~$ python3 
    Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import django
    >>> print(django.VERSION)
    (1, 11, 3, 'final', 0)

`django`安装测试完毕后，我们就要开始测试`Django`部署`(Apache)`。

## Apache2的安装

查看一下`Apache2`版本

    root@ubuntu:~$ apachectl -v
    The program 'apachectl' is currently not installed. You can install it by typing:
    sudo apt install apache2

发现没有安装`apache2`，那么我们开始按着提示的方法进行安装：

    sudo apt install apache2

又一堆代码提示安装完毕，再测试一下 

    root@ubuntu:~$ apachectl -v
    Server version: Apache/2.4.18 (Ubuntu)
    Server built:   2017-09-18T15:09:02

这次ok了，然后安装`apache2`对`python3`的支持

    sudo apt-get install libapache2-mod-wsgi-py3


好了，至此，服务器上对`django python3`的支持全部搞定，接下来就是配置`apache2`新建一个`django`站点，把自己的blog放到服务器上去了。

## 拷贝blog目录到服务器

之前都是一些环境的搭建，现在开始部署blog，首先把你的程序传到服务器的指定目录下，我们在home目录下新建一个www目录，以后把所有web应用都放在www下即可。

    root@ubuntu:/home#  mkdir www


好了，通过上边的终端命令，我们创建www目录，
现在我们要准备把blog整目录上传上去，关于上传文件有很多方法，如果是自己一个人打理程序，推荐直接上传文件或是使用git都可以。
我通过终端命令进行上传：

    ➜  ~ scp -r /Users/mac/PycharmProjects/PythonStudy/Django/blog01/ root@192.168.0.106:/home/www/blog01

scp是linux下的远程拷贝命令：

（1）将本地文件拷贝到远程：scp 文件名 用户名@计算机IP或者计算机名称:远程路径 
（2）从远程将文件拷回本地：scp 用户名@计算机IP或者计算机名称:文件名 本地路径
（3）将本地目录拷贝到远程：scp -r 目录名 用户名@计算机IP或者计算机名称:远程路径
（4）从远程将目录拷回本地：scp -r 用户名@计算机IP或者计算机名称:目录名 本地路径

如果你修改过远程端口号，请加上-P 端口号。
上边的ip应该换成你自己虚拟机中服务器的ip地址哦，如果没有其它特殊情况，blog整目录就已经copy过去了。
为了保证程序的正确性，我们先启动一下django自带的服务器测试一下：

    root@ubuntu:/home/www/blog01# cd blog01
    root@ubuntu:/home/www/blog01/blog01# ls
    __init__.py  __pycache__  settings.py  urls.py  wsgi.py
    root@ubuntu:/home/www/blog01/blog01# vim settings.py

vim settings.py 里我们修改了一下配置文件中的：

    ALLOWED_HOSTS = ['*',]

然后启动服务器：

    root@ubuntu:/home/www/blog01/blog01# cd ..
    root@ubuntu:/home/www/blog01# python3 manage.py runserver 192.168.0.207:8000

然后地址栏里输入http://192.168.0.207:8000/，一切完美，blog正常打开。

接下来我们开始配置apache2，这们就不在启用django自带的服务器了。

## Django 部署(Apache2)

终端下进入目录/etc/apache2/sites-available，这里有一个000-default.conf的配置文件，我们可以直接使用这个配置文件。

    root@ubuntu:/etc/apache2$ cd /etc/apache2/sites-available/
    root@ubuntu:/etc/apache2/sites-available$ ls
    000-default.conf  default-ssl.conf
    root@ubuntu:/etc/apache2/sites-available$ sudo vim 000-default.conf 

这里一定要加上sudo启动vim，然后我们编辑这个文件内容修改如下：

    <VirtualHost *:80>
        ServerName 17python.com
        ServerAlias www.17python.com
        ServerAdmin webmaster@localhost
        DocumentRoot /home/www/blog01

        Alias /media/ /home/www/blog01/media/
        Alias /static/ /home/www/blog01/static/

        <Directory /home/www/blog01/media/>
            Require all granted
        </Directory>

        <Directory /home/www/blog01/static/>
            Require all granted
        </Directory>
        <Directory /home/www/blog01/blog01>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>
        WSGIScriptAlias / /home/www/blog01/blog01/wsgi.py

            ErrorLog /home/www/blog01/error.log
            CustomLog /home/www/blog01/access.log common
    </VirtualHost>
    WSGIPythonPath /home/www/blog01

配置编辑好后，我们还需要修改网站目录的权限:

    root@ubuntu:/home/www# sudo chmod -R 644 blog01
    root@ubuntu:/home/www# sudo find blog01 -type d | xargs chmod 755

修改上传文件目录的权限：

    root@ubuntu:/home/www/blog01/media# sudo chgrp -R www-data upload
    root@ubuntu:/home/www/blog01/media# sudo chmod -R g+w upload

修改数据库权限,进到www这个目录

    root@ubuntu:/home/www# sudo chgrp www-data blog01
    root@ubuntu:/home/www# sudo chmod g+w blog01
    root@ubuntu:/home/www# sudo chgrp www-data blog01/db.sqlite3
    root@ubuntu:/home/www# sudo chmod g+w blog01/db.sqlite3

经过以上这些设置，网站基本上配置好了，我们来测试一下吧！
更新一下`apache2`的配置文件并重启`apache2`

    root@ubuntu:/etc/apache2/sites-available# sudo service apache2 reload
    root@ubuntu:/etc/apache2/sites-available# sudo service apache2 restart

现在我们不用在启动`django`自带的服务器了，我们打开ip地址 `http://192.168.0.106/`  (注意这里换成你自己的ip哦)
如果没有什么问题基，会看到首页正常打开，和我们平时用`django`自带的环境打开是一样的。
我们再打开admin后台看看 `http://192.168.0.106/admin`

![]()

额，后台没有加载css样式，哦原来是我们没有通过`django`的命令收集admin后台需要的静态文件，我们来配置一下：
编辑blog01中的配置文件settigns.py，在文件的最后添加:

    #服务器部署设置网站后ADMIN目录
    STATICFILES_DIRS = [
        "/usr/local/lib/python3.5/dist-packages/django/contrib/admin/static",
    ]
    #服务器部署时修改为静态文件存放目录
    STATIC_ROOT = "/home/www/blog01/static/"

然后切换目录到`www/blog01/` 运行终端命令：

    python3 manage.py collectstatic

如果你的目录地址正确，那么会把admin后台需要的css相关文件复制到网站的静态目录下了。

我们重启一下服务`apache2` 

    sudo service apache2 restart
    
好吧，久违的后台界面又正常啦，登陆后测试应该是功能一切正常啦！

## apache2 配置django中的一些坑

1. 提示403错误，这个我觉得一种可能是没有使用具有root权限的`ubuntu`管理员进行了服务器的配置，第二个就是网站目录的权限没有修改。
2. 静态文件无法读取，考虑两种可能，一种是静态文件的目录权限不正确，还有就是静态文件没有被程序收集，请运行终端全集进行收集。
3. 网站显示不正常，请检查`apache2`配置文件和`Django`的配置文件是否正确？

暂时只想到这些，这篇教程写的有些长，前后更进行了三次测试，确保可以在虚拟下完美配置，有什么问题请给俺留言哈，有错误欢迎指正！




'''