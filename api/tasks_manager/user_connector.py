from api.models import CameraStatus, Labels
from api.models.camera import CameraMessage
from api.tasks_manager import TasksManager
from api.tasks_manager.boxes_checker import BoxesChecker
from api.tasks_manager.camera import Camera
from api.tasks_manager.connector import WebsocketConnector
from api.tasks_manager.statuses import Executed
from api.tasks_manager.task import IdCreator
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
        self.__camera: Camera | None = None
        self.__boxes_checker = BoxesChecker(config.labels)

    def resize_boxes(self, labels: Labels) -> Labels:
        for box in labels.boxes:
            box.x1 = box.x1 * self.__camera.width_coefficient
            box.x2 = box.x2 * self.__camera.width_coefficient
            box.y1 = box.y1 * self.__camera.height_coefficient
            box.y2 = box.y2 * self.__camera.height_coefficient
        return labels

    async def on_start(self):
        data = await self.websocket.receive_json()
        data = CameraMessage.model_validate(data)
        self.__camera = Camera(data, self.__task_manager, self.__id_creator)

    async def get_message(self):
        data = await self.websocket.receive_json()
        if data is not None:
            if data["type"] == "url":
                data = CameraMessage.model_validate(data)
                self.__camera = Camera(data, self.__task_manager, self.__id_creator)
            elif data["type"] == "status":
                data = CameraStatus.model_validate(data)
                if data.status == "active":
                    self.__camera.to_active()
                if data.status == "not_active":
                    self.__camera.to_inactive()

    async def update_socket(self):
        if self.__camera is not None:
            await self.__camera.read()
            if self.__camera.current_task is not None and isinstance(self.__camera.current_task.status, Executed):
                task = self.resize_boxes(self.__camera.current_task.boxes)
                await self.websocket.send_json(task.model_dump_json())
                warns = self.__boxes_checker.check_boxes(task)
                for w in warns:
                    await self.websocket.send_json(w.model_dump_json())
                self.__camera.close_task()
