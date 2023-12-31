# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:32:38 2023

@author: DarkPalad1n
"""

import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in # self created dummy file
import numpy as np
import pickle

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data["model"]
    return model

# Must be on top of predict function
app = Flask(__name__)
@app.route("/predict", methods = ["GET"])

def predict():
    # Stub input features
    request_json = request.get_json()
    x = request_json["input"]
    x_in = np.array(x).reshape(1, -1)
    # print(x)
    # Load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({"response": prediction})
    return response, 200

if __name__ == "__main__":
    application.run(debug = True)