from fastapi import APIRouter

from app.data_loader import app_data
from app.schemas import AnalyzeResponse, AnalyzeRequest

router = APIRouter(tags=["Analyze"])

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_prompt(req: AnalyzeRequest):
    embedding = app_data.encoder.encode([req.prompt])
    emb_50d = app_data.pca.transform(embedding)
    cluster_id = int(app_data.kmeans.predict(emb_50d)[0])

    cluster_name = "Unknown"
    for c in app_data.clusters:
        if c["id"] == cluster_id:
            cluster_name = c["name"]
            break

    return AnalyzeResponse(
        prompt_length=len(req.prompt),
        word_count=len(req.prompt.split()),
        cluster_id=cluster_id,
        cluster_name=cluster_name
    )