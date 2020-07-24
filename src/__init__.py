import os

from flask import Flask

def createApp(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        return 'hello world'

    return app
