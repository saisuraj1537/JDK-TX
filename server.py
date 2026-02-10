from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()
clients: List[WebSocket] = []

@app.websocket("/control")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    print("Client connected")

    try:
        while True:
            data = await ws.receive_text()
            for client in clients:
                if client != ws:
                    await client.send_text(data)

    except:
        clients.remove(ws)
        print("Client disconnected")
