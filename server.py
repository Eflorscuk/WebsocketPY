import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Mensagem recebida: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Servidor iniciado")
    try:
        await server.wait_closed()
    except KeyboardInterrupt:
        print("\nServidor interrompido pelo usuário")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServidor encerrado graciosamente")
