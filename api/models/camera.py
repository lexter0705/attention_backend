from typing import Literal

from pydantic import BaseModel


class CameraMessage(BaseModel):
    type: str = "url",
    camera_id: int
    camera_url: str


class CameraStatus(BaseModel):
    type: str = "status",
    status: Literal["active", "not_active"]
