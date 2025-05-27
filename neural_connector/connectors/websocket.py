import asyncio
import json

from fastapi import WebSocket

from neural_connector.connectors.base import NeuralConnector
from neural_connector.statuses import Executed
from neural_connector.tasks import Task, Tasks


class WebsocketConnector(NeuralConnector):
    def __init__(self, tasks: Tasks):
        super().__init__(tasks)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        last_task: Task | None = None
        while True:
            task = self.tasks.get_not_executed_task()
            if task is not None and (last_task is None or isinstance(last_task.status, Executed)):
                last_task = task
                await websocket.send_json({"id": task.id, "image": str(task.image)})
            answer = await websocket.receive_json()
            self.tasks[answer["id"]].execute(answer)
            await asyncio.sleep(1)