import requests
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

executor = ThreadPoolExecutor(10)

def getHtml(url):
    print("开始连接：{}".format(url))
    r = requests.get(url)
    print("{}  {}".format(url,r.status_code))
    print("{} 的requests 测试结束！！".format(url))

urls = ["http://2vv.net",
        "http://www.qq.com",
        "http://www.163.com",
        "http://www.sina.com.cn",
        "http://sports.sina.com.cn/nba/",
        "http://news.sina.com.cn/",
        "http://mil.news.sina.com.cn/",
        "http://news.sina.com.cn/society/",
        "http://news.sina.com.cn/world/",
        "http://finance.sina.com.cn/",
        "http://finance.sina.com.cn/stock/",
        "http://finance.sina.com.cn/fund/",
        "http://finance.sina.com.cn/forex/",
        "http://tech.sina.com.cn/",
        "http://mobile.sina.com.cn/",
        "http://tech.sina.com.cn/discovery/",
        "http://zhongce.sina.com.cn/"]

def main():
    print(f"started at {time.strftime('%X')}")
    for url in urls:
        executor.submit(getHtml,url)
    print(f"finished at {time.strftime('%X')}")

main()