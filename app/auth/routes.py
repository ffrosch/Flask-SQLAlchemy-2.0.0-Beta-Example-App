from flask import flash, redirect, render_template, url_for

from app import db
from app.auth import bp
from app.auth.forms import RegistrationForm
from app.models import Address, User


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.addresses.append(Address(email_address=form.email.data))
        db.session.add(user)
        db.session.commit()
        flash("User successfully registered!")
        return redirect(url_for("main.index"))
    return render_template("auth/register.html", title="Register", form=form)
