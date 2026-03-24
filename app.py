from flask import Flask, render_template, request

import joblib
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data=[
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['Blood Pressure']),
            float(request.form['Skin Thickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['Diabetes Pedigree Function']),
            float(request.form['Age'])
        ]
        prediction = model.predict([data])[0]
        result = "Diabetic" if prediction == 1 else "Non-Diabetic"
        return render_template('form.html', prediction_text=result)
    except Exception as e:
        return render_template('form.html', prediction_text="Invalid input")
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=True)