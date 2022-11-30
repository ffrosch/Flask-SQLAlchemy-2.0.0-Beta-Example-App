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

    # The models are needed to initialize the db
    from . import models  # noqa

    with app.app_context():
        db.create_all()

    return app
