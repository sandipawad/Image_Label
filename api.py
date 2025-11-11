# Fasfrom fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from config import config
import shutil
import os

# Initialize FastAPI app
app = FastAPI(title="YOLOv8 Object Detection API", version="1.0")

# Load YOLO model once when the server starts
model = YOLO(config.MODEL_PATH)

@app.get("/")
def root():
    return {"message": "Welcome to the YOLOv8 Object Detection API 🚀"}

@app.post("/detect/")
async def detect_objects_api(file: UploadFile = File(...)):
    """
    Upload an image to detect objects using YOLOv8
    """
    # Save uploaded image temporarily
    image_path = os.path.join(config.DATA_DIR, file.filename)
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run YOLO detection
    results = model.predict(
        source=image_path,
        conf=config.CONF_THRESHOLD,
        iou=config.IOU_THRESHOLD,
        save=True,
        project=config.OUTPUT_DIR,
        name="api_detections"
    )

    # Collect detections info (bounding boxes, labels, confidence)
    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls_id]
            detections.append({
                "label": label,
                "confidence": round(conf, 2)
            })

    # Clean up the uploaded image if you don’t need to keep it
    os.remove(image_path)

    # Return detection results
    return JSONResponse(content={
        "filename": file.filename,
        "detections": detections,
        "output_saved_to": os.path.join(config.OUTPUT_DIR, "api_detections")
    })
tAPI or Flask API to serve predictions