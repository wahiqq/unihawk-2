"""
API for Insurance Cost Prediction
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Add the current directory to path to import the modules
sys.path.append(str(Path(__file__).parent))
from prediction import predict_insurance_cost

@app.route('/api/models', methods=['GET'])
def get_available_models():
    """
    Return a list of available trained models
    """
    model_files = Path('.').glob('*.pkl')
    models = [file.stem for file in model_files if file.stem not in ['preprocessor']]
    return jsonify({'models': models})

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    API endpoint to predict insurance cost
    """
    try:
        # Get data from request
        data = request.get_json()
        
        # Extract features
        age = int(data['age'])
        sex = data['sex']
        bmi = float(data['bmi'])
        children = int(data['children'])
        smoker = data['smoker']
        region = data['region']
        model_name = data.get('model_name', 'gradient_boosting')
        
        # Validate inputs
        if age < 0 or age > 120:
            return jsonify({'error': 'Age must be between 0 and 120'}), 400
        
        if bmi < 10 or bmi > 60:
            return jsonify({'error': 'BMI must be between 10 and 60'}), 400
        
        if children < 0:
            return jsonify({'error': 'Children cannot be negative'}), 400
            
        if sex not in ['male', 'female']:
            return jsonify({'error': 'Sex must be "male" or "female"'}), 400
            
        if smoker not in ['yes', 'no']:
            return jsonify({'error': 'Smoker must be "yes" or "no"'}), 400
            
        if region not in ['northeast', 'northwest', 'southeast', 'southwest']:
            return jsonify({'error': 'Invalid region'}), 400
        
        # Make prediction
        prediction = predict_insurance_cost(
            age=age,
            sex=sex,
            bmi=bmi,
            children=children,
            smoker=smoker,
            region=region,
            model_name=model_name
        )
        
        # Return prediction
        return jsonify({
            'prediction': round(float(prediction), 2),
            'model_used': model_name
        })
        
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/')
def index():
    """
    Serve the frontend HTML
    """
    return app.send_static_file('index.html')

# Create a static folder if it doesn't exist
static_folder = Path(__file__).parent / 'static'
static_folder.mkdir(exist_ok=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)