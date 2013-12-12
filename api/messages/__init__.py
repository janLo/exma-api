from api.messages.ressources import MessageList, Message, FolderList
from flask import Blueprint
import flask_restful


def message_blueprint():
    message_bp = Blueprint("messages", __name__)

    message_api = flask_restful.Api()
    message_api.init_app(message_bp)

    message_api.add_resource(MessageList, "/", "/folder/<folder_id>")
    message_api.add_resource(Message, "/single/<message_topic_id>")
    message_api.add_resource(FolderList, "/folder")