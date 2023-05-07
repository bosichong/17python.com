'''
Author: J.sky bosichong@qq.com
Date: 2021-06-05 10:21:58
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-21 10:02:33
FilePath: /PythonStudy/log/logtest.py
'''

from loguru import logger
import sys

LOG_LEVEL = "INFO"
logger.remove()  # 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
handler_id = logger.add(sys.stderr, level=LOG_LEVEL)  # 添加一个可以修改控制的handler

logger.info("来自test_a文件的logger日志。")
logger.debug("来自test_a文件的logger日志。")
