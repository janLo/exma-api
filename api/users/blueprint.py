from api.request_helper import charset_fix_decorator
from api.users.ressources import Login, Logout
from flask import Blueprint
import flask_restful


def user_blueprint():
    user_bp = Blueprint("user", __name__)

    user_api = flask_restful.Api(decorators=[charset_fix_decorator])
    user_api.init_app(user_bp)

    user_api.add_resource(Login, "/login")
    user_api.add_resource(Logout, "/logout")

    return user_bp