#codeing=utf-8
# @Time    : 2017-09-10
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : Python 字符串格式化（%操作符）及format函数的使用
# @Url     : http://www.17python.com/blog/18
# @Details : Python 字符串格式化（%操作符）及format函数的使用,Python参考手册，字符串格式化章读书笔记。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1

# python的字符串操作是程序员编码中频繁使用的技巧，所以熟练掌握是可以影响到你的编码效率地。
# 目前比较流行的字符串打印有两种方式（据笔者所知，当然如果还有其它方法，请不吝赐教）：
# 一种是%符号操作，一种是format函数高级字符串格式化，两种各有特点，据说format的性能更好。

## %操作符的使用
a = 'hello'
b = 588
c = 12.7896
d = {'x':98, 'y':235.4444, 'z':'world',}
print("a:%s" % a)
# 10 和 2 是间隔的空格长度,小数点后的数字可以用来设置浮点数显示的精度，四舍五入，—号表示左对齐，+号是右对齐。
print("%-10d %2.3f" % (b, c)) 
print("%(x)-5d %(y).2f %(z).4s" % d)#打印字典中的值,.4s 表示要打印四个字符
#vars() 函数，它将返回当前定义的所有变量的字典
print ("%(a)s %(b)d %(c).2f %(d)s)" % vars())

## format函数高级字符串格式化
print("{0} {1} {2}".format(a,b,c))
print("{0},{b},{c}".format(a,b=b,c=c))
print("{0[x]} {0[y]} {0[z]}".format(d))

print("{0:>10.4s} {1:d}".format(a,b))# <>^ 这几个符号用来设置排版间隔
print("{0:10b}".format(b))#二进制整数
print("{0:,}".format(123456789))#,号用来做金额的千位分隔符。
