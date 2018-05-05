import json

from flask import Flask, request, session
from data_source import DataSource
from web_api.utils.exceptions import TopicException


def create_app():
    flask_app = Flask(__name__)
    flask_app.secret_key = '9bc853e5-0e93-46aa-836a-1d1799f999c2'
    return flask_app


app = create_app()
data_source = DataSource(app)

# Views blueprint
from web_api.topics.views import TOPICS_BP
app.register_blueprint(TOPICS_BP, url_prefix='/topics')


@app.after_request
def after_request(response):
    '''
        1. setting response header
    '''
    if response.headers.get("Content-Length", "0") != "0" \
            and not 'admin' in request.path:
        response.headers["Content-Type"] = "application/json"

    session.clear()
    return response


@app.errorhandler(TopicException)
def handle_invalid_request_error(error):
    return json.dumps(error.to_dict()), error.status_code