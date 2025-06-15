from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('loadmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',method=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.fit(features)[0]
    return render_template('index.html', result = f"Your predictions :{prediction}")




