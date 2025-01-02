from datetime import datetime
from pydantic import BaseModel
from aaa_repo.responsemodels.customer import CustomerModel


class BreakdownModel(BaseModel):
    """
    Breakdown Class including breakdown_id
    """

    breakdown_id: int
    customer_id: int
    customer: CustomerModel
    moment_of_breakdown: datetime
    description: str


class CreateBreakdownModel(BaseModel):
    """
    CreateBreakdown Class
    """

    customer_id: int
    moment_of_breakdown: datetime
    description: str


class PatchBreakdownModel(BaseModel):
    """
    PatchBreakdown Class
    """

    customer_id: int | None = None
    moment_of_breakdown: datetime | None = None
    description: str | None = None
