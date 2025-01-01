from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from aaa_repo.database.db import SQLiteBase
from aaa_repo.database.db import engine
from aaa_repo.database.db import DatabaseSession
from aaa_repo.responsemodels.customer import CustomerModel
from aaa_repo.responsemodels.customer import CreateCustomerModel
from aaa_repo.database.customer_table import Customer
from aaa_repo.database.breakdown_table import Breakdown


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Create tables
    """
    SQLiteBase.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


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


@app.put("/customer/{customer_id}", response_model=CustomerModel)
def update_customer(
    customer_id: int, updated_customer: CreateCustomerModel, db: DatabaseSession
):
    """
    Update Customer
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer.name = updated_customer.name
    customer.car_model = updated_customer.car_model
    customer.license_number = updated_customer.license_number
    customer.is_premium_member = updated_customer.is_premium_member
    db.commit()
    db.refresh(customer)
    return customer


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
