#!/usr/bin/env python3


"""App Forms"""

from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import (
    StringField, EmailField, PasswordField, BooleanField,
    SubmitField, DecimalField
)
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app import db
import sqlalchemy as sa
from app.models.user import User
from app.constants import default_measurement


class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).one_or_none()
        if not user is None:
            raise ValidationError("Username already taken")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).one_or_none()
        if not user is None:
            raise ValidationError("Email already exist")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class EditProfileForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    username = StringField()
    phone = StringField()
    submit = SubmitField('Save')


class InputMeasurementForm(FlaskForm):
    top_length = DecimalField("Top Length", places=2)
    shoulder = DecimalField("Shoulder", places=2)
    sleeve_length = DecimalField("Sleeve Length", places=2)
    neck = DecimalField("Neck", places=2)
    muscle = DecimalField("Muscle", places=2)
    waist = DecimalField("Waist", places=2)
    laps = DecimalField("Laps", places=2)
    knee = DecimalField("Knee", places=2)
    stomach = DecimalField("Stomach", places=2)
    chest_burst = DecimalField("Chest/Burst", places=2)
    submit = SubmitField("Save")



# default=current_user.measurements.get("stomach"))