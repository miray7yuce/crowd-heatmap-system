import cv2
import numpy as np

from app.core.config import (
    FLOW_PYRAMID_SCALE,
    FLOW_LEVELS,
    FLOW_WINSIZE,
    FLOW_ITERATIONS,
    FLOW_POLY_N,
    FLOW_POLY_SIGMA
)


def compute_optical_flow(prev_gray, gray):
    flow = cv2.calcOpticalFlowFarneback(
        prev_gray,
        gray,
        None,
        FLOW_PYRAMID_SCALE,
        FLOW_LEVELS,
        FLOW_WINSIZE,
        FLOW_ITERATIONS,
        FLOW_POLY_N,
        FLOW_POLY_SIGMA,
        0
    )

    magnitude, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    magnitude = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX)

    return magnitude
