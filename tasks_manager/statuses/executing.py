from tasks_manager.statuses.base import Status


class Executing(Status):
    def __str__(self) -> str:
        return "Executing"