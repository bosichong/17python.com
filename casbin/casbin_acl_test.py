'''
Author: J.sky bosichong@qq.com
Date: 2022-10-26 21:02:49
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-24 10:07:50
FilePath: /PythonStudy/casbin/casbin_acl_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


from casbin import FileAdapter
import casbin
import os

# model.conf 和 policy.csv 文件地址
model_dir = os.path.join(os.path.dirname(__file__), 'model.conf')
policy_dir = os.path.join(os.path.dirname(__file__), 'policy.csv')

p_dir = FileAdapter(policy_dir)
# 加载配置文件
e = casbin.Enforcer(model_dir,policy_dir)






sub = "alice"  # 想要访问资源的用户
obj = "data8"  # 将要被访问的资源
act = "read"  # 用户对资源进行的操作


def getEnforce(sub, obj, act):
    """
    执行器的封装
    """
    if e.enforce(sub, obj, act):
        # 允许alice读取data1
        return True
    else:
        # 拒绝请求，抛出异常
        return False


if __name__ == '__main__':
    print(getEnforce(sub,obj,act))