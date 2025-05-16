from neural_connector.statuses import NotExecuted, Executed
from neural_connector.tasks.task import Task


class Tasks:
    def __init__(self):
        self.__tasks: list[Task] = []

    def get_not_executed_task(self) -> Task | None:
        for task in self.__tasks:
            if isinstance(task.status, NotExecuted):
                task.start_execution()
                return task

    def get_executed_task(self) -> Task | None:
        for task in self.__tasks:
            if isinstance(task.status, Executed):
                self.__tasks.remove(task)
                return task

    def __getitem__(self, item: int) -> Task:
        for task in self.__tasks:
            if task.id == item:
                return task
        raise KeyError

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError()
        self.__tasks.append(task)