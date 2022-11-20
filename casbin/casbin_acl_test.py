

from casbin import FileAdapter
import casbin
import os

# model.conf 和 policy.csv 文件地址
model_dir = os.path.join(os.path.dirname(__file__), 'model.conf')
policy_dir = os.path.join(os.path.dirname(__file__), 'policy.csv')

p_dir = FileAdapter(policy_dir)
# 加载配置文件
e = casbin.Enforcer(model_dir,p_dir)


# # 组装数据库的绝对地址
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_DIR = os.path.join(BASE_DIR, 'test.db')
# # 数据库访问地址
# SQLALCHEMY_DATABASE_URL = "sqlite:///" + DB_DIR
# # 从数据库加载casbin的policy
# adapter = casbin_sqlalchemy_adapter.Adapter(SQLALCHEMY_DATABASE_URL)
# e = casbin.Enforcer(model_dir, adapter)


p_dir.save_policy(["alice", "data3", "read"])
# e.update_policy(["alice", "data1", "read"],["alice", "data2", "write"])
# e.remove_policy(["alice", "data4","write"])

sub = "alice"  # 想要访问资源的用户
obj = "data1"  # 将要被访问的资源
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