#codeing=utf-8
# @Time    : 2017-11-16
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 听说存储数据Python与SQLite3更配哦！
# @Url     : http://www.17python.com/blog/55
# @Details : 听说存储数据Python与SQLite3更配哦！
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 听说存储数据Python与SQLite3更配哦！
###################################
'''
曾经以为数据库自己一定需要大的，好的，功能多的，处理数据快的，迸发牛的，现在想想就象上小学时时常想：以后考大学是北大还是清华呢？后来才发现自己真特么多虑了。
如果你只是个人或是小型的应用，我这里隆重的推荐给你SQLite这个迷你型的数据库。

## SQLite
SQLite 是一个软件库，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。SQLite 是在世界上最广泛部署的 SQL 数据库引擎。SQLite 源代码不受版权限制。
是不是很兴奋？没有其它数据库的安装配置繁琐步骤，没有占用你吃紧的内存，最重要的是功能一样大而全而且免费不要钱。

## SQLite安装
几乎所有版本的 Linux 操作系统都附带 SQLite，所以win党们请自行在官网上下载安装即可。

    ➜  ~ sqlite3 
    SQLite version 3.8.10.2 2015-05-20 18:17:19
    Enter ".help" for usage hints.
    Connected to a transient in-memory database.
    Use ".open FILENAME" to reopen on a persistent database.
    sqlite> 

通过终端输入sqlite3即可验证数据库是否安装成功！

## python中使用sqlite3

通过Python结合sqlite3实现一个简单的个人备忘录，简单了解一下在Python中是如何操作数据库的。
在Python中操作sqlite很简单，引入sqlite3模块，就可以开始进行数据库的编程之旅了。

## 创建数据库
'''
# import sqlite3#引入模块
# import os
# from datetime import *
# print(os.path.join(os.path.dirname(__file__), 'memorandum.db'))
# conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'memorandum.db'))#在当目录下创建数据库
# print('备忘录数据库创建成功！')
'''
## 创建表及字段

cursor()将创建一个cursor对象，将在Python数据库编程中用到。
cursor.execute()将处理操作与数据库相关的几乎所有命令。
'''

# c = conn.cursor()#创建一个cursor对象
# # 创建表
# c.execute('''create table tab(
#     id integer not null primary key autoincrement,
#     title char(50),
#     content text not null,
#     c_date text);''')
# print('数据表创建成功！')
# conn.commit()#提交事务
# conn.close()#关闭连接

'''
通过以上代码就可以在数据库中创建一个表了，如果你不太习惯在代码中创建表，你可以使用DBeaver,操作简单方便人性化，是编写数据库命令，查看数据库表结构，备份数据之良品。
有了数据表，我们就可以对表进行增删改查了。
sqlite中的sql语句和大部分数据库操作语名是相同的，如果你有过其它数据库操作的基础，那么使用sqlite就会非常简单了

'''

## 插入数据

# title = '测试标题'
# content = '插入数据测试。'
# format = "%Y-%m-%d %H:%M:%S"
# now = datetime.now().strftime(format)#创建当前时间字符串
# sql = "insert into tab (id,title, content, c_date) values (NULL,'{0}','{1}','{2}')".format(title,content,now)
# print(sql)
# c.execute(sql)
# conn.commit()
# conn.close()#关闭连接
'''
## 批量插入数据

python往sqlite3插入数据的sql语句支持'?'占位符，这样我们很方便的可以批量插入数据。

'''

# 准备10000条数据插入
# for i in range(10000):
#     format = "%Y-%m-%d %H:%M:%S"
#     now = datetime.now().strftime(format)#创建当前时间字符串
#     c.execute('insert into tab (id,title, content, c_date) values(?,?,?,?)',(None,str(i),str(i),now))
# conn.commit()#提交事务
# conn.close()

## 删除数据

sql = "delete from tab where id = 2"#拼装sql语句
c.execute(sql)#执行删除
conn.commit()
conn.close()

'''
执行上边的代码，发现id为2的数据已经被删除。
![]()

'''

## 更新数据

# sql = "update tab set title='Boy' where id = 20004"
# c.execute(sql)
# conn.commit()
# conn.close()

##查询数据

# sql = "select * from tab"
# l = c.execute(sql)
# for s in l :
#     print(s)
# conn.close

'''
运行代码后可以看到终端输出：
![]()

其它查询只是sql语句的不同，这里暂时不再测试了，有兴趣的可以查阅sql编程相关资料。
综合来说，`python`与`sqlite3`联合使用真是很方便，是数据采集入库处理查询必备哇。


'''

