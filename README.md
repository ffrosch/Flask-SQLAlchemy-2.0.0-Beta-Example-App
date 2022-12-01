# Flask-SQLAlchemy 2.0.0 Beta

A basic example on how to use and structure a **flask** app using the new **SQLAlchemy 2**.

The `development.dev.txt` containts tools to ensure best coding practices during development.

This example app uses the new typechecking-friendly **SQLAlchemy 2** idiom for ORM class creation with `Mapper` and `mapped_column`.

The class attribute `__mapper_args__` supplies an example mechanism to automatically update the timestamp of a column.

The database backend is configured as a **SQLite In-Memory** database (`"sqlite://"`)

## Configuration

For development the `.flaskenv` file is used.
It is automatically loaded by flask's integrated webserver.

Configuration can be adjusted by creating a file `.env` in the root folder and setting values there.
The `.env` file will be loaded automatically by `config.py` and replace default settings.

The file `config.py` provides a basic configuration and should not be used for production.
It is way too easy to accidentially commit production settings to version control.

**Configuration resolution**

- Development: `commandline arguments` > `.env` > `.flaskenv` > `config.py`
- Production: `.env` > `config.py`

**Structure**

- [Static files](https://flask.palletsprojects.com/en/2.2.x/tutorial/static/) can be referenced relative to the apps `app/static` folder like so: `{{ url_for('static', filename='style.css') }}`

## Usage

1. Clone the repo, e.g. with the Github-CLI: `gh repo clone ffrosch/SQLAlchemy-2.0.0-Beta-Example-App`
1. Create a virtual environment for Python within the cloned repo: `python -m venv env`
1. Activate the virtual environment: `source env/bin/activate`

### Production

1. Install dependencies: `pip install -r requirements.txt`
1. Copy `.env.example` to `.env` and set the variables up for production
1. Setup a WSGI server

### Development

1. Install dependencies: `pip install -r requirements.dev.txt` (the normal requirements file will also be loaded and read)
1. Use the [flask cli](https://flask.palletsprojects.com/en/2.2.x/cli/) to serve the application in development & debug mode with `flask --debug run`
1. Use `flask shell` in the root folder to get an interactive shell.
   The shell is configured in `wsgi.py` (which is run by flask) and gives access to `db`, `Address`, `User`, `select` and `create_testdata()`.
1. Play around with these commands!

If you want to use **SQLAlchemy-Utils**, insert this code at the very top of the file:

```python
# flake8: noqa
import sqlalchemy

# Monkey-Patch version "2.0.0b3" to avoid sqlalchemy_utils init-error
sqlalchemy.__version__ = "2.0.0"
```

## Notes

In theory `nullable=True` and `Optional` should be equivalent.
So far this does not work with flask-sqlalchemy.

```
mapped_column() will derive additional arguments from the corresponding Mapped type annotation on the left side, if present. Additionally, Declarative will generate an empty mapped_column() directive implicitly, whenever a Mapped type annotation is encountered that does not have a value assigned to the attribute (this form is inspired by the similar style used in Python dataclasses); this mapped_column() construct proceeds to derive its configuration from the Mapped annotation present.
```

> Source: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-table
