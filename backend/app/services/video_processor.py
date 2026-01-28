import cv2

from app.services.detector import PersonDetector
from app.services.density import generate_density_map
from app.services.heatmap import overlay_heatmap
from app.core.config import EMA_ALPHA
from app.utils.video_utils import get_video_writer


def process_video(input_video_path: str, output_video_path: str):
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        raise RuntimeError("Input video could not be opened")

    detector = PersonDetector()

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps is None or fps <= 0:
        fps = 25

    writer = None
    prev_density = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        points = detector.detect(frame)
        density = generate_density_map(points, frame.shape)

        # Temporal smoothing (EMA)
        if prev_density is None:
            smooth_density = density
        else:
            smooth_density = (
                EMA_ALPHA * density + (1 - EMA_ALPHA) * prev_density
            )

        prev_density = smooth_density

        output_frame = overlay_heatmap(frame, smooth_density)

        if writer is None:
            writer = get_video_writer(
                output_video_path,
                frame.shape[1],
                frame.shape[0],
                fps
            )

        writer.write(output_frame)

    cap.release()
    if writer:
        writer.release()
