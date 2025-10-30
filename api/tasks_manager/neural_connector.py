from pydantic import ValidationError

from logging import getLogger

from api.models.box import Labels
from api.tasks_manager.connector import WebsocketConnector
from api.tasks_manager.task import Task
from api.tasks_manager.statuses import Executed


class NeuralConnector(WebsocketConnector):
    def __init__(self):
        super().__init__()
        self.__task: Task | None = None
        self.__logger = getLogger(__name__)

    async def update_socket(self):
        answer = await self.websocket.receive_json()
        if answer is not None and self.__task is not None:
            answer = Labels.model_validate(answer)
            try:
                self.__task.execute(answer)
            except ValidationError:
                self.__logger.error("Answer from neural is not valid")

    async def send_task(self, task: Task):
        if  not (self.__task is None or isinstance(self.__task, Executed)):
            raise Exception("NeuralConnector every have task")

        self.__task = task
        self.__task.start_execution()
        await self.websocket.send_json({"id": task.id, "image": str(task.image)})

    def is_have_task(self):
        return self.__task is not None
