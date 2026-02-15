from fastapi import APIRouter
from app.schemas import StatsOverview, WordCount
from app.data_loader import app_data

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/overview", response_model=StatsOverview)
def get_overview():
    return app_data.stats_overview

@router.get("/top-words", response_model=list[WordCount])
def get_top_words(limit: int = 20):
    return app_data.top_words[:limit]