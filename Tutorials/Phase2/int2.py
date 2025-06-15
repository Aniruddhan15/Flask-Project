from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('loadmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', method=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.fit([features])[0]
    return render_template('form.html', result = f'Your predictions: {prediction}')