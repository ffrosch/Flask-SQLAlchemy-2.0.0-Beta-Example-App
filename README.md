# Flask-SQLAlchemy 2.0.0 Beta

A basic example on how to use and structure a **flask** app using the new **SQLAlchemy 2**.

This example app uses the new typechecking-friendly **SQLAlchemy 2** idiom for ORM class creation with `Mapper` and `mapped_column`.

The class attribute `__mapper_args__` supplies an example mechanism to automatically update the timestamp of a column.

The database backend is configured as a **SQLite In-Memory** database (`"sqlite://"`)

## TODO

- [flask-talisman](https://github.com/GoogleCloudPlatform/flask-talisman) for setting HTTP headers
- [alembic](https://alembic.sqlalchemy.org/) for migrations, ALTER statements, etc.
- use sqlalchemy-utils [Model mixin](https://sqlalchemy-utils.readthedocs.io/en/latest/models.html) `generic_repr`
- implement Babel and/or SQLAlchemy-i18n/sqlalchemy-utils-TranslationHybrid

## Configuration

The app imports settings from `config.py`, which provides default values that are overriden by environment variables.

- development: `.flaskenv`
- production: `.env` (copy and adjust from `.env.example`)

The configuration resolution is `commandline arguments` > `.env` > (`.flaskenv`) > `config.py`.
In production the `.flaskenv` file will not be loaded!

**Structure**

- [Static files](https://flask.palletsprojects.com/en/2.2.x/tutorial/static/) can be referenced relative to the apps `app/static` folder like so: `{{ url_for('static', filename='style.css') }}`
- [Templates](https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/) are automatically found in the folder `app/templates`
- [Blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints/) and how they work with templates and static files

## Security

- CSRF: Include CSRF tokens on every view (e.g. with FlaskForm) -> no site can make your browser send a malicious request to another site with your credentials (because your browser would make the request triggered by the site, the browser would use your auth cookie and thus the site would think it was your request). If you are using something else than Flask-WTF, check whether you can configure the library to use a CSRF token by default for every request.

  > Basically for each request that modifies content on the server you would have to either use a one-time token and store that in the cookie and also transmit it with the form data. After receiving the data on the server again, you would then have to compare the two tokens and ensure they are equal. Why does Flask not do that for you? The ideal place for this to happen is the form validation framework, which does not exist in Flask. ([flask](https://flask.palletsprojects.com/en/2.2.x/security/#cross-site-request-forgery-csrf))

- CORS: Implement very strict acces control with the `Access-Control-Allow-Origin` HTTP headers to [mitigate](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) the risks of cross-origin HTTP requests
- CSP: [Content Security Policy](https://flask.palletsprojects.com/en/2.2.x/security/#security-csp) response header. This is important to set so that e.g. `<a href=` can't load javascript code
- [HTTP Security Headers](https://flask.palletsprojects.com/en/2.2.x/security/#security-headers) in general
- XSS: [Cross-Site Scripting](https://flask.palletsprojects.com/en/2.2.x/security/#cross-site-scripting-xss). This is needed to avoid injection of arbitrary HTML (and with it JavaScript) into the context of a website. All values must be properly escaped! Flask configures Jinja2 to do this automatically, so all templates should be safe. Jinja2 cannot prevent attribute injection in expressions like these `<input value={{ value }}>`. Solve this by always quoting your attributes `<input value="{{ value }}">`.
- SQL Injection: SQLAlchemy prevents this by quoting all data. Make sure to use proper [SQLAlchemy variable substitution](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#sending-parameters) so as to not bypass this mechanism!

## Usage

1. Clone the repo, e.g. with the Github-CLI: `gh repo clone ffrosch/SQLAlchemy-2.0.0-Beta-Example-App`
1. Create a virtual environment for Python within the cloned repo: `python -m venv env`
1. Activate the virtual environment: `source env/bin/activate`
1. Install `npm`
   ```bash
   wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
   source ~/.bashrc # Reload .bashrc
   ```
1. Install dependencies for CSS Framework Tailwind with `npm install`(installs everything from `package.json`)
1. Build the CSS files with `npm run build` (the build script is defined in `package.json`)

### Production

1. Install dependencies: `pip install -r requirements.txt`
1. Copy `.env.example` to `.env` and set the variables for production
1. Setup a WSGI server

### Development

During development two commandline instances are needed. One to run `flask --debug run` and one to run `npm run watch`.
This is important for making sure, that css classes that were not used before are added and rendered!

1. Install dependencies: `pip install -r requirements.dev.txt` (the normal requirements file will also be loaded and read)
1. Use the [flask cli](https://flask.palletsprojects.com/en/2.2.x/cli/) to serve the application in development & debug mode with `flask --debug run`
1. ... Or use `flask shell` in the root folder to get an interactive shell.
   The shell is configured in `wsgi.py` (which is run by flask) and gives access to `db`, `Address`, `User`, `select` and `create_testdata()`.
1. Auto-rebuild CSS files on changes in html-files with `npm run watch`

## Notes

If you want to use **SQLAlchemy-Utils** in a file, insert this code at the very top:

```python
# flake8: noqa
import sqlalchemy

# Monkey-Patch version "2.0.0b3" to avoid sqlalchemy_utils init-error
sqlalchemy.__version__ = "2.0.0"
```

In theory `nullable=True` and `Optional` should be equivalent.
So far this does not work with flask-sqlalchemy.

```
mapped_column() will derive additional arguments from the corresponding Mapped type annotation on the left side, if present. Additionally, Declarative will generate an empty mapped_column() directive implicitly, whenever a Mapped type annotation is encountered that does not have a value assigned to the attribute (this form is inspired by the similar style used in Python dataclasses); this mapped_column() construct proceeds to derive its configuration from the Mapped annotation present.
```

> Source: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-table
