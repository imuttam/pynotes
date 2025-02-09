import asyncio
import websockets

connected_clients = set()

async def chat_handler(websocket, path):  # Accept path argument
    # Register the new client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all connected clients
            for client in connected_clients:
                if client != websocket:  # Don't echo back to the sender
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Remove the client on disconnect
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(chat_handler, "localhost", 6789)
    print("WebSocket server started at ws://localhost:6789")
    await server.wait_closed()

asyncio.run(main())
