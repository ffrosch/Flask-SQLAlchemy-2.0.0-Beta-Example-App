# mypy: disable-error-code=name-defined
from datetime import datetime
from typing import List, Optional

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, column_property, mapped_column, relationship

from .extensions import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[str] = column_property(
        firstname + " " + lastname  # type: ignore[operator]
    )

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")
    timestamp = mapped_column(DateTime, nullable=False)

    __mapper_args__ = {
        "version_id_col": timestamp,
        "version_id_generator": lambda v: datetime.now(),
    }

    def __repr__(self):
        return (
            f"User-ID: {self.id}, "
            f"Name: {self.fullname}, "
            f"Addresses: {[a.email_address for a in self.addresses]}"
        )


class Address(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    email_address: Mapped[str]
    address_statistics: Mapped[Optional[str]] = mapped_column(
        Text, deferred=True
    )

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return (
            "'"
            f"User-ID: {self.user.id}, "
            f"Name: {self.user.fullname}, "
            f"Address-ID: {self.id}, "
            f"E-Mail: {self.email_address}"
            "'"
        )
