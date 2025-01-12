import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Response from server: {response}")

asyncio.run(hello())