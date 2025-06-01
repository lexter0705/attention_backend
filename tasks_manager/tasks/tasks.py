from tasks_manager.statuses import Executed
from tasks_manager.tasks import Task


class Tasks:
    def __init__(self):
        self.__tasks: list[Task] = []

    def add_task(self, task):
        self.__tasks.append(task)

    def get_first_executed(self):
        for i in range(len(self.__tasks)):
            if isinstance(self.__tasks[i].status, Executed):
                task = self.__tasks[i]
                self.__tasks.pop(i)
                return task
        return None

