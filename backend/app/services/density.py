# backend/app/services/density.py

import numpy as np
import cv2

from app.core.config import GAUSSIAN_SIGMA, DENSITY_NORMALIZATION_EPS


def generate_density_map(points, frame_shape):
    """
    points: list[(x,y)]
    frame_shape: (H,W,3)
    """
    h, w = frame_shape[:2]
    density = np.zeros((h, w), dtype=np.float32)

    for (x, y) in points:
        if 0 <= x < w and 0 <= y < h:
            density[y, x] += 1.0

    density = cv2.GaussianBlur(
        density,
        ksize=(0, 0),
        sigmaX=GAUSSIAN_SIGMA,
        sigmaY=GAUSSIAN_SIGMA
    )

    density /= (density.max() + DENSITY_NORMALIZATION_EPS)

    return density
