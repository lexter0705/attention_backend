import asyncio

from fastapi import WebSocket


class WebsocketConnector:
    def __init__(self, sleep_time: float = 0.01):
        self.__sleep_time = sleep_time
        self.__websocket: WebSocket | None = None

    async def connect(self, websocket: WebSocket) -> None:
        self.__websocket = websocket
        await websocket.accept()
        await self.on_start()
        while True:
            await self.update_socket()
            await asyncio.sleep(self.__sleep_time)

    async def on_start(self):
        pass

    async def update_socket(self):
        pass

    @property
    def websocket(self) -> WebSocket:
        return self.__websocket
