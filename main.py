import os
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
app = FastAPI()
API_KEY = os.environ.get("API_KEY")
def check_key(x_api_key: str = Header(None)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
@app.get("/")
def home():
    return {"message": "Hello from my API"}
employees = [
    {"id": 1, "name": "Fatima", "department": "IT"},
    {"id": 2, "name": "Ali", "department": "HR"},
    {"id": 3, "name": "Nora", "department": "Finance"}
]
@app.get("/employees", dependencies=[Depends(check_key)])
def get_employees():
    return employees

@app.get("/employees/{employee_id}", dependencies=[Depends(check_key)])
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}
class NewEmployee(BaseModel):
    name: str
    department: str


@app.post("/employees", dependencies=[Depends(check_key)])
def add_employee(new:NewEmployee):
    new_id = max(e["id"] for e in employees) + 1
    employee = {
        "id":new_id,
        "name":new.name,
        "department": new.department
    }
    employees.append(employee)
    return employee
