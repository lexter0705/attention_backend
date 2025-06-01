from connectors.base import WebsocketConnector
from tasks_manager import IdCreator, TasksManager
from tasks_manager.tasks import Task


class UserConnector(WebsocketConnector):
    def __init__(self, id_creator: IdCreator, task_manager: TasksManager):
        super().__init__()
        self.__id_creator = id_creator
        self.__task_manager = task_manager

    async def update_socket(self):
        data = await self.websocket.receive_json()
        task = Task(data["image"], self.__id_creator.id, 0)
        await self.__task_manager.add_task(task)
        executed_task = self.__task_manager.get_executed_task()
        if executed_task is not None:
            await self.websocket.send_json(executed_task.boxes["boxes"])
