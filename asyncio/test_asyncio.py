import time
import  asyncio

async def display(num):
    await asyncio.sleep(2)
    print(num)

async def main():
    print("start")
    await asyncio.gather(*[display(i) for i in range(10)])
    print("end")
asyncio.run(main())

# ct = [display(num) for num in range(20)]#列表生成式
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(ct))
# loop.close()







