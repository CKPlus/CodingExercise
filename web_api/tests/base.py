from flask import Flask
from flask_testing import TestCase

from web_api import app


class BaseTestCase(TestCase):
    def create_app(self):
        return app
