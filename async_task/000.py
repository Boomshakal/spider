import asyncio
import time

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    # print(sleep_time)
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task
    # await tasks[1]
    # print('will print after tasks[2] awaited?')
    # await tasks[1]
    # await tasks[0]
    # print('will print after tasks[0] awaited?')
    # await tasks[3]
start = time.time()
asyncio.run(main(['url_1', 'url_5', 'url_4', 'url_3']))
end = time.time()
print('wall time:'+ str(end - start))
