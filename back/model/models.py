from typing import List
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.sql import func

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
    date_updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"CategoryField(id={self.id!r}, title={self.title!r})"
    

class Item(Base):
    __tablename__ = "item"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    xml_id: Mapped[str]
    bel_version: Mapped[str] = mapped_column(String(), default="")
    eng_version: Mapped[str]
    ru_version: Mapped[str] 
    readiness: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    data_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    date_updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    category_id: Mapped[int] = mapped_column(ForeignKey("category_file.id"))
    category: Mapped["CategoryFile"] = relationship(back_populates="items")

    def __repr__(self) -> str:
        return f"Item(id={self.id!r}, xml_id={self.xml_id}, bel_version={self.bel_version}, eng_version={self.eng_version}, ru_version={self.ru_version})"
