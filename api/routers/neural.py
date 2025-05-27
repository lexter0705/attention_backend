from fastapi import APIRouter, WebSocket

from api.id_creator import IdCreator
from neural_connector import WebsocketConnector
from neural_connector.tasks import Tasks, Task

router = APIRouter(prefix="/websocket")

tasks = Tasks()

id_creator = IdCreator()


@router.websocket("/connect_neural")
async def connect_neural(websocket: WebSocket):
    connector = WebsocketConnector(tasks)
    await connector.connect(websocket)


@router.websocket("/connect_user")
async def connect_user(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        task = Task(data["image"], id_creator.id, 0)
        tasks.add_task(task)
        executed_task = tasks.get_executed_task()
        if executed_task is not None:
            await websocket.send_json(executed_task.boxes["boxes"])
