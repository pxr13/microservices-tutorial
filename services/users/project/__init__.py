import os

from flask import Flask  # new
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
toolbar = DebugToolbarExtension()  # new


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)  # new

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
