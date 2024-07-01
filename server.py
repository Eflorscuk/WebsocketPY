import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Mensagem recebida: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Server started")
    await server.wait_closed()

asyncio.run(main())