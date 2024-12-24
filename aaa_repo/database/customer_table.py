from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from aaa_repo.database.db import SQLiteBase


class Customer(SQLiteBase):
    """
    Customer table
    """

    __tablename__ = "CUSTOMER"

    id: Mapped[int] = mapped_column("ID", Integer, default=None, primary_key=True)
    name: Mapped[str] = mapped_column("NAME", String, nullable=False)
    car_model: Mapped[str] = mapped_column("CAR_MODEL", String, nullable=True)
    license_number: Mapped[str] = mapped_column("LICENSE_NUMBER", String, nullable=True)
    is_premium_member: Mapped[bool] = mapped_column(
        "IS_PREMIUM_MEMBER", Boolean, nullable=True
    )
