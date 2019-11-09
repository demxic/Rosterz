from flask import Flask

from tripper.rest import station
from flask_settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(station.blueprint)
    return app
