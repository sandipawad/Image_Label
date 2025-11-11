# configuration settings (paths, model name, etc.)

import os

class Config:
    # Base directory of your project
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Data directory (where your images are stored)
    DATA_DIR = os.path.join(BASE_DIR, "data")

    # YOLO model path (you can change to your custom model if trained)
    MODEL_PATH = os.path.join(BASE_DIR, "model", "yolov8n.pt")

    # Output directory for saving results
    OUTPUT_DIR = os.path.join(BASE_DIR, "runs")

    # Detection settings
    CONF_THRESHOLD = 0.5  # confidence threshold
    IOU_THRESHOLD = 0.45  # intersection-over-union threshold

    # Create folders if they don't exist
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "model"), exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize config object
config = Config()