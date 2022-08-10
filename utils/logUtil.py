# -*- coding:utf-8 -*-
import datetime
import logging.config
import os
from utils import getPath

LOG_PATH = getPath.dirPath("log")
# 日志路输出文件
logPath = os.path.join(LOG_PATH,datetime.datetime.now().strftime('%Y-%m-%d') + ".log")

# 日志打印等级
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}
# 创建一个日志
logger = logging.getLogger()
level = 'info'

# 设置日志格式
formatter = logging.Formatter(
    "\n【%(asctime)s %(levelname)s %(message)s】", '%Y-%m-%d %H:%M:%S')

# 给logger添加handler 添加内容到日志句柄中
def set_handler():
    logger.addHandler(MyLog.fileHandler)

# 在记录日志之后移除句柄
def remove_handler():
    logger.removeHandler(MyLog.fileHandler)

class MyLog:
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    # 创建一个handler，用于写入日志文件
    fileHandler = logging.FileHandler(logPath, encoding='utf-8')
    fileHandler.setFormatter(formatter)
    @staticmethod
    def debug(log_meg):
        set_handler()
        # 文件中输出模式
        logger.debug(log_meg)
        remove_handler()

    @staticmethod
    def info(log_meg):
        set_handler()
        logger.info(log_meg)
        remove_handler()

    @staticmethod
    def warning(log_meg):
        set_handler()
        logger.warning(log_meg)
        remove_handler()

    @staticmethod
    def error(log_meg):
        set_handler()
        logger.error(log_meg)
        remove_handler()

    @staticmethod
    def critical(log_meg):
        set_handler()
        logger.error(log_meg)
        remove_handler()

    # 再创建一个handler，用于输出到控制台
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    console.setLevel(logging.NOTSET)


if __name__ == "__main__":
    MyLog.debug("This is debug message")
    MyLog.info("This is info message")
    MyLog.warning("This is warning message")
    MyLog.error("This is error")
    MyLog.critical("This is critical message")