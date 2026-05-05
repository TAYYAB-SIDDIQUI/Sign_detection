from flask import Flask, jsonify, request
from Predict.models import load_yolo_model
from Predict.predict import detect_sign
import json, config

app = Flask(__name__)
try:
    model = load_yolo_model(config.MODEL_PATH)
    if isinstance(model, dict):
        if model.get('Error'): print(f"❌❌❌ Faced Error from load model : {model['Error']} ❌❌❌")
except Exception as e:print(f'❌❌❌ Faced Error: {str(e)} ❌❌❌')

@app.route('/', methods = ['GET'])
def index():
    try:
        if request.method == 'GET':
            index_path = 'utils/index.json'
            with open(index_path, 'r', encoding='utf-8') as f:
                index_output = json.load(f)
            return jsonify(index_output)
    except Exception as e:
        return jsonify({'Error': str(e)})
    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        if request.method == 'GET':
            return jsonify({'message': 'Service is running...'}), 200
        elif request.method == 'POST':
            if 'file' not in request.files:
                return jsonify({'Error':'NO file provided'}), 400
            file = request.files['file']
            if file.filename == '':
                return jsonify({'Error':'Empty File Name'}), 400
            if file.filename.lower().endswith(('jpg', 'jpeg', 'png')):
                result = detect_sign(file, model, 0.5)
                return jsonify(result)
            else:
                return jsonify({'Error':'File type not supported'})
    except Exception as e:
        return jsonify({'Error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=config.PORT)
