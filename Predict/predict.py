from tools.b64_to_img import is_base64_image, decode_base64_image
from PIL import Image
import numpy as np
def detect_sign(image, model, threshold=0.5):
    try:
        if isinstance(image, str) and is_base64_image(image):
            image = decode_base64_image(image)

        elif hasattr(image, "stream"):
            image = Image.open(image.stream).convert("RGB")
            image = np.array(image)

        elif isinstance(image, Image.Image):
            image = np.array(image)

        image = np.array(image)

        results = model(image, conf=threshold)
        if not results or len(results) == 0:
            return {"detections": []}
        result = results[0]
        detections = []
        if not hasattr(result, "boxes") or result.boxes is None:
            return {"detections": detections}
        for box in result.boxes:
            x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            label = model.names[class_id]

            detections.append({
                "label": label,
                "confidence": confidence,
                "bbox": {"x_min": x_min,"y_min": y_min,"x_max": x_max,"y_max": y_max}
            })

        return {"detections": detections}
    except Exception as e:
        return {'Error': str(e)}