"""
download VidProM_unique.csv from HuggingFace and save to data/.
dataset: WenhaoWang/VidProM
"""
from datasets import load_dataset
from pathlib import Path
import os

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

output_path = DATA_DIR / "VidProM_unique.csv"

if output_path.exists():
    print(f"file already exists: {output_path}")
    print(f"size: {output_path.stat().st_size / 1e6:.1f} MB")
else:
    print("downloading VidProM dataset with HuggingFace...")
    ds = load_dataset("WenhaoWang/VidProM", data_files="VidProM_unique.csv", split="train")
    print(f"downloaded {len(ds)} strings")

    print(f"save to {output_path}...")
    ds.to_csv(str(output_path), index=False)
    print(f"done! size: {output_path.stat().st_size / 1e6:.1f} MB")