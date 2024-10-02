import asyncio
import itertools as it
import os
import random
import time

async def makeitem() -> str:
    return os.urandom(5).hex()

async def randomsleep(caller=None)->None:
    i = random.randint(0,10)
    if caller:
        print(f"{caller} sleeping for {i} secounds")
    
    await asyncio.sleep(i)

async def produce(name:int,q:asyncio.Queue) -> None:
    n = random.randint(0,10)
    for _ in it.repeat(None,n):
        await randomsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i,t))
        print(f"Producer {name} added <{i}> to queue.")

async def consumer(name:int,q:asyncio.Queue) -> None:
    while True:
        await randomsleep(caller=f"Consumer {name}")
        i,t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now-t:0.5f} seconds.")
              
        q.task_done()
        
async def main(nprod:int,ncon:int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n,q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consumer(n,q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()
        
if __name__ == "__main__":
    random.seed(444)
    start = time.perf_counter()
    asyncio.run(main(1,4))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")