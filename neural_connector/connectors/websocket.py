from starlette.websockets import WebSocket

from neural_connector.connectors.base import NeuralConnector
from neural_connector.tasks.tasks import Tasks


class WebsocketConnector(NeuralConnector):
    def __init__(self, tasks: Tasks):
        super().__init__(tasks)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        while True:
            task = self.tasks.get_not_executed_task()
            if task is not None:
                await websocket.send_json({"id": task.id, "bboxes": task.boxes})
            answer = await websocket.receive_json()
            self.tasks[answer["id"]].execute(answer["bboxes"])