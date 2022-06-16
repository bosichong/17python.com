import pytest

from algorithm import *

'''终端运行 pytest test_main.py  进行测试'''

def test_factorial():
    '''测试递归函数'''
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(3) == 88888