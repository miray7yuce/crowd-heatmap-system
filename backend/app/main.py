from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.video_routes import router as video_router
from app.core.paths import STATIC_DIR

app = FastAPI(
    title="Video Crowd Heatmap API",
    version="1.0.0"
)

# ✅ CORS — BLazor için DOĞRU konfigürasyon
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5138"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)

# API routes
app.include_router(video_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "ok"}
