from flask import Flask
from werkzeug.utils import find_modules, import_string

from api_result import ApiResult, ApiException
from models.db import db
import views

class ApiFlask(Flask):
    def make_response(self, return_value):
        if isinstance(return_value, ApiResult):
            return return_value.to_response()
        return Flask.make_response(self, return_value)


def create_app():
    app = ApiFlask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    register_blueprints(app)
    register_error_handlers(app)
    app.add_url_rule('/', 'home', views.home)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprints(app):
    for name in find_modules('myapp.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def register_error_handlers(app):
    app.register_error_handler(ApiException, lambda err: err.to_result())
