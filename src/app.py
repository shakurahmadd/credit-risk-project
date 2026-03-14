#import Flask
from flask import Flask  
from flask import render_template # return HTML form 
from flask import request 
import joblib 
import pandas as pd
import os


model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'rf_model.pkl')
loaded_model = joblib.load(model_path)

#__name__ tells Flask where to look for files like templates
app = Flask(__name__)

# add first route 
@app.route('/')
def index():
    return render_template('index.html') 
# find html file and send to browser 

@app.route('/predict', methods=['POST']) # only accepts POST requests (from form submissions)
def predict():
    data = pd.DataFrame([request.form], dtype=float)
    prediction = loaded_model.predict(data)
    probability = loaded_model.predict_proba(data)[0][1] * 100
    return render_template('result.html', prediction=int(prediction[0]), probability=f"{probability:.1f}")

# only run this code if this file is being directly, not imported by another file
if __name__ == '__main__':
    app.run(debug=False) # for development changed to false for deployment

