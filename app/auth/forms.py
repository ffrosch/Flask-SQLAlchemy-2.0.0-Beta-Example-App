# mypy: disable-error-code=import
from flask_wtf import FlaskForm
from sqlalchemy import select
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from app import db
from app.models import Address


class RegistrationForm(FlaskForm):
    firstname = StringField("Firstname", validators=[DataRequired()])
    lastname = StringField("Lastname", validators=[DataRequired()])
    email = StringField("E-Mail", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")

    def validate_email(self, email):
        address = db.session.execute(
            select(Address).filter(Address.email_address == email.data)
        ).first()
        if address is not None:
            raise ValidationError(
                "An account with this E-Mail address already exists."
            )
