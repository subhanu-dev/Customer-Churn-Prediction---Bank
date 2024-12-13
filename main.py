import uvicorn  # ASGI
from fastapi import FastAPI

from customer import Customer

import numpy as np
import pandas as pd
import pickle  # pickle is built in


# creating the app object
app = FastAPI()

# accessing the pickle
pickle_in = open("churn_predictor.pkl", "rb")
classifier = pickle.load(pickle_in)

# loading the scaler
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)


# routers


@app.get("/")
def index():
    return {"message": "Churn Prediction for Bank"}


@app.get("/welcome")
def getname(name: str):
    return {"welcome to the churn prediction ": f"{name}"}


@app.post("/predict")
async def predict_churn(data: Customer):
    df = pd.DataFrame(
        [data.dict().values()], columns=data.dict().keys()
    )  # converting input data into a DF

    scaled_features = scaler.transform(df)

    prediction = classifier.predict(scaled_features)
    # Get prediction probabilities
    probabilities = classifier.predict_proba(scaled_features)

    if prediction[1]:
        customer_status = "The customer will churn"
    else:
        customer_status = "The customer will not churn"

    return {
        "prediction": customer_status,
        "probability": {
            "churn": round(probabilities[0][1], 2),  # Probability of churn (class 1)
            "not_churn": round(
                probabilities[0][0], 2
            ),  # Probability of not churn (class 0)
        },
    }


# running the api with uvicorn on localhost

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn main:app --reload