from pydantic import BaseModel


class PromptLengthStats(BaseModel):
    mean: float
    median: float

class NsfwStats(BaseModel):
    toxicity: float
    obscene: float
    identity_attack: float
    insult: float
    threat: float
    sexual_explicit: float


class StatsOverview(BaseModel):
    total_prompts: int
    date_from: str
    date_to: str
    prompt_length: PromptLengthStats
    word_count: PromptLengthStats
    nsfw_above_05: NsfwStats


class WordCount(BaseModel):
    word: str
    count: int


class ClusterSummary(BaseModel):
    id: int
    name: str
    count: int

class ClusterDetail(BaseModel):
    id: int
    name: str
    count: int
    sample_prompts: list[str]