from pydantic import BaseModel


class CustomerModel(BaseModel):
    """
    Customer Class including id
    """

    id: int
    name: str
    car_model: str | None = None
    license_number: str | None = None
    is_premium_member: bool = False


class CreateCustomerModel(BaseModel):
    """
    CreateCustomer Class
    """

    name: str
    car_model: str
    license_number: str
    is_premium_member: bool = False
