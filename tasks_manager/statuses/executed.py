from tasks_manager.statuses.base import Status


class Executed(Status):
    def __str__(self) -> str:
        return "Executed"