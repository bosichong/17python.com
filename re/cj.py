#codeing=utf-8
# @Time    : 2017-09-02
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python 采集数据三步曲之[Requests + re.py模块进行数据采集]
# @Url     : http://www.17python.com/blog/10
# @Details : Requests + re.py模块进行数据采集
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1

import re, requests # 加载所需模块
###################################
# 数据采集第一步，加载数据源。
###################################
r = requests.get('http://hq.sinajs.cn/list=s_sh000001') #互联网上市公司股票价格
r.encoding = 'gbk'# 设置编码 解决乱码问题
print(r.text) #返回html代码（数据）

###################################
# 数据采集第二步，解析数据，提取我们自己需要的。
###################################
s = r.text # 获取数据
p = r'"(.+)"' #设置正则表达式
r = re.search(p, s).group(1) #匹配并获取结果字符串
print(r)
ls = r.split(',')
print(ls)
#数据含义分别为：指数名称，当前点数，当前价格，涨跌率，成交量（手），成交额（万元）；

###################################
# 数据采集第三步，处理最后的打印
###################################

print('''{}:{}
当前价格:{}
涨跌率:{}
成交量（手）:{}
成交额（万元）:{}'''.format(ls[0],ls[1],ls[2],ls[3],ls[4],ls[5])
)