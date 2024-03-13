from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship



class Base(
        DeclarativeBase,
        # MappedAsDataclass
        ):
    pass

class CategoryFile(Base):
    __tablename__ = "category_file"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    items: Mapped[List["Item"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"CategoryField(id={self.id!r}, title={self.title!r})"
    

class Item(Base):
    __tablename__ = "item"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    xml_id: Mapped[str]
    bel_version: Mapped[str] = mapped_column(String(), default="Empty")
    eng_version: Mapped[str]
    ru_version: Mapped[str] 

    category_id: Mapped[int] = mapped_column(ForeignKey("category_file.id"))
    category: Mapped["CategoryFile"] = relationship(back_populates="items")

    def __repr__(self) -> str:
        return f"Item(id={self.id!r}, xml_id={self.xml_id}, bel_version={self.bel_version}, eng_version={self.eng_version}, ru_version={self.ru_version})"
