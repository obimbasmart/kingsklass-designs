#!/usr/bin/python3

# """Category Module

# """

# from ..models.base_model import BaseModel, Base
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship, validates
# from ..models.product import product_category
# from ..exceptions.validation_exceptions import NonUniqueValueError

# class Category(BaseModel, Base):
#     __tablename__ = 'categories'
#     id = Column(String(128), nullable=False, primary_key=True)
#     products = relationship(
#         "Product", secondary=product_category, back_populates="categories")

#     @validates("id")
#     def validate_name(self, key, value):
#         from ..models import storage
#         all_names = [m.id for m in storage.all(Category).values()]
#         if value not in all_names:
#             return value
#         raise NonUniqueValueError(f"category: {value} already exist")
