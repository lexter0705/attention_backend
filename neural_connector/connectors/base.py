import abc

from fastapi import WebSocket

from neural_connector.tasks import Tasks


class NeuralConnector(abc.ABC):
    def __init__(self, tasks: Tasks):
        self.__tasks = tasks

    @abc.abstractmethod
    async def connect(self, websocket: WebSocket):
        pass

    @property
    def tasks(self):
        return self.__tasks
