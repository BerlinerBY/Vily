from pydantic import BaseModel
from typing import Optional

class CategoryInput(BaseModel):
    title: str


class ItemCreateInput(BaseModel):
    item_id: str
    bel_version: Optional[str] = None
    first_version: str
    second_version: Optional[str] = None
    category_id: int
    readiness: Optional[bool] = False
    context: Optional[str] = None


class ItemPutInput(BaseModel):
    bel_version: str
    readiness: bool