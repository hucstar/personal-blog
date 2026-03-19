from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

DEFAULT_CONFIG_OBJECT = "config.DevelopmentConfig"


def _init_extensions(app: Flask) -> None:
    """Initialize Flask extensions."""
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id: str):
        from app.models import User
        return User.query.get(int(user_id))


def _register_blueprints(app: Flask) -> None:
    """Register application blueprints."""
    from app.routes import main
    app.register_blueprint(main)


def create_app(config_object: str = DEFAULT_CONFIG_OBJECT) -> Flask:
    """Application factory."""
    app = Flask(__name__)
    app.config.from_object(config_object)

    _init_extensions(app)
    _register_blueprints(app)

    return app
