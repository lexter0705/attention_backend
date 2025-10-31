from typing import Literal

from pydantic import BaseModel


class ErrorMessage(BaseModel):
    camera_id: int
    object_name: str
    warning_type: Literal["error", "warning"]
    type: str = "warning"

