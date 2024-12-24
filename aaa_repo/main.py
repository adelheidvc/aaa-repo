from fastapi import FastAPI
from aaa_repo.database.db import SQLiteBase
from aaa_repo.database.db import engine
from aaa_repo.responsemodels.customer import CustomerModel
from aaa_repo.responsemodels.customer import CreateCustomerModel
from aaa_repo.database.customer_table import Customer
from aaa_repo.database.breakdown_table import Breakdown


app = FastAPI()


@app.on_event("startup")
def on_startup():
    """
    Create tables
    """
    SQLiteBase.metadata.create_all(engine)


@app.get("/")
def read_root():
    """
    Read Root
    """
    return {"Hello": "This is your trusty AAA app"}


@app.get("/customer/{customer_id}")
def read_customer(customer_id: int, name: str | None = None):
    """
    Read Customer
    """
    return {"customer_id": customer_id, "name": name}


@app.put("/customer/{customer_id}")
def update_customer(customer_id: int, customer: CustomerModel):
    """
    Update Customer
    """
    return {
        "customer_id": customer_id,
        "customer_name": customer.name,
        "premium_member": customer.is_premium_member,
    }
