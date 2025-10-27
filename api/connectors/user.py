from api.connectors.base import WebsocketConnector
from api.tasks_manager import IdCreator, TasksManager
from api.tasks_manager.statuses import Executed
from api.tasks_manager import Task


class UserConnector(WebsocketConnector):
    def __init__(self, id_creator: IdCreator, task_manager: TasksManager):
        super().__init__()
        self.__id_creator = id_creator
        self.__task_manager = task_manager
        self.__last_task: Task | None = None

    async def update_socket(self):
        data = await self.websocket.receive_json()
        if self.__last_task is None:
            task = Task(data["image"], self.__id_creator.id, 0)
            self.__last_task = await self.__task_manager.send_task(task)
        elif isinstance(self.__last_task.status, Executed):
            await self.websocket.send_json(self.__last_task.boxes["boxes"])
            self.__last_task = None