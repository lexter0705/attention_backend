from pydantic import BaseModel


class Ids(BaseModel):
    need_ids: list[int]
    desirable_ids: list[int]
    main_id: int


class Config(BaseModel):
    database_path: str
    ids: Ids
