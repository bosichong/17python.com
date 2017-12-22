#codeing=utf-8
# @Time    : 2017-12-22
# @Author  : py.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # Python生成器yield应用实例——监控日志
# @Url     : http://www.17python.com/blog/68
# @Details : # Python生成器yield应用实例——监控日志
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# Python生成器yield应用实例——监控日志
###################################
    import time

    def tail(f):
        f.seek(0,2)#移动到文件尾部。
        while True:
            line = f.readline()
            if not line :
                time.sleep(1)
                continue
            yield line

    def grep(lines):
        for l in lines:
            k = int(l.split()[2])
            if k >50000:
                yield l

    serverlog = tail(open('server_log.log'))
    lines = grep(serverlog)

    for line in lines:
        print(line)