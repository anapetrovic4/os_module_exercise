from ultralytics import YOLO
from matplotlib import pyplot as plt
from PIL import Image

# Train model
model = YOLO('yolov8n-seg.yaml')
model = YOLO('yolov8n-seg.pt')

results = model.train(data='/mnt/c/projects/os_module_task/coco128-test-seg.yaml',
                      epochs=3,
                      batch=4,
                      imgsz=640)