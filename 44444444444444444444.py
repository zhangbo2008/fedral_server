import time
import asyncio
from aiohttp import ClientSession
import requests
tasks = []
url = "https://www.baidu.com/{}"
async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
#            print(response)
#             print(requests.get(url))
            tmp=requests.get(url)
            print('Hello World:%s' % time.time())
            return  tmp

def run():
    for i in range(50):
        task = asyncio.ensure_future(hello(url.format(i))) # 对future对象进行封装
        tasks.append(task) # 把task放入tasks里面就行了.
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(len(result),'返回数据的长度')
    print(type(result))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()

    print('run other',"我要保证上面并发结果都收集到了之后才运行这句话")