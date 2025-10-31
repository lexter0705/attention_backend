import asyncio

from api.models.camera import Camera
from api.tasks_manager import TasksManager
from api.tasks_manager.boxes_checker import BoxesChecker
from api.tasks_manager.connector import WebsocketConnector
from api.tasks_manager.statuses import Executed
from api.tasks_manager.task import Task, IdCreator
from config import Config


class UserConnector(WebsocketConnector):
    def __init__(self, id_creator: IdCreator, task_manager: TasksManager, config: Config):
        if not isinstance(id_creator, IdCreator):
            raise TypeError("id_creator must be a IdCreator")

        if not isinstance(task_manager, TasksManager):
            raise TypeError("id_creator must be an instance of IdCreator")

        super().__init__()
        self.__id_creator = id_creator
        self.__task_manager = task_manager
        self.__last_task: Task | None = None
        self.__boxes_checker = BoxesChecker(config.labels)

    async def on_start(self):
        data = await self.websocket.receive_json()
        data = Camera.model_validate_json(data)

    async def update_socket(self):
        data = await self.websocket.receive_json()
        if self.__last_task is None:
            task = Task(data["image"], self.__id_creator.id, data["camera_id"])
            self.__last_task = await self.__task_manager.send_task(task)
        elif isinstance(self.__last_task.status, Executed):
            print(self.__last_task.status)
            await self.websocket.send_json(self.__last_task.boxes.model_dump_json())
            warns = self.__boxes_checker.check_boxes(self.__last_task.boxes)
            for w in warns:
                await self.websocket.send_json(w.model_dump_json())
            self.__last_task = None
