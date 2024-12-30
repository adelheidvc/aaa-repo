from fastapi import FastAPI
from sqlalchemy import select
from aaa_repo.database.db import SQLiteBase
from aaa_repo.database.db import engine
from aaa_repo.database.db import DatabaseSession
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


@app.get("/customer/", response_model=list[CustomerModel])
def list_customer(db: DatabaseSession):
    """
    List all Customers
    """
    return db.query(Customer).all()


@app.get("/customer/{customer_id}", response_model=CustomerModel)
def read_customer(customer_id: int, db: DatabaseSession):
    """
    Read Customer
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    return customer


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


@app.post("/customer/", response_model=CustomerModel)
def create_customer(customer: CreateCustomerModel, db: DatabaseSession):
    """
    Create Customer
    """
    new_customer = Customer(
        name=customer.name,
        car_model=customer.car_model,
        license_number=customer.license_number,
        is_premium_member=customer.is_premium_member,
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
