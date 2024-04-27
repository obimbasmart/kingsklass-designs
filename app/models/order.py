#!/usr/bin/python


from ..models.base_model import BaseModel
from sqlalchemy import Column, String, Enum, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.constants import default_measurement


ORDER_STATUS = Enum(
    'PENDING', 'COMFIRMED',
    'COMPLETED', 'IN_PRGRESS',
    'DELIVERED',
    name = 'OrderStatus'
)

ORDER_PROGRESES = Enum(
    'AWAITING_COMFIRMATION', 'MATERIAL_SOURCING',
    'CUTTING','SEWING', 'IRONING', 'PACKAGING',
    name='OrderStatus'
)


class Order(BaseModel):
    __tablename__ = 'orders'

    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    order_status = mapped_column(ORDER_STATUS, default='PENDING')
    order_progress = mapped_column(ORDER_PROGRESES, default='AWAITING_COMFIRMATION')

    additional_info = mapped_column(String(1024), nullable=True)
    measurements = mapped_column(JSON, default=default_measurement)
