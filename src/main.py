from fastapi import FastAPI

from src.routers import router as router_crypt

app = FastAPI()
app.include_router(router_crypt)
