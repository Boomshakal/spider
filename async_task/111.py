import asyncio
import time


now = lambda: time.time()


async def do_some_work(x):
    print('start:',x)
    await asyncio.sleep(2)
    print("waiting:", x)

start = now()

asyncio.run(do_some_work(2))
print("Time:",now()-start)
