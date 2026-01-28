import numpy as np
from ultralytics import YOLO

from app.core.config import PERSON_CONF_THRESHOLD


class PersonDetector:
    """
    YOLOv8-based person detector.
    Model is downloaded and cached automatically by Ultralytics.
    """

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

        self.model.fuse()

    def detect(self, frame: np.ndarray):
        """
        Detect persons in a frame.

        Args:
            frame (np.ndarray): BGR image (OpenCV format)

        Returns:
            list[tuple[int, int]]: List of (cx, cy) center points
        """

        results = self.model(
            frame,
            conf=PERSON_CONF_THRESHOLD,
            classes=[0],  # COCO class 0 = person
            verbose=False
        )

        points: list[tuple[int, int]] = []

        for r in results:
            if r.boxes is None or len(r.boxes) == 0:
                continue

            boxes = r.boxes.xyxy.cpu().numpy()

            for x1, y1, x2, y2 in boxes:
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                points.append((cx, cy))

        return points
