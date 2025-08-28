# create a flask app for salary prediction
# import the library
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# create a flask app
app = Flask(__name__)

# load the model
pipeline = pickle.load(open('Salary.pkl', 'rb'))

# create home page route 
@app.route('/')
def home():
    return render_template('index.html')

# create a predict route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Create DataFrame with correct column names
    df = pd.DataFrame([{
        'Age': data['age'],
        'Education Level': data['education'],
        'Years of Experience': data['experience']
    }])

    # Predict using the pipeline (expects DataFrame with correct columns)
    prediction = pipeline.predict(df)
    return jsonify({'salary': float(prediction[0])})

# run the app
if __name__ == '__main__':
    app.run(debug=False)
