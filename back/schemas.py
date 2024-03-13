from pydantic import BaseModel

class CategoryInput(BaseModel):
    title: str


class ItemCreateInput(BaseModel):
    xml_id: str
    eng_version: str
    ru_version: str
    category_id: int


class ItemPutInput(BaseModel):
    xml_id: str
    bel_version: str
    eng_version: str
    ru_version: str
    category_id: int