import asyncio


async def task1():
    print("Fetching data....")
    await asyncio.sleep(2)
    print("Data returned....")
    return {"data", 100}


async def task2():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())
    data = await x
    print(data)
    await y


asyncio.run(main())
