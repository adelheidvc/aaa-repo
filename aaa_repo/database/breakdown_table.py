from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from aaa_repo.database.db import SQLiteBase
from aaa_repo.database.customer_table import Customer

class Breakdown(SQLiteBase):
    """
    Breakdown table
    """

    __tablename__ = "BREAKDOWN"

    breakdown_id: Mapped[int] = mapped_column("BREAKDOWN_ID", Integer, default=None, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("CUSTOMER.ID"))
    customer: Mapped[Customer] = relationship()
    moment_of_breakdown: Mapped[datetime] = mapped_column("MOMENT_OF_BREAKDOWN", String, nullable = False)
    description: Mapped[str] = mapped_column("DESCRIPTION", String, nullable = True)
    