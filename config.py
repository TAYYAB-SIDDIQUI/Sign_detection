import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "utils/models/train/weights/best.pt"

PORT = int(os.getenv("PORT", 1111))
DEBUG = os.getenv("DEBUG", "False") == "True"