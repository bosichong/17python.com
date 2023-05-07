import time
import functools


def t(str):
    '''定义一个程序运行时间计算函数'''
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            start = time.time()  # 起始时间
            fun(*args, **kwargs)  # 要执行的函数
            end = time.time()  # 结束时间
            print('传入的字符串是:', str)
            print(fun.__name__, '程序运行时间:{:.2f}ms'.format((end - start) * 1000))
        return wrapper
    return decorator


@t('hello world')
def myfunc(x, y):
    '''打印从x到y的数值'''
    for i in range(x, y):
        print(i)


myfunc(0, 9)
