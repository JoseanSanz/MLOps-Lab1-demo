# Generar una aplicación FastAPI que use las funciones de calculadora del módulo mylib.calculator
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from mylib.calculator import add, subtract, multiply, divide, power

# Crear instancia de FastAPI
app = FastAPI(
    title="API de Calculadora con FastAPI",
    description="API para realizar operaciones aritméticas básicas usando mylib.calculator",
    version="1.0.0",
)


# Modelo de entrada con Pydantic
class CalcRequest(BaseModel):
    operation: str
    a: float
    b: float


templates = Jinja2Templates(directory="templates")


# Endpoint raíz
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


# def home():
#     return {"message": "API FastAPI funcionando correctamente"}


# Endpoint principal para operaciones
@app.post("/calculate")
def calculate(data: CalcRequest):
    """
    Realiza una operación matemática según los parámetros recibidos.
    """
    op = data.operation.lower()
    a = data.a
    b = data.b

    if op not in ["add", "subtract", "multiply", "divide", "power"]:
        raise HTTPException(status_code=400, detail="Operación no válida")

    result = None
    if op == "add":
        result = add(a, b)
    elif op == "subtract":
        result = subtract(a, b)
    elif op == "multiply":
        result = multiply(a, b)
    elif op == "divide":
        if b == 0:
            raise HTTPException(
                status_code=400, detail="División por cero no permitida"
            )
        result = divide(a, b)
    elif op == "power":
        result = power(a, b)

    return {"result": result}


# Punto de entrada (solo para ejecución directa)
if __name__ == "__main__":
    uvicorn.run("api.fastapi_main:app", host="0.0.0.0", port=8000, reload=True)
