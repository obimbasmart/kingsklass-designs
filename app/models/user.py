#!/usr/bin/python

"""User Model
"""

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Boolean, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.constants import default_measurement
from ..models.base_model import BaseModel
from flask_login import UserMixin
from app import login_manager, db, app
import jwt
from time import time

class User(UserMixin, BaseModel):
    """User class """

    __tablename__ = 'users'
    first_name: Mapped[str] = mapped_column(String(128), nullable=True)
    last_name: Mapped[str] = mapped_column(String(128), nullable=True)
    username: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(String(128), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    phone_no: Mapped[str] = mapped_column(String(128), nullable=True)
    is_admin: Mapped[Boolean] = mapped_column(Boolean,  default=False)
    measurements = mapped_column(JSON, nullable=True,
                                 default=default_measurement)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_public_info(self):
        ignore_attrs = ["created_at", "updated_at"]
        return {
            attr: value
            for attr, value in super().to_dict().items()
            if attr not in ignore_attrs
        }
    
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return db.session.get(User, id)


@login_manager.user_loader
def load_user(id: str) -> User:
    return db.session.get(User, id)
