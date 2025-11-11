# main training/inference code
# main.py

from ultralytics import YOLO
from config import config
import cv2
import os

def detect_objects(image_path):
    # Load YOLOv8 model
    model = YOLO(config.MODEL_PATH)

    # Run detection
    results = model.predict(
        source=image_path,  # path to image or folder
        conf=config.CONF_THRESHOLD,  # confidence threshold
        iou=config.IOU_THRESHOLD,    # IoU threshold
        save=True,                   # save results with bounding boxes
        project=config.OUTPUT_DIR,   # output folder
        name='detections'            # subfolder name
    )

    # Print results
    print("\n Detection complete!")
    print("Results saved in:", os.path.join(config.OUTPUT_DIR, "detections"))

    # Optional: display image using OpenCV
    img = cv2.imread(image_path)
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_image = os.path.join(config.DATA_DIR, "test_image.jpg")
    detect_objects(test_image)
