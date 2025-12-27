from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load model
model = None
try:
    model = joblib.load('heart_disease_model.pkl')
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({'success': False, 'error': 'Model not loaded'})
        
        # Get form data
        data = request.form
        
        # Prepare input data
        input_data = pd.DataFrame([[
            int(data['age']),
            data['sex'],
            data['chestPainType'],
            int(data['restingBP']),
            int(data['cholesterol']),
            int(data['fastingBS']),
            data['restingECG'],
            int(data['maxHR']),
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
            'message': 'High risk detected. Consult a doctor.' if prediction == 1 else 'Low risk. Maintain healthy lifestyle.'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'python_version': os.sys.version
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
