from sqlalchemy import select

from app import create_app, db
from app.models import Address, User

app = create_app()


def create_testdata():
    u = User(firstname="Peter", lastname="Mustermann")
    a1 = Address(user=u, email_address="peter@example.com")
    a2 = Address(user=u, email_address="mustermann@example.com")
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()


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
