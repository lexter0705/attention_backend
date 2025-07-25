from connectors.neural import NeuralConnector
from tasks_manager.task import Task


class TasksManager:
    def __init__(self):
        self.__connectors: list[NeuralConnector] = []

    async def send_task(self, task: Task) -> Task | None:
        for connector in self.__connectors:
            if not connector.is_have_task():
                await connector.send_task(task)
                return task

    def add_connector(self, connector: NeuralConnector):
        if not isinstance(connector, NeuralConnector):
            raise ValueError("connector must be an instance of NeuralConnector")
        self.__connectors.append(connector)
