'''
Author: J.sky bosichong@qq.com
Date: 2017-09-04 11:47:52
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-12-02 20:11:23
FilePath: /PythonStudy/io/ospathtest.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#codeing=utf-8
# @Time    : 2017-09-04
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python os.path模块中一些常用方法的整理总结
# @Url     : http://www.17python.com/blog/12
# @Details : Python os.path模块中一些常用方法的整理总结
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
import os
import time
###################################
# 路径的常用方法
###################################
print(__file__) #当前文件的完整地址
print(os.path.abspath('ospathtest.py'))#当前文件的完整地址
print(os.path.dirname(__file__)) #当前目录所属地址
print(os.path.isdir(os.path.dirname(__file__)))# 判断是否为路径
print(os.path.isfile(os.path.dirname(__file__)))# 判断是否为文件
print(os.path.exists(os.path.dirname(__file__)))# 判断文件或是目录是否存在
##################################
p = os.path.join(os.path.dirname(__file__), 'aaa')
os.mkdir(p) # 创建目录
time.sleep(3)# 暂停3秒，这样就可以在左侧目录中看到新建的'aaa'目录了
os.rmdir(p)
print(p)# 组装目录
print(os.path.split(__file__))# 分割路径与文件名

###################################
# os中的一些is get方法
###################################
path = __file__
print(os.path.getatime(path))  #返回最后一次进入此path的时间。
print(os.path.getmtime(path))  #返回在此path下最后一次修改的时间。
print(os.path.getctime(path))  #返回path的大小
print(os.path.getsize(path))  #返回文件大小，如果文件不存在就返回错误
print(os.path.isabs(path))  #判断是否为绝对路径
print(os.path.isfile(path))  #判断路径是否为文件
print(os.path.isdir(path))  #判断路径是否为目录
print(os.path.islink(path))  #判断路径是否为链接
print(os.path.ismount(path))  #判断路径是否为挂载点


# 查找文件
def find_file(path,filename):
    """
    :param path: 文件夹路径
    :param filename: 文件名
    :return: 找到的文件路径列表
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == filename:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    return file_list

# 查找文件夹
def find_dir(path,dirname):
    """
    :param path: 文件夹路径
    :param dirname: 文件夹名
    :return: 找到的文件路径列表
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == dirname:
                file_path = os.path.join(root, dir)
                file_list.append(file_path)
    return file_list



# 删除文件
def del_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))


# 删除目录
def del_dir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))


