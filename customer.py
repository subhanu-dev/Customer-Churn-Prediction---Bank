from pydantic import BaseModel


class customer(BaseModel):
    credit_score: int
    age: int
    tenure: int
    balance: float
    products_number: float
    credit_card: int
    active_member: int
    estimated_salary: float
    zero_balance: int
    country_Germany: int
    country_Spain: int
    gender_Male: int
