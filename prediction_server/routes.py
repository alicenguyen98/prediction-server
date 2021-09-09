import json
from flask import request, jsonify
from . import app
from . import config
from . import models_handler

@app.route('/', methods=['GET'])
def home():
    return ''

@app.route('/api/v1/info', methods=['GET'])
def info():
    response = {
        "models": models_handler.get_available_models()
    }
    return jsonify(response)

@app.route('/api/v1/predict', methods=['POST'])
def predict():
    response = None
    try:
        conf = config.get()

        # Check if there's a specified model, else check default model specified in config
        model = request.json.get('model', conf.get('default_model', None))
        if not model:
            raise Exception("No model selected")
        # Data
        params = request.json.get('params')

        # predict
        y_pred = models_handler.predict(model, params)

        response = {
            "prediction": y_pred
        }

    except Exception as err:
        print(f'Failed to handle prediction: {err}')
        response = {
            "error": str(err)
        }

    return jsonify(response)
