import uvicorn
from fastapi import FastAPI
from src.routers import router as main_router


app = FastAPI()
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)