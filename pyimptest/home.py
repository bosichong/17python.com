# 有关Python文件不同目录加载的测试。
from suba.a import *
# from subb.b import *

import subb

home = "这是来自home目录的变量。"

def homeprint():
    print("home目录的打印")


subaprint()
b.subbprint()

