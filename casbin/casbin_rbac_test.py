'''
Author: J.sky bosichong@qq.com
Date: 2022-10-28 15:10:55
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-28 16:04:10
FilePath: /PythonStudy/casbin/casbin_rbac_test.py
'''
from casbin_sqlalchemy_adapter import Adapter
from casbin_sqlalchemy_adapter import CasbinRule
import casbin
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from casbin_sqlalchemy_adapter import Base

import os,time

# model.conf 和 policy.csv 文件地址
model_dir = os.path.join(os.path.dirname(__file__), 'rbac_model.conf')

# 组装数据库的绝对地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'test_rbac.db')
# 数据库访问地址
SQLALCHEMY_DATABASE_URL = "sqlite:///" + DB_DIR
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=False)
print(os.path.exists(DB_DIR))
if os.path.exists(DB_DIR):
    Base.metadata.drop_all(engine)
    pass
else:
    Base.metadata.create_all(engine)
# 启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 从数据库加载casbin的policy
adapter = Adapter(engine)

def get_db():
    '''
    description: 获取一个数据连接 异步fastapi下使用.
    return ssesion
    '''    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



s = next(get_db())
s.query(CasbinRule).delete()
s.add(CasbinRule(ptype="p", v0="alice", v1="data1", v2="read"))
s.add(CasbinRule(ptype="p", v0="bob", v1="data1", v2="read"))
s.add(CasbinRule(ptype="p", v0="bob", v1="data1", v2="write"))
s.add(CasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="read"))
s.add(CasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="write"))
s.add(CasbinRule(ptype="g", v0="alice", v1="data2_admin"))
s.commit()
s.close()


def getEnforce():
    return casbin.Enforcer(model_dir, adapter)


# 每次提交完修改的数据,都要刷新e,用来加载新的验证规则
e = getEnforce()
sub = "alice"  # 想要访问资源的用户
obj = "data2"  # 将要被访问的资源
act = "read"  # 用户对资源进行的操作


assert e.enforce(sub, obj, act)

# 增加数据到数据库,可以保存到数据库 == add_policy
# 增加数据 必须保持数据为list或tuple,否则添加数据是会判断为不同的数据重复添加.
e.add_policy("eve", "data3", "read")
e.add_policy("eve", "data4", "read")
e.add_policy("eve", "data44", "read")
e.add_policy("eve", "data44", "read")
assert e.enforce("eve", "data3", "read")
e.add_permission_for_user("eve", "data3", "read")
e.add_permission_for_user("eve", "data4", "read")

# 批量增加数据
e.add_policies([["eve", "data3", "w"], ["eve", "data4", "w"]])

#  删除数据  == remove_policy
# e.delete_permission_for_user("eve", "data4", "read")
# assert not e.enforce("eve", "data4", "read")

# 批量删除数据库
e.add_policies((("alice", "data5", "read"), ("alice", "data6", "read")))
e.remove_policies((("alice", "data5", "read"), ("alice", "data6", "read")))

#  指定关键字删除,并不能在数据库里删除
# e.remove_filtered_policy(1, "data1")
# assert not e.enforce("alice", "data1", "read")

# 更新数据   批量更新 update_policies([old],[new])
e.update_policy(["alice", "data1", "read"], ["alice", "data1", "no_read"])
assert not e.enforce("alice", "data1", "read")


'''
以下这些操作基本都要操作casbin_rule数据库
想要访问资源的用户和角色组,在rbac中,只有role角色.
role create 正常添加 +++
role update casbin_rule中 v0 v1 字段数据存在此角色就得修改. +++
role delete casbin_rule中 v0 v1 字段数据存在此角色就得删除. +++

obj将要被访问的资源
object create 正常添加 ++++
object update casbin_rule中 v1 字段数据存在就得修改.资源只存在 v1字段 中.+++
object delete casbin_rule中 v1 字段数据存在就得删除.++++

action 用户对资源进行的操作,此表一般定义好后很少的几率修改和删除了.
action create 正常添加 +++
action update casbin_rule中 v2 字段数据存在就得修改.资源只存在 v2字段 中.+++
action delete casbin_rule中 v2 字段数据存在就得删除.+++

++++++++++++++++++++++++++++++++++++++++++++++++
为role与policy(资源权限)关系操作 用户组添修改删除加权限
权限组 所包含的权限需要搜索casbinrule ptype="p", v0=role_key
就可以返回权限组包含的权限
这里是权限管理的核心操作,此处应为多选框操作,选取一组资源权限.
无论角色权限的添加,修改,删除都是先删除原来的所有权限,
然后根据前端发来的数据重新添加权限给role

++++++++++++++++++++++++++++++++++++++++++++++
为用户增加角色role 添加 ptype=g 用户 角色
为用户修改角色 搜 ptype=g 用户名称v0 修改v1
删除用户角色  删除对应的ptype=g 用户 角色 的那条数据
为用户增加角色role 添加 ptype=g 用户 角色
一般角色修改只有添加这个外部动作,新建用户默认会有默认的角色,所以编辑角色管理,只是删除当前的角色,换成另外的角色.
所以操作步骤,删除当前的用户的角色,然后为用户添加新的角色.

'''


