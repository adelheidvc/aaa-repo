from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from aaa_repo.database.db import SQLiteBase
from aaa_repo.database.db import engine
from aaa_repo.database.db import DatabaseSession
from aaa_repo.responsemodels.customer import CustomerModel, CreateCustomerModel
from aaa_repo.database.customer_table import Customer
from aaa_repo.database.breakdown_table import Breakdown
from aaa_repo.responsemodels.breakdown import BreakdownModel, CreateBreakdownModel


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

@app.get("/breakdown/", response_model=list[BreakdownModel])
def list_breakdown(db: DatabaseSession):
    """
    List all Breakdowns
    """
    return db.query(Breakdown).all()


@app.get("/customer/{customer_id}", response_model=CustomerModel)
def read_customer(customer_id: int, db: DatabaseSession):
    """
    Read Customer
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    return customer

@app.get("/breakdown/{breakdown_id}", response_model=BreakdownModel)
def read_breakdown(breakdown_id: int, db: DatabaseSession):
    """
    Read Breakdown
    """
    breakdown = db.query(Breakdown).filter(Breakdown.breakdown_id == breakdown_id).first()
    return breakdown


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

@app.put("/breakdown/{breakdown_id}", response_model=BreakdownModel)
def update_breakdown(
    breakdown_id: int, updated_breakdown: CreateBreakdownModel, db: DatabaseSession
):
    """
    Update Breakdown
    """
    breakdown = db.query(Breakdown).filter(Breakdown.breakdown_id == breakdown_id).first()
    if breakdown is None:
        raise HTTPException(status_code=404, detail="breakdown not found")
    breakdown.customer_id = updated_breakdown.customer_id
    breakdown.moment_of_breakdown = updated_breakdown.moment_of_breakdown
    breakdown.description = updated_breakdown.description
    db.commit()
    db.refresh(breakdown)
    return breakdown


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

@app.post("/breakdown/", response_model=BreakdownModel)
def create_breakdown(breakdown: CreateBreakdownModel, db: DatabaseSession):
    """
    Create Breakdown
    """
    new_breakdown = Breakdown(
        customer_id=breakdown.customer_id,
        moment_of_breakdown=breakdown.moment_of_breakdown,
        description=breakdown.description,
    )
    db.add(new_breakdown)
    db.commit()
    db.refresh(new_breakdown)
    return new_breakdown
