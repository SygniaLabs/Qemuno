# -*- encoding: utf-8 -*-

from flask import Flask
from importlib import import_module


def register_blueprints(app):
    module = import_module('apps.{}.routes'.format('home'))
    app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app
