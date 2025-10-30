from api.models.box import Labels
from api.tasks_manager.statuses import Status, NotExecuted, Executed, Executing


class Task:
    def __init__(self, image: bytes, task_id: int, camera_id: int):
        self.__id = task_id
        self.__image = image
        self.__boxes: Labels | None = None
        self.__camera_id = camera_id
        self.__status: Status = NotExecuted()

    def start_execution(self):
        self.__status = Executing()

    def execute(self, boxes: Labels):
        if not isinstance(boxes, Labels):
            raise TypeError("boxes must be Labels")

        self.__boxes = boxes
        self.__status = Executed()

    @property
    def image(self) -> bytes:
        return self.__image

    @property
    def boxes(self) -> Labels | None:
        return self.__boxes

    @property
    def status(self) -> Status:
        return self.__status

    @property
    def id(self) -> int:
        return self.__id

    @property
    def camera_id(self) -> int:
        return self.__camera_id