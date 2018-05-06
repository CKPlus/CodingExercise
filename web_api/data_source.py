from flask import current_app


class DataSource(object):
    ''' Data store for this application '''
    data = {}

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        pass