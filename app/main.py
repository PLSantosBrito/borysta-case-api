from fastapi import FastAPI

from app.routes.risk_routes import router


app = FastAPI()

app.include_router(router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}