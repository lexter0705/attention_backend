from connectors.neural import NeuralConnector
from tasks_manager.tasks.task import Task
from tasks_manager.tasks.tasks import Tasks


class TasksManager:
    def __init__(self):
        self.__connectors: list[NeuralConnector] = []
        self.__tasks: Tasks = Tasks()

    async def add_task(self, task: Task):
        for connector in self.__connectors:
            if not connector.is_have_task():
                self.__tasks.add_task(task)
                await connector.send_task(task)

    def add_connector(self, connector: NeuralConnector):
        if not isinstance(connector, NeuralConnector):
            raise ValueError("connector must be an instance of NeuralConnector")
        self.__connectors.append(connector)

    @property
    def get_executed_task(self):
        return self.__tasks.get_first_executed()