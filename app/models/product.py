#!/usr/bin/python

"""Product Module
"""

from ..models.base_model import BaseModel
from sqlalchemy import (
    String,
    Float, Integer,
    Boolean
)
from sqlalchemy.orm import (
    Mapped, relationship, mapped_column
)



class Product(BaseModel):
    __tablename__ = 'products'
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    price: Mapped[str] = mapped_column(Float,  nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=False)
    img_url: Mapped[str] = mapped_column(String(1024), nullable=False)
    estimated: Mapped[str] = mapped_column(Integer, nullable=True)
    on_draft: Mapped[str] = mapped_column(Boolean, default=False, nullable=False)

    # relationships
    reviews = relationship('Review', backref='product')
