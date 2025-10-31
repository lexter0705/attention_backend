from typing import Literal

from pydantic import BaseModel


class CameraMessage(BaseModel):
    type: str
    camera_id: int
    camera_url: str


class CameraStatus(BaseModel):
    type: str
    status: Literal["active", "not_active"]
