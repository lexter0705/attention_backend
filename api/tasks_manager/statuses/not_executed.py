from api.tasks_manager.statuses.base import Status


class NotExecuted(Status):
    def __str__(self) -> str:
        return "NotExecuted"