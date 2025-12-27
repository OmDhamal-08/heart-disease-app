from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form
        
        # Create DataFrame
        input_data = pd.DataFrame([[
            float(data['age']),
            data['sex'],
            data['chestPainType'],
            float(data['restingBP']),
            float(data['cholesterol']),
            int(data['fastingBS']),
            data['restingECG'],
            float(data['maxHR']),
            data['exerciseAngina'],
            float(data['oldpeak']),
            data['stSlope']
        ]], columns=['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol',
                    'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina',
                    'Oldpeak', 'ST_Slope'])
        
        # Make prediction
        prediction = int(model.predict(input_data)[0])
        probability = float(model.predict_proba(input_data)[0][1])
        
        return jsonify({
            'success': True,
            'prediction': prediction,
            'probability': probability,
            'risk': 'High' if prediction == 1 else 'Low',
            'message': 'Consult a doctor!' if prediction == 1 else 'Low risk detected.'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)