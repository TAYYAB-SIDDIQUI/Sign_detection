import base64
import numpy as np
from PIL import Image
import io

def is_base64_image(data):
    if not isinstance(data, str):
        return False

    if data.startswith("data:image"):
        return True

    # fallback heuristic
    return len(data) > 200

def decode_base64_image(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    return np.array(image)