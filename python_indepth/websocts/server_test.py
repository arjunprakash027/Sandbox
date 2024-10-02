import asyncio
import websockets

regestered_users = {}

async def handler(websocket):
    client_name = await websocket.recv()
    regestered_users[client_name] = websocket
    print(regestered_users)
    
    for user in regestered_users.values():
        try:
            await user.send("New user {} has joined the server.".format(client_name))
        except:
            print("error for {}".format(user))

    while True:
        message = await websocket.recv()
        print(message)

        for user in regestered_users.values():
            try:
                await user.send(message)
            except:
                print("error for {}".format(user))


        #print(websocket)

        # for user in regestered_users.values():
        #     try:
        #         await user.send(message)
        #     except:
        #         print("error for {}".format(user))

# async def reg_handler(websocket):

#     client_name = await websocket.recv()
#     regestered_users[client_name] = websocket
#     print(regestered_users)
    
#     for user in regestered_users.values():
#         try:
#             await user.send("New user {} has joined the server.".format(client_name))
#         except:
#             print("error for {}".format(user))


async def main():
    server1 = websockets.serve(handler, "", 8000)
    # server2 = websockets.serve(reg_handler, "", 8000)
    await asyncio.gather(server1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()

