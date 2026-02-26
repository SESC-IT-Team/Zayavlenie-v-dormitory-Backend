import uvicorn
from fastapi import FastAPI
from src.routers import router as main_router


app = FastAPI()
app.include_router(main_router)