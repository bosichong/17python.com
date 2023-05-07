'''
Author: J.sky bosichong@qq.com
Date: 2022-11-21 08:22:25
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-21 08:22:58
FilePath: /PythonStudy/pytest/test_pytest.py



.setup和teardown主要分为：模块级别、类级别、函数级别、方法级别、方法细化级别，分别如下：
方法	描述
setup_module()	在每个模块之前执行
teardown_module()	在每个模块之后执行
setup_class()	在每个类之前执行，即:在一个测试类只运行一次setup_class和teardown_class，不关心测试类内有多少个测试函数。
teardown_class()	在每个类之后执行，即:在一个测试类只运行一次setup_class和teardown_class，不关心测试类内有多少个测试函数。
setup_function()	在每个函数之前执行。
teardown_function()	在每个函数之后执行。
setup_method()	在每个方法之前执行
teardown_method()	在每个方法之后执行
setup()	在每个方法之前执行
teardown()	在每个方法之后执行


'''

import pytest


def setup_module():
    print("=====整个.py模块开始前只执行一次:打开浏览器=====")


def teardown_module():
    print("=====整个.py模块结束后只执行一次:关闭浏览器=====")


def setup_function():
    print("===每个函数级别用例开始前都执行setup_function===")


def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function====")


def test_one():
    print("one")


def test_two():
    print("two")


class TestCase():
    def setup_class(self):
        print("====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        print("==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        print("==类里面每个用例结束后都会执行teardown_method==")

    def setup(self):
        print("=类里面每个用例执行前都会执行setup=")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=")

    def test_three(self):
        print("three")


def test_four():
    print("four")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "test_one.py"])
# 运行测试用例，显示总的结果信息，使用命令 pytest -ra
