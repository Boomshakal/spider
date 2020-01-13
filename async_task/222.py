import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
    print('start:',x)
    await asyncio.sleep(2)
    print("waiting:", x)

async def main(x):
    task = asyncio.create_task(do_some_work(x))

    await task

start = now()

asyncio.run(main(2))

print("Time:", now() - start)
