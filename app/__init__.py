import logging

from flask import Flask
from flask.logging import default_handler

from app.config import DevelopmentConfig
from app.controller.auth_controller import auth_blueprint
from app.controller.default_controller import default_blueprint
from app.controller.media_controller import media_blueprint
from app.controller.search_controller import search
from app.utils.encoder import DefaultEncoder


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig())
    app.logger.removeHandler(default_handler)

    app.register_blueprint(default_blueprint)
    app.register_blueprint(media_blueprint)
    app.register_blueprint(search)
    app.register_blueprint(auth_blueprint)

    return app
