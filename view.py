from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def setup():
    return {"message":"hi its working"}

@app.get("/about")
def about():
    return {"message":"welcome to patients management system"}

@app.get("/view")
async def view_patients():
    data = load_data()
    return data