from ultralytics import YOLO

def load_yolo_model(model_path):
    try:
        model = YOLO(model_path)
        return model
    except Exception as e:
        return {'Error': str(e)}
