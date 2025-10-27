import abc


class Status(abc.ABC):
    @abc.abstractmethod
    def __str__(self) -> str:
        pass