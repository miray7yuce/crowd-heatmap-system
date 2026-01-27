# backend/app/core/paths.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

STATIC_DIR = BASE_DIR / "app" / "static"
UPLOAD_DIR = STATIC_DIR / "uploads"
OUTPUT_DIR = STATIC_DIR / "outputs"

MODEL_DIR = BASE_DIR / "app" / "models"
YOLO_MODEL_PATH = MODEL_DIR / "yolov8n.pt"

# Create directories if not exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
