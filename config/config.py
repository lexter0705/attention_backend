from pydantic import BaseModel


class LabelsConfig(BaseModel):
    error_labels: list[str]
    warning_labels: list[str]


class Config(BaseModel):
    database_url: str
    labels: LabelsConfig
