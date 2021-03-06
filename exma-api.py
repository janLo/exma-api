from api import users, messages, albums, topics, representation, events
from api.users import authorization
from flask import Flask, request

import db_backend.mapping.config
import db_backend.mapping
import pixma_images


app = Flask(__name__)
Flask.secret_key = r"af4thei1VaongahB7eiloo]Push@ieZohz{o2hjo?w&ahxaegh2zood0rie3i"


@app.teardown_request
def shutdown_session(exception=None):
    """Cleanup the database session after a request.
    """
    db_backend.mapping.config.connection.session.remove()


@app.after_request
def add_cors_header(resp):
    #resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin") or "*"
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept"
    del resp.headers['WWW-Authenticate'] # = 'Basic realm="flask-restful'
    return resp


authorization.setup_auth(app, db_backend.mapping.DbMembers.by_id)
representation.configure_default_json()

@app.route('/')
def start():
    return 'eXma REST API!'


app.register_blueprint(users.make_blueprint())
app.register_blueprint(pixma_images.pixma_blueprint(), url_prefix="/piXma")
app.register_blueprint(topics.make_blueprint(), url_prefix="/topics")
app.register_blueprint(albums.make_blueprint(), url_prefix="/pixma")
app.register_blueprint(messages.make_blueprint(), url_prefix="/messages")
app.register_blueprint(events.make_blueprint(), url_prefix="/events")

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
