import casbin_sqlalchemy_adapter
from casbin_sqlalchemy_adapter import CasbinRule
import casbin
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import os

# model.conf 和 policy.csv 文件地址
model_dir = os.path.join(os.path.dirname(__file__), 'rbac_model.conf')

# 组装数据库的绝对地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'test_rbac.db')
# 数据库访问地址
SQLALCHEMY_DATABASE_URL = "sqlite:///" + DB_DIR
# 从数据库加载casbin的policy
adapter = casbin_sqlalchemy_adapter.Adapter(SQLALCHEMY_DATABASE_URL)
e = casbin.Enforcer(model_dir, adapter)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(bind=engine)
s = session()
s.query(CasbinRule).delete()
s.add(CasbinRule(ptype="p", v0="alice", v1="data1", v2="read"))
s.add(CasbinRule(ptype="p", v0="bob", v1="data2", v2="write"))
s.add(CasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="read"))
s.add(CasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="write"))
s.add(CasbinRule(ptype="g", v0="alice", v1="data2_admin"))
s.add(CasbinRule(ptype="g", v0="alice", v1="data2_admin"))
s.add(CasbinRule(ptype="g", v0="alice", v1="data2_admin"))
s.commit()
s.close()

# e.add_policy(["alice", "data1", "read"])
# e.add_policy(["bob", "data2", "write"])

# e.add_policy(["data2_admin", "data2", "read"])
# e.add_policy(["data2_admin", "data2", "read"])
# e.add_policy(["data2_admin", "data2", "read"])
# e.add_policy(["data2_admin", "data2", "write"])
# todo 解决 添加规则是重复的问题,把登陆token验证和权限控制验证分别做成装饰器,用来验证登陆.

# adapter.add_policy("p", "g", ["alice", "data2_admin"])
# adapter.add_policy("p", "g", ["alice", "data2_admin"])
# adapter.add_policy("p", "g", ["alice", "data2_admin"])
# e.update_policy(["alice", "data1", "read"],["a
# e.update_policy(["alice", "data1", "read"],["alice", "data2", "write"])
# e.remove_policy(["bob", "data2","write"])
# adapter.remove_policy("p", "g", ["alice", "data2_admin"])

sub = "alice"  # 想要访问资源的用户
obj = "data2"  # 将要被访问的资源
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