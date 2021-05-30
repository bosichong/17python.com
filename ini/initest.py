#codeing=utf-8
# @Time    : 2017-09-06
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : PythonINI配置文件读写的简单方法
# @Url     : http://www.17python.com/blog/14
# @Details : PythonINI配置文件读写的简单方法
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
import os
from configparser import ConfigParser
###################################
# .ini 文件是Initialization File的缩写，
# 即初始化文件，是windows的系统配置文件所采用的存储格式，
# 统管windows的各项配置，一般用户就用windows提供的各项图形化管理界面就可实现相同的配置了。
# 但在某些情况，还是要直接编辑ini才方便，一般只有很熟悉windows才能去直接编辑。
###################################
def readINI(file_path):
    """ ini文件读取，返回一个INI配置对象 """
    cfg = ConfigParser()
    cfg.read(file_path, encoding='utf-8')
    return cfg

def main():
    ini_file=os.path.join(os.path.dirname(__file__),'config.ini')#拼装配置文件目录
    c = readINI(ini_file)#读取加载ini文件配置
    #创建section及选项
    # c.add_section('cc')
    # c.set('cc','a','aa')
    # c.set('cc','b','bb')
    # c.set('cc','c','cc')
    for s in c.sections():#返回一个空间列表
        print('[{0}]'.format(s))
        for v in c.options(s):#打印列表下所有选项
            print('{0}={1}'.format(v,c.get(s,v)))
    #修改ini中的选项
    c.set('cc','a','ccc')#修改最后一组参数就会修改ini文件中对应的选项值
    #再次读取
    c.get('cc','a')
    #保存文件
    # ini = open(ini_file, mode='w', encoding='utf-8')
    # c.write(ini)
    # ini.close
    with open(ini_file, mode='w', encoding='utf-8') as ini:
        c.write(ini)
if __name__ == '__main__':
    main()
# configparser 还有一些其它方法，可以参考：
# 官方文档 http://python.usyiyi.cn/translate/python_352/library/configparser.html