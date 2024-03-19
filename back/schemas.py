from pydantic import BaseModel
from typing import Optional

class CategoryInput(BaseModel):
    title: str


class ItemCreateInput(BaseModel):
    xml_id: str
    bel_version: Optional[str] = None
    eng_version: str
    ru_version: str
    category_id: int


class ItemPutInput(BaseModel):
    bel_version: str
    readiness:bool