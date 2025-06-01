import asyncio

from connectors.base import WebsocketConnector
from tasks_manager.statuses import Executed
from tasks_manager.tasks import Task


class NeuralConnector(WebsocketConnector):
    def __init__(self):
        super().__init__()
        self.__last_task: Task | None = None

    async def update_socket(self):
        await self.websocket.send_text("is_connected")
        answer = await self.websocket.receive_json()
        if answer is not None and self.__last_task is not None:
            self.__last_task.execute(answer)
        await asyncio.sleep(1)

    async def send_task(self, task: Task):
        if self.is_have_task():
            raise Exception("NeuralConnector every have task")
        self.__last_task = self.__last_task
        await self.websocket.send_json({"id": task.id, "image": str(task.image)})

    def is_have_task(self):
        return self.__last_task is not None and not isinstance(self.__last_task.status, Executed)
