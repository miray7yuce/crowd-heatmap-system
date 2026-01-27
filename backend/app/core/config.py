# backend/app/core/config.py

# Video processing
TARGET_FPS = 15
MAX_FRAMES = None  # None = full video

# Detection
PERSON_CONF_THRESHOLD = 0.4

# Density map
GAUSSIAN_SIGMA = 15
DENSITY_NORMALIZATION_EPS = 1e-6

# Temporal smoothing
EMA_ALPHA = 0.6  # 0.0 → only past, 1.0 → only current

# Heatmap visualization
HEATMAP_ALPHA = 0.6
COLORMAP = "JET"

# Optical flow
FLOW_PYRAMID_SCALE = 0.5
FLOW_LEVELS = 3
FLOW_WINSIZE = 15
FLOW_ITERATIONS = 3
FLOW_POLY_N = 5
FLOW_POLY_SIGMA = 1.2
