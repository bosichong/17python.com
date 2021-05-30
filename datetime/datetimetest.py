#codeing=utf-8
# @Time    : 2017-09-17
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python3 datetime模块的时间操作
# @Url     : http://www.17python.com/blog/16
# @Details : python3 datetime模块的时间操作
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
from datetime import *
###################################
# Python datetime 模块的时间操作。
###################################

# 获取当前时间
now = datetime.now()
td = datetime.today()
print(now, td)
# 格式化打印时间 格式字符串参见后边的附录。
format = "%Y-%m-%d %H:%M:%S"
print('今天的日期：'+ now.strftime(format))
# 根据字符串返回datetime对象
# 格式化的字符串应与前边的时间对应。比如："2017-09-18 13:02:34", "%Y-%m-%d %H:%M:%S"
print('strptime:{}'.format(datetime.strptime("2017-09-18", "%Y-%m-%d")))
#转换成时间戮
tmp = td.timestamp()
print('timestamp: {}'.format(tmp))
# 根据时间戮转换成datetime对象
print('fromtimestamp:{}'.format(datetime.fromtimestamp(tmp)))
# 星期几？0是星期一
print(now.weekday()+1)

# datetime 支持的最大及最小时间单位
print(datetime.max)
print(datetime.min)

# 打印datetime对象包含的一个tuple
for it in now.timetuple():
    print(it)

# 附录：格式字符串
# datetime. strftime (format)  
# %a 星期的简写。如 星期三为Web  
# %A 星期的全写。如 星期三为Wednesday  
# %b 月份的简写。如4月份为Apr  
# %B月份的全写。如4月份为April   
# %c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）  
# %d:  日在这个月中的天数（是这个月的第几天）  
# %f:  微秒（范围[0,999999]）  
# %H:  小时（24小时制，[0, 23]）  
# %I:  小时（12小时制，[0, 11]）  
# %j:  日在年中的天数 [001,366]（是当年的第几天）  
# %m:  月份（[01,12]）  
# %M:  分钟（[00,59]）  
# %p:  AM或者PM  
# %S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）  
# %U:  周在当年的周数当年的第几周），星期天作为周的第一天  
# %w:  今天在这周的天数，范围为[0, 6]，6表示星期天  
# %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天  
# %x:  日期字符串（如：04/07/10）  
# %X:  时间字符串（如：10:43:39）  
# %y:  2个数字表示的年份  
# %Y:  4个数字表示的年份  
# %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）  
# %Z:  时区名称（如果是本地时间，返回空字符串）  
# # %%:  %% => %  