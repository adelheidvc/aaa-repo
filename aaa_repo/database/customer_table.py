from sqlmodel import Field, Session, SQLModel, create_engine, select


class Customer(SQLModel, table=True):
    """
    Customer table
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str
    car_model: str
    license_number: str
    is_premium_member: bool | None = Field(default=None)