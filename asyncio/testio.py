'''
Author: J.sky bosichong@qq.com
Date: 2021-03-04 13:47:20
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-12-02 20:13:21
FilePath: /PythonStudy/asyncio/testio.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

executor = ThreadPoolExecutor(10)

def getHtml(url):
    print("开始连接：{}".format(url))
    r = requests.get(url)
    print("{}  {}".format(url,r.status_code))
    print("{} 的requests 测试结束！！".format(url))

urls = [
        "http://www.qq.com",
        "http://www.163.com",
        "http://www.sina.com.cn",
        "http://www.baidu.com",
        "https://www.csdn.net/",
        "https://gitee.com/",
        "https://github.com/"
        ]

def main():
    print(f"started at {time.strftime('%X')}")
    for url in urls:
        executor.submit(getHtml,url)
    print(f"finished at {time.strftime('%X')}")

main()