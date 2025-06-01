import asyncio

from fastapi import WebSocket


class WebsocketConnector:
    def __init__(self):
        self.__websocket: WebSocket | None = None

    async def connect(self, websocket: WebSocket) -> None:
        self.__websocket = websocket
        await websocket.accept()
        await self.on_start()
        while True:
            await self.update_socket()
            await asyncio.sleep(1)

    async def on_start(self):
        pass

    async def update_socket(self):
        pass

    @property
    def websocket(self) -> WebSocket:
        if self.__websocket is None:
            raise Exception('Websocket not connected')
        return self.__websocket
