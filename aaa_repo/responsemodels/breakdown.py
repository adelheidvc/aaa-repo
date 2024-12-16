from datetime import datetime
from pydantic import BaseModel


class BreakdownModel(BaseModel):
    """
    Breakdown Class
    """
    customer_id: int
    moment_of_breakdown: datetime
    description: str


class CreateBreakdownModel(BaseModel):
    """
    CreateBreakdown Class including breakdown_id
    """
    breakdown_id: int
    customer_id: int
    moment_of_breakdown: datetime
    description: str

