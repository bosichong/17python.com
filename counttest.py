#codeing=utf-8
# @Time    : 2017-10-10
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 你与黑客之间差了多少行代Python码？
# @Url     : http://www.17python.com/blog/38
# @Details : 你与黑客之间差了多少行代Python码？
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 你与黑客之间差了多少行代Python码？
###################################

'''
## 100000万行代码

雷布斯曾说过：“必须写够十万行代码，不要心存侥幸。没有写过足够代码量的，想成为高手是不可能的，只能纸上谈兵！”，看来要成一名黑客10万代码量也许只是个起步。
那么自己与黑客差了多少呢，要不咱统计一下吧。

## 编写思路

程序的编写思路其实很简单：统计自己编写过的.py文件，然后统计文件行数累加到一起就ok。

`os.walk`这个方法可以统计当前目录下所有的文件、子目录、子目录下的文件，有了这个数据，我们只需要排除掉不需要的，统计以.py为结尾的文件目录地址加入一个列表即可。

有了所有.py文件的列表，循环迭代出每个文件的行数，加到一起总数据就出来了。具体实现请看代码：

'''
import os
def getpys(dir):
    '''
    递归获得当前目录及其子目录中所有的.py文件列表。
    '''
    pys = []
    # 当前目录下所有的文件、子目录、子目录下的文件。
    for root, dirs, files in os.walk(dir):
        for name in files:
            #排除掉git目录中的备份的文件，只保留.py文件
            if '.git' not in root and name.endswith('.py'):
                pys.append(os.path.join(root, name))
        #下边是拼装所有目录
        # for name in dirs:
        #     print(os.path.join(root, name))
    return pys
pys = getpys(os.path.dirname(__file__))
# print(pys)
hacker=100000#假设黑客需要10万行代码才能练成
lines = 0
for file in pys:
    with open(file, mode='r', encoding='utf8') as f:
        lines = lines + len(f.readlines())#统计每个文件的行数。
print("累计编写了源文件{0}个,手打{1}行Python代码，完成度{2:.2f}%".format(len(pys),lines,lines/hacker*100))
print("距离成为一名黑客还差{0}行代码".format(hacker-lines))
        
'''
累计编写了源文件32个,手打2133行Python代码，完成度2.13%
距离成为一名黑客还差97867行代码

这个数量有点惨。。。不过我会努力的。
'''