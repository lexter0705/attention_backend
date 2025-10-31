import asyncio
import base64
from logging import getLogger

import cv2

from api.models import CameraMessage
from api.tasks_manager import IdCreator
from api.tasks_manager.manager import TasksManager
from api.tasks_manager.task import Task


class Camera:
    def __init__(self, camera_message: CameraMessage,
                 task_manager: TasksManager,
                 id_creator: IdCreator,
                 active_framerate: int = 10,
                 inactive_framerate: int = 0.1,
                 width: int = 480,
                 height: int = 480):
        if not isinstance(camera_message, CameraMessage):
            raise TypeError("camera_message must be a CameraMessage")

        if not isinstance(task_manager, TasksManager):
            raise TypeError("task_manager must be a TasksManager")

        if not isinstance(id_creator, IdCreator):
            raise TypeError("id_creator must be a IdCreator")

        if active_framerate <= 0:
            raise ValueError("active_framate must be greater than 0")

        if inactive_framerate <= 0:
            raise ValueError("inactive_framerate must be greater than 0")

        self.__camera_id = camera_message.camera_id
        self.__video = camera_message
        self.__logger = getLogger()
        self.__current_task: Task | None = None
        self.__id_creator = id_creator
        self.__task_manager = task_manager
        self.__active_framerate = active_framerate
        self.__inactive_framerate = inactive_framerate
        self.__frame_rate = 1 / active_framerate
        self.__height = height
        self.__width = width
        self.__width_coefficient = 1
        self.__height_coefficient = 1

    async def read(self):
        if self.__current_task is None:
            video = cv2.VideoCapture(self.__video.camera_url)
            ret, frame = video.read()
            self.__height_coefficient = frame.shape[0] / self.__height
            self.__width_coefficient = frame.shape[1] / self.__width
            frame = cv2.resize(frame, (self.__height, self.__width))
            base64_bytes = base64.b64encode(frame.tobytes())
            task = Task(base64_bytes, self.__id_creator.id, self.__camera_id, frame.shape)
            self.__current_task = await self.__task_manager.send_task(task)
            await asyncio.sleep(self.__frame_rate)

    def to_inactive(self):
        self.__frame_rate = 1 / self.__inactive_framerate

    def to_active(self):
        self.__frame_rate = 1 / self.__active_framerate

    def close_task(self):
        self.__current_task = None

    @property
    def current_task(self):
        return self.__current_task

    @property
    def width_coefficient(self):
        return self.__width_coefficient

    @property
    def height_coefficient(self):
        return self.__height_coefficient
