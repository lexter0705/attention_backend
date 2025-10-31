import asyncio

from fastapi import WebSocket


class WebsocketConnector:
    def __init__(self, sleep_time: float = 1):
        self.__sleep_time = sleep_time
        self.__websocket: WebSocket | None = None

    async def __update_cycle(self):
        while True:
            await self.update_socket()
            await asyncio.sleep(self.__sleep_time)

    async def __recv_cycle(self):
        while True:
            await self.get_message()
            await asyncio.sleep(self.__sleep_time)

    async def connect(self, websocket: WebSocket) -> None:
        self.__websocket = websocket
        await websocket.accept()
        await self.on_start()
        await self.__update_cycle()
        await self.__recv_cycle()

    async def on_start(self):
        pass

    async def update_socket(self):
        pass

    async def get_message(self):
        pass

    @property
    def websocket(self) -> WebSocket:
        return self.__websocket
