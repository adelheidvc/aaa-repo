from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Customer(BaseModel):
    """
    Customer Class
    """
    name: str
    is_premium_member: Union[bool, None] = None


@app.get("/")
def read_root():
    """
    Read Root
    """
    return {"Hello": "This is AAA"}


@app.get("/customer/{customer_id}")
def read_customer(customer_id: int, name: Union[str, None] = None):
    """
    Read Customer
    """
    return {"customer_id": customer_id, "name": name}


@app.put("/customer/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    """
    Update Customer
    """
    return {"customer_id": customer_id, "customer_name": customer.name, "premium_member": customer.is_premium_member}