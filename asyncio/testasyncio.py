'''
Author: J.sky bosichong@qq.com
Date: 2021-02-02 15:59:34
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-12-02 20:12:51
FilePath: /PythonStudy/asyncio/testasyncio.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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

urls = [
        "http://www.qq.com",
        "http://www.163.com",
        "http://www.sina.com.cn",
        "http://www.baidu.com",
        "https://www.csdn.net/",
        "https://gitee.com/",
        "https://github.com/"
        ]
 
# async def main():
#     print("start")
#     await asyncio.gather(*[getHtml(url) for url in urls])
#     print("end")
# asyncio.run(main())


ct = [getHtml(url) for url in urls]#列表生成式
loop = asyncio.new_event_loop()
loop.run_until_complete(asyncio.wait(ct))
loop.close()


