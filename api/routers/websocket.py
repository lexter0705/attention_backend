import asyncio

from fastapi import APIRouter, WebSocket

from api.models import Image
from api.tasks_manager import IdCreator, TasksManager
from api.tasks_manager import NeuralConnector, UserConnector
from api.tasks_manager.statuses import Executed
from api.tasks_manager.task import Task
from config import ConfigReader

router = APIRouter(prefix="/websocket")

tasks_manager = TasksManager()
id_creator = IdCreator()
config = ConfigReader().read()


@router.websocket("/connect_neural")
async def connect_neural(websocket: WebSocket):
    neural_connector = NeuralConnector()
    tasks_manager.add_connector(neural_connector)
    await neural_connector.connect(websocket)


@router.websocket("/connect_user")
async def connect_user(websocket: WebSocket):
    user_connector = UserConnector(id_creator, tasks_manager, config)
    await user_connector.connect(websocket)


@router.post("/send_image")
async def send_image(image: Image):
    task = Task(image.image, id_creator.id, 1)
    task = await tasks_manager.send_task(task)
    while True:
        await asyncio.sleep(1)
        if isinstance(task.status, Executed):
            print(task.boxes.model_dump_json())
            break
    return task.boxes
