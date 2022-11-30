from flask import Flask

from .extensions import db


def create_app():
    """Initialize flask app.

    Returns
    -------
    Flask
        Flask app object
    """
    app = Flask(__name__)
    # In-Memory Database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    db.init_app(app)

    # The models are needed to initialize the db
    from . import models  # noqa

    with app.app_context():
        db.create_all()

    return app
