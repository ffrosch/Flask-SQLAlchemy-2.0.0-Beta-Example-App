from flask import Flask

from config import Config

from .extensions import db


def create_app(config_class=Config):
    """Initialize flask app.

    Returns
    -------
    Flask
        Flask app object
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp

    app.register_blueprint(auth_bp)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    # The models are needed to initialize the db
    from . import models  # noqa

    with app.app_context():
        db.create_all()

    return app
