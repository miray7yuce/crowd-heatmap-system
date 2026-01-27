# backend/app/services/heatmap.py

import cv2
import numpy as np

from app.core.config import HEATMAP_ALPHA, COLORMAP


def overlay_heatmap(frame, density_map):
    heatmap = np.uint8(255 * density_map)

    if COLORMAP == "JET":
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    else:
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_HOT)

    overlay = cv2.addWeighted(
        frame,
        1 - HEATMAP_ALPHA,
        heatmap,
        HEATMAP_ALPHA,
        0
    )

    return overlay
