# mypy: disable-error-code=name-defined
from datetime import datetime
from typing import List, Optional

from sqlalchemy import DateTime, ForeignKey, String, func, select
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, column_property, mapped_column, relationship

from .extensions import db


class TimestampMixin:
    created = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated = mapped_column(DateTime, nullable=False)

    __mapper_args__ = {
        "version_id_col": updated,
        "version_id_generator": lambda v: datetime.utcnow(),
    }


class User(TimestampMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    nickname: Mapped[Optional[str]] = mapped_column(String(50))
    fullname: Mapped[str] = column_property(
        firstname + " " + lastname  # type: ignore[operator]
    )
    # address_count: added at the end of the script

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    @hybrid_property
    def alias(self):
        if self.nickname is not None:
            return f"{self.nickname} ({self.firstname} {self.lastname})"
        else:
            return self.fullname

    def __repr__(self):
        return (
            f"User-ID: {self.id}, "
            f"Name: {self.fullname}, "
            f"E-Mail Addresses: {[a.email_address for a in self.addresses]}"
        )


class Address(TimestampMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    email_address: Mapped[str] = mapped_column(nullable=False)

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


User.address_count = column_property(
    select(func.count(Address.id))
    .where(Address.user_id == User.id)
    .scalar_subquery()
)
