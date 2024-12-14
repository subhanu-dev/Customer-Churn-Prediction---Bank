import uvicorn  # ASGI
from fastapi import FastAPI

# modules for serving root files
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# iput data model class
from customer import Customer


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


# static folder for the frontend root endpoint
@app.get("/", response_class=HTMLResponse)
async def get_home():
    with open("./Frontend/index.html") as f:
        return f.read()


app.mount("/static", StaticFiles(directory="Frontend/static"), name="static")


@app.post("/predict")
async def predict_churn(data: Customer):
    df = pd.DataFrame(
        [data.dict().values()], columns=data.dict().keys()
    )  # converting input data into a DF

    scaled_features = scaler.transform(df)

    prediction = classifier.predict(scaled_features)
    # Get prediction probabilities
    probabilities = classifier.predict_proba(scaled_features)

    if prediction == 1:
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
