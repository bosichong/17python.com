import asyncio
import requests
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# executor = ThreadPoolExecutor(10)

async def getHtml(url):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, print, "开始连接{}".format(url))
    r = await loop.run_in_executor(None, requests.get, url)
    # r = await loop.run_in_executor(executor, requests.get, url)
    
    print("{}  {}".format(url,r.status_code))
    print("{} 的requests asyncio 测试结束！！".format(url))

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
 
async def main():
    print("start")
    await asyncio.gather(*[getHtml(url) for url in urls])
    print("end")
asyncio.run(main())


# ct = [getHtml(url) for url in urls]#列表生成式
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(ct))
# loop.close()


