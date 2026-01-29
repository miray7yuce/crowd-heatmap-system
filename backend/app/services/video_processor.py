# app/services/video_processor.py

import cv2
import numpy as np

from app.services.detector import PersonDetector
from app.services.density import generate_density_map
from app.services.heatmap import density_to_heatmap
from app.utils.video_utils import get_video_writer


DECAY = 0.97
ACCUM_GAIN = 1.0


def process_video(input_video_path: str, output_video_path: str):
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        raise RuntimeError("Input video could not be opened")

    detector = PersonDetector()
    fps = cap.get(cv2.CAP_PROP_FPS) or 25

    writer = None
    accumulated_density = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # İnsan noktaları
        points = detector.detect(frame)

        # Anlık density
        current_density = generate_density_map(points, frame.shape)

        # Zamansal birikme
        if accumulated_density is None:
            accumulated_density = current_density.copy()
        else:
            accumulated_density *= DECAY
            accumulated_density += ACCUM_GAIN * current_density

        # SADECE HEATMAP FRAME
        heatmap_frame = density_to_heatmap(accumulated_density)

        if writer is None:
            h, w = heatmap_frame.shape[:2]
            writer = get_video_writer(
                output_video_path,
                w,
                h,
                fps
            )

        writer.write(heatmap_frame)

    cap.release()
    if writer:
        writer.release()
