from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello from my API"}
employees = [
    {"id": 1, "name": "Fatima", "department": "IT"},
    {"id": 2, "name": "Ali", "department": "HR"},
    {"id": 3, "name": "Nora", "department": "Finance"}
]
@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}