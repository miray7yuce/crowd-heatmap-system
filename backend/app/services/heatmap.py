# app/services/heatmap.py

import cv2
import numpy as np
from app.core.config import COLORMAP


def density_to_heatmap(density: np.ndarray) -> np.ndarray:
    """
    Density map -> BGR heatmap image
    """
    if density.max() <= 0:
        h, w = density.shape
        return np.zeros((h, w, 3), dtype=np.uint8)

    norm = density / (density.max() + 1e-6)
    heat = (norm * 255).astype(np.uint8)

    if COLORMAP == "JET":
        heat = cv2.applyColorMap(heat, cv2.COLORMAP_JET)
    else:
        heat = cv2.applyColorMap(heat, cv2.COLORMAP_HOT)

    return heat
