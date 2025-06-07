from connectors.base import WebsocketConnector
from tasks_manager.statuses import Executed
from tasks_manager import Task


class NeuralConnector(WebsocketConnector):
    def __init__(self):
        super().__init__()
        self.__last_task: Task | None = None

    async def update_socket(self):
        answer = await self.websocket.receive_json()
        if answer is not None and self.__last_task is not None:
            self.__last_task.execute(answer)

    async def send_task(self, task: Task):
        if self.is_have_task():
            raise Exception("NeuralConnector every have task")
        self.__last_task = task
        await self.websocket.send_json({"id": task.id, "image": str(task.image)})

    def is_have_task(self):
        return not (self.__last_task is None or isinstance(self.__last_task.status, Executed))
