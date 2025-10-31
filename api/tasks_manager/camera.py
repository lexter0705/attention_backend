import cv2

from logging import getLogger

from api.models import CameraMessage, CameraStatus
from api.tasks_manager.manager import TasksManager


class Camera:
    def __init__(self, camera_message: CameraMessage,
                task_manager: TasksManager,
                active_framrate: int = 60,
                inactive_framerate: int = 1):
        if not isinstance(camera_message, CameraMessage):
            raise TypeError("camera_message must be a CameraMessage")
            
        if not isinstance(task_manager, TasksManager):
            raise TypeError("task_manager must be a TasksManager")

        if not isinstance(ac)

        self.__camera_id = camera_message.camera_id
        self.__video = cv2.VideoCapture(camera_message.camera_url)
        self.__logger = getLogger()

    async def start(self):
        ret, frame = self.__video.read()

        if not ret:
            self.__logger.error("Camera read error")

        return frame