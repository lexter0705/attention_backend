from neural_connector.statuses.base import Status


class Executed(Status):
    def __str__(self) -> str:
        return "Executed"