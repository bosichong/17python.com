# codeing=utf-8

import argparse

'''
action="store_true"  参数可以为空


'''

parser = argparse.ArgumentParser(
    prog="Test", description="终端命令行测试", epilog="这是一个argparse的测试程序。")
parser.add_argument("aa", help="打印aaaaaaaa")
parser.add_argument("bb", help="打印bbbbbbbb")
parser.add_argument("-c", "--cc", help="打印aa+bb", action="store_true")
parser.add_argument("-d", "--dd", help="打印dddd")
args = parser.parse_args()

if args.cc:
    print(args.aa, args.bb)
elif args.dd:
    print(args.dd)
elif args.bb:
    print(args.bb)
elif args.aa:
    print(args.aa)

else:
    print(parser.print_help())  # 默认打印帮助
