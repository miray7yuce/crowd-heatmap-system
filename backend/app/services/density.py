# app/services/density.py

import numpy as np
import cv2

from app.core.config import GAUSSIAN_SIGMA


def generate_density_map(points, frame_shape):
    h, w = frame_shape[:2]
    density = np.zeros((h, w), dtype=np.float32)

    if len(points) == 0:
        return density

    ksize = int(GAUSSIAN_SIGMA * 6) | 1
    kernel = cv2.getGaussianKernel(ksize, GAUSSIAN_SIGMA)
    kernel = kernel @ kernel.T

    for (x, y) in points:
        if 0 <= x < w and 0 <= y < h:
            x1 = max(0, x - ksize // 2)
            y1 = max(0, y - ksize // 2)
            x2 = min(w, x + ksize // 2 + 1)
            y2 = min(h, y + ksize // 2 + 1)

            kx1 = ksize // 2 - (x - x1)
            ky1 = ksize // 2 - (y - y1)
            kx2 = kx1 + (x2 - x1)
            ky2 = ky1 + (y2 - y1)

            density[y1:y2, x1:x2] += kernel[ky1:ky2, kx1:kx2]

    return density
