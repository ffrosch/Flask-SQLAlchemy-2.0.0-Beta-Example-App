import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL", "").replace(
            "postgres://", "postgresql://"
        )
        or "sqlite://"  # In-Memory Database
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
