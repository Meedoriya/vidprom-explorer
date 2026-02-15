import json
from pathlib import Path

import joblib
from sentence_transformers import SentenceTransformer

DATA_DIR = Path(__file__).parent.parent / "data"
MODELS_DIR = Path(__file__).parent.parent / "models"


def load_json(filename: str):
    with open(DATA_DIR / filename, "r") as f:
        return json.load(f)


class AppData:
    stats_overview: dict
    top_words: list
    clusters: list
    encoder: SentenceTransformer
    pca: object
    kmeans: object

    def load(self):
        self.stats_overview = load_json("stats_overview.json")
        self.top_words = load_json("top_words.json")
        self.clusters = load_json("clusters_summary.json")
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self.pca = joblib.load(MODELS_DIR / "pca50.joblib")
        self.kmeans = joblib.load(MODELS_DIR / "kmeans10.joblib")

app_data = AppData()