import uuid
import subprocess
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from app.core.paths import UPLOAD_DIR, OUTPUT_DIR
from app.services.video_processor import process_video

router = APIRouter(
    prefix="/video",
    tags=["video"]
)


@router.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    video_id = str(uuid.uuid4())

    input_path = UPLOAD_DIR / f"{video_id}_{file.filename}"

    # Geçici AVI
    temp_avi_path = OUTPUT_DIR / f"{video_id}_heatmap.avi"

    # Son MP4 
    output_mp4_path = OUTPUT_DIR / f"{video_id}_heatmap.mp4"

    # Save uploaded file
    with open(input_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Process video -> AVI
    process_video(
        input_video_path=str(input_path),
        output_video_path=str(temp_avi_path)
    )

    # AVI -> MP4 (faststart = browser streaming)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i", str(temp_avi_path),
            "-movflags", "+faststart",
            "-pix_fmt", "yuv420p",
            str(output_mp4_path)
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    temp_avi_path.unlink(missing_ok=True)

    return JSONResponse({
        "original_video": f"/static/uploads/{input_path.name}",
        "heatmap_video": f"/static/outputs/{output_mp4_path.name}"
    })
