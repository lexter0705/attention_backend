from api.connectors.base import WebsocketConnector
from api.tasks_manager import Task
from api.tasks_manager.statuses import Executed


class NeuralConnector(WebsocketConnector):
    def __init__(self):
        super().__init__()
        self.__task: Task | None = None

    async def update_socket(self):
        answer = await self.websocket.receive_json()
        if answer is not None and self.__task is not None:
            self.__task.execute(answer)

    async def send_task(self, task: Task):
        if self.__task is None or isinstance(self.__task, Executed):
            raise Exception("NeuralConnector every have task")
        self.__task = task
        await self.websocket.send_json({"id": task.id, "image": str(task.image)})

    def is_have_task(self):
        return self.__task is not None
