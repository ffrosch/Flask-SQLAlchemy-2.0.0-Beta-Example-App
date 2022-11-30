# Flask-SQLAlchemy 2.0.0 Beta

A basic example on how to use and structure a **flask** app using the new **SQLAlchemy 2**.

The `development.dev.txt` containts tools to ensure best coding practices during development.

This example app uses the new typechecking-friendly **SQLAlchemy 2** idiom for ORM class creation with `Mapper` and `mapped_column`.

The class attribute `__mapper_args__` supplies an example mechanism to automatically update the timestamp of a column.

The database backend is configured as a **SQLite In-Memory** database (`"sqlite://"`)

## Usage

1. Clone the repo, e.g. with the Github-CLI: `gh repo clone ffrosch/SQLAlchemy-2.0.0-Beta-Example-App`
1. Create a virtual environment for Python within the cloned repo: `python -m venv env`
1. Activate the virtual environment: `source env/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
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
