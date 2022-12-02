from sqlalchemy import select

from app import create_app, db
from app.models import Address, User
from app.utils import create_testdata

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Register elements with the flask shell."""
    return {
        "db": db,
        "Address": Address,
        "User": User,
        "create_testdata": create_testdata,
        "select": select,
    }
