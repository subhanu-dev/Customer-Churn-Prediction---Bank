import uvicorn  # ASGI
from fastapi import FastAPI


app = FastAPI()

# routers


@app.get("/")
def index():
    return {"message": "Churn Prediction for Bank"}


@app.get("/welcome")
def getname(name: str):
    return {"welcome to the churn prediction ": f"{name}"}


# running the api with uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn main:app --reload
