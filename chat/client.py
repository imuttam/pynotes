import asyncio
import websockets

async def chat_client():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        print("Connected to the server")
        while True:
            message = input("Enter your message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Server says: {response}")

asyncio.run(chat_client())
