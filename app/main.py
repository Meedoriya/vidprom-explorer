from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.data_loader import app_data
from app.routers import clusters, stats, analyze


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_data.load()
    yield


app = FastAPI(title="VidProM Explorer API", lifespan=lifespan)
app.include_router(stats.router)
app.include_router(clusters.router)
app.include_router(analyze.router)


@app.get("/")
def root():
    return {"message": "VidProM Explorer API", "docs": "/docs"}