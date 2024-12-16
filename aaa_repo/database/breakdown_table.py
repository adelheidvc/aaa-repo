from sqlmodel import Field, SQLModel


class Breakdown(SQLModel, table=True):
    """
    Breakdown table
    """
    breakdown_id: int | None = Field(default=None, primary_key=True)
    customer_id: str
    moment_of_breakdown: str
    description: str
    