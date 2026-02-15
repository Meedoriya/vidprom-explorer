import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_json(filename: str):
    with open(DATA_DIR / filename, "r") as f:
        return json.load(f)


class AppData:
    stats_overview: dict
    top_words: list
    clusters: list

    def load(self):
        self.stats_overview = load_json("stats_overview.json")
        self.top_words = load_json("top_words.json")
        self.clusters = load_json("clusters_summary.json")

app_data = AppData()