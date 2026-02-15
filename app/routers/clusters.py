from fastapi import APIRouter, HTTPException

from app.data_loader import app_data
from app.schemas import ClusterSummary, ClusterDetail

router = APIRouter(prefix="/clusters", tags=["Clusters"])

@router.get("/", response_model=list[ClusterSummary])
def get_clusters():
    return [
        {"id": c["id"], "name": c["name"], "count": c["count"]}
        for c in app_data.clusters
    ]


@router.get("/{cluster_id}", response_model=ClusterDetail)
def get_cluster(cluster_id: int):
    for c in app_data.clusters:
        if c["id"] == cluster_id:
            return c
    raise HTTPException(status_code=404, detail="Cluster not found")