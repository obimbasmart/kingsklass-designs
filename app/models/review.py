#!/usr/bin/python3

"""
Review Model
"""

from ..models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from ..models.user import User


class Review(BaseModel):    
    __tablename__ = 'reviews'
    product_id: Mapped[str] = mapped_column(String(60), ForeignKey('products.id'), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey(User.id), index=True, nullable=False)
    comment: Mapped[str] = mapped_column(String(1024),  nullable=False)
    rating: Mapped[str] = mapped_column(Integer, nullable=False)
