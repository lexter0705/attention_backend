from neural_connector.statuses.base import Status


class Executing(Status):
    def __str__(self) -> str:
        return "Executing"