#!/usr/bin/python3
"""module for REST API entry point"""

from flask import Flask, jsonify, make_response
from app.config import DevConfig, Config, ProdConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def create_app(config=None) -> Flask:
    """create a flask app"""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)

    @app.errorhandler(404)
    def resource_not_found(self):
        """handle 404 error"""
        return make_response(jsonify({"error": "Not found"}), 404)

    return app

config = DevConfig
if getenv("APP_ENV") == "production":
    config = ProdConfig

app = create_app(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "app_views.login"
