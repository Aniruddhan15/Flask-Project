from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open('loadmodel.pkl','rb'))

@app.route('/')
def home():
    return "Hellow People"

@app.route('/predict', method=['POST'])
def predict():
    data = request.get_json(force=True)
    values = np.array(data['features']).reshape(-1,1)
    pred = model.predict(values)[0]
    
    return jsonify({'prediction values': round(pred,2)})

if __name__ == '__main__':
    app.run(debug=True)
    

    
    

    
    

