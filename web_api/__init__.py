from flask import Flask


def create_app():
    flask_app = Flask(__name__)

    return flask_app


app = create_app()

from web_api.topics.views import TOPICS_BP
app.register_blueprint(TOPICS_BP, url_prefix='/topics')
