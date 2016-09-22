from datetime import datetime


def is_future(year, month, day, hour, minute, second):
    # 给定时间 大于 当前时间
    return (datetime(year, month, day, hour, minute, second) - datetime.now()).seconds > 0
