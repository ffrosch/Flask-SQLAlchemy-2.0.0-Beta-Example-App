from sqlalchemy import select

from app import create_app, db
from app.models import Address, User
from app.utils import TailwindCompiler, create_testdata

app = create_app()

# Run TailwindCSS as subprocess; watch for changes; build css on-the-fly
TailwindCompiler(app, debugmode_only=True)


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
