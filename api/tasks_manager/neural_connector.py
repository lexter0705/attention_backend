from logging import getLogger

from numpy.ma.core import shape
from pydantic import ValidationError

from api.models.box import Labels
from api.tasks_manager.connector import WebsocketConnector
from api.tasks_manager.statuses import Executed
from api.tasks_manager.task import Task


class NeuralConnector(WebsocketConnector):
    def __init__(self):
        super().__init__()
        self.__task: Task | None = None
        self.__logger = getLogger(__name__)

    async def update_socket(self):
        answer = await self.websocket.receive_json()
        if answer is not None and self.__task is not None:
            try:
                answer = Labels.model_validate(answer)
                self.__task.execute(answer)
                self.__task = None
            except ValidationError:
                self.__logger.error("Answer from neural is not valid")

    async def send_task(self, task: Task):
        if not (self.__task is None or isinstance(self.__task, Executed)):
            raise Exception("NeuralConnector every have task")
        self.__task = task
        self.__task.start_execution()
        await self.websocket.send_json(
            {"id": task.id, "camera_id": self.__task.camera_id, "image": self.__task.image.decode('utf-8'), "shape": list(self.__task.shape)})

    def is_have_task(self):
        return self.__task is not None
