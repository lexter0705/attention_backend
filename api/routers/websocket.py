from fastapi import APIRouter, WebSocket

from api.connectors import NeuralConnector, UserConnector
from api.tasks_manager import IdCreator, TasksManager

router = APIRouter(prefix="/websocket")

tasks_manager = TasksManager()
id_creator = IdCreator()


@router.websocket("/connect_neural")
async def connect_neural(websocket: WebSocket):
    neural_connector = NeuralConnector()
    tasks_manager.add_connector(neural_connector)
    await neural_connector.connect(websocket)


@router.websocket("/connect_user")
async def connect_user(websocket: WebSocket):
    user_connector = UserConnector(id_creator, tasks_manager)
    await user_connector.connect(websocket)
