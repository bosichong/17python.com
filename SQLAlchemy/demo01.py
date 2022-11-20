#codeing=utf-8

from sqlalchemy import create_engine

# 通过SQLAlchemy中的create_engine()函数连接数据库
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

