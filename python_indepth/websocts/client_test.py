import asyncio
import websockets


async def send_messages(websocket):
    
    message = input("you:")
    await websocket.send(message)

async def recv_message(websocket):
    
    try:
        message = await websocket.recv()
        print(message)
    except:
        pass

async def regester(websocket):

    client_name = input("enter your name:")
    await websocket.send(client_name)


async def main():

    # async with websockets.connect("ws://localhost:8001/") as websocket_reg:
    #     #print(websocket_reg)
    #     recv_task = asyncio.create_task(recv_message(websocket_reg))
    #     reg_task = asyncio.create_task(regester(websocket_reg))
    #     await asyncio.gather(reg_task)
    # #print(recv_task)
        
    async with websockets.connect("ws://localhost:8000/") as websocket:
        
        reg_task = asyncio.create_task(regester(websocket))
        await asyncio.gather(reg_task)
        while True:
            recv_task = asyncio.create_task(recv_message(websocket))
            send_task = asyncio.create_task(send_messages(websocket))
            await asyncio.wait([send_task, recv_task], return_when=asyncio.FIRST_COMPLETED)

asyncio.run(main())