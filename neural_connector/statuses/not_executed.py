from neural_connector.statuses.base import Status


class NotExecuted(Status):
    def __str__(self) -> str:
        return "NotExecuted"