from pydantic import BaseModel


# Defining the input data model
class Customer(BaseModel):
    credit_score: int
    age: int
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float
    zero_balance: int
    country_Germany: int
    country_Spain: int
    gender_Male: int
