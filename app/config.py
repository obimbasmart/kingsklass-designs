#!/usr/bin/env python3

"""App Configurations
"""

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '463d18af-f326-40b7-a86b-785acd738d5f'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mail setup
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.sendgrid.net'
    MAIL_PORT = int(os.environ.get('MAIL_PORT')) or 587
    MAIL_USE_TLS =  True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "apikey"
    MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    ADMINS = ['emmapromisesmartnbc@gmail.com']

    # print(MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS, MAIL_USERNAME, MAIL_PASSWORD, MAIL_DEFAULT_SENDER, end="\n")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(os.environ.get("MYSQL_USER"),
                                                                   os.environ.get(
                                                                       "MYSQL_PWD"),
                                                                   os.environ.get(
                                                                       "MYSQL_HOST"),
                                                                   os.environ.get(
                                                                       "MYSQL_DB"),
                                                                   pool_pre_ping=True)
