import uvicorn  # ASGI
from fastapi import FastAPI

from customer import Customer

import numpy as np
import pandas as pd
import pickle # pickle is built in


#creating the app object
app = FastAPI()

#accessing the pickle
pickle_in = open("churn_predictor.pkl","rb")
classifier = pickle.load(pickle_in)

# routers


@app.get("/")
def index():
    return {"message": "Churn Prediction for Bank"}


@app.get("/welcome")
def getname(name: str):
    return {"welcome to the churn prediction ": f"{name}"}


@app.post("/predict")
def predict_churn(data:Customer):
    data=data.dict()
    print(data)
    print('hello subhanu')
    credit_score = data['credit score']
    age= data['age']
    tenure=data['tenure']
    balance=data['balance']
    products_number= data['products number']
    credit_card=data['credit card']
    active_member=data['age']
    estimated_salary=data['estimated salary']
    zero_balance=data['zero balance']
    country_Germany=data['country Germany']
    country_Spain=data['country Spain']
    gender_Male=data['gender_Male']
    prediction =classifier.predict([[credit_score,age,tenure,balance, products_number,credit_card,active_member,estimated_salary,zero_balance,country_Germany,country_Spain,gender_Male]])
    if(prediction[1]):
        prediction = "The customer will churn"
    else:

# running the api with uvicorn on localhost

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn main:app --reload
