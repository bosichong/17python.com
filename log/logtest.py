from loguru import logger
import sys

LOG_LEVEL = "DEBUG"
logger.remove()  # 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
handler_id = logger.add(sys.stderr, level=LOG_LEVEL)  # 添加一个可以修改控制的handler

logger.info("来自test_a文件的logger日志。")
logger.debug("来自test_a文件的logger日志。")
