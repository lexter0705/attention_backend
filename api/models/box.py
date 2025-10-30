from pydantic import BaseModel


class Label(BaseModel):
    name: str
    x1: float
    x2: float
    y1: float
    y2: float


class Labels(BaseModel):
    type: str = "labels"
    camera_id: int
    boxes: list[Label]
