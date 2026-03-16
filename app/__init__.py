from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Load configurations from a config file

    # Initialize plugins/extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints, routes, etc.

    return app
