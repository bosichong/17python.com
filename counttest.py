'''
Author: J.sky bosichong@qq.com
Date: 2017-10-10 13:43:26
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-12-02 20:19:27
FilePath: /PythonStudy/counttest.py
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
            if '.git' not in root and name.endswith('.py'): # 排除掉git目录中的备份的文件，只保留.py文件
                pys.append(os.path.join(root, name))
        # 下边是拼装所有目录
        # for name in dirs:
        #     print(os.path.join(root, name))
    return pys


pys = getpys(os.path.dirname(__file__))
print(pys)
hacker = 100000  # 假设黑客需要10万行代码才能练成
lines = 0
for file in pys:

    with open(file, mode='r', encoding='utf8') as f:
        lines = lines + len(f.readlines())  # 统计每个文件的行数。


print("累计编写了源文件{0}个,手打{1}行Python代码，完成度{2:.2f}%".format(
    len(pys), lines, lines/hacker*100))


print("距离成为一名黑客还差{0}行代码".format(hacker-lines))

'''
累计编写了源文件32个,手打2133行Python代码，完成度2.13%
距离成为一名黑客还差97867行代码

这个数量有点惨。。。不过我会努力的。
'''
