from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    # General
    SECRET_KEY = environ.get("SECRET_KEY") or "you-will-never-guess"

    # Database
    SQLALCHEMY_DATABASE_URI = (
        environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite://"  # In-Memory
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
