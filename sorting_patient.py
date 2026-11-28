from fastapi import FastAPI, Query, HTTPException, Path
import json

app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/sort")
async def sort_patient(sort_by: str = Query(...,description="Enter sorting value either age, gender or city"),
                       order: str = Query('asc',description="sort either in asc or desc")):
    valid_fields = ["age","gender","city"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code= 400, detail=f'Enter the specif value from {valid_fields}')
    if order not in ["asc","desc"]:
        raise HTTPException(status_code= 400, detail="Enter either asc or desc")

    data = load_data()

    sort_order = True if order == "desc" else False


    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse= sort_order)

    return sorted_data