import asyncio
import time


async def file_reply():
    await asyncio.sleep(4)
    return {"file returned", time.strftime('%X')}


async def data_reply():
    await asyncio.sleep(2)
    return {"data", 100}


async def task1():
    print(f"waiting for data from {time.strftime('%X')}")
    x = await data_reply()
    print(x)


async def task2():
    print("waiting for file.....")
    x = await file_reply()
    print(x)


async def main():
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())
    await x
    await y


asyncio.run(main())
