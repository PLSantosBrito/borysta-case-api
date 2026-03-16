from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.routes.risk_routes import router
from app.exceptions import validation_exception_handler

app = FastAPI()

app.include_router(router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

app.add_exception_handler(RequestValidationError, validation_exception_handler)
