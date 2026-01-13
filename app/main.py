from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Life Design Backend Service",
    description="Microservice for tracking user growth, consistency, and wellness optimization.",
    version="1.0.0"
)

app.include_router(router)