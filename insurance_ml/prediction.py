"""
Prediction function for Insurance Cost Prediction
"""

import pandas as pd
import numpy as np
import joblib
from pathlib import Path

def load_model(model_name='gradient_boosting'):
    """
    Load a trained model
    
    Parameters:
    model_name (str): Name of the model to load (default: 'gradient_boosting')
                      Options: 'linear_regression', 'ridge_regression', 'lasso_regression', 
                               'random_forest', 'gradient_boosting'
    
    Returns:
    Trained model object
    """
    model_path = Path(f'insurance_ml/{model_name}.pkl')
    if not model_path.exists():
        raise FileNotFoundError(f"Model file {model_path} not found!")
    
    model = joblib.load(model_path)
    return model

def load_preprocessor():
    """
    Load the trained preprocessor
    
    Returns:
    Trained preprocessor object
    """
    preprocessor_path = Path('insurance_ml/preprocessor.pkl')
    if not preprocessor_path.exists():
        raise FileNotFoundError(f"Preprocessor file {preprocessor_path} not found!")
    
    preprocessor = joblib.load(preprocessor_path)
    return preprocessor

def predict_insurance_cost(age, sex, bmi, children, smoker, region, model_name='gradient_boosting'):
    """
    Predict insurance cost for a new individual
    
    Parameters:
    age (int): Age of the individual
    sex (str): 'male' or 'female'
    bmi (float): Body Mass Index
    children (int): Number of children/dependents
    smoker (str): 'yes' or 'no'
    region (str): 'northeast', 'northwest', 'southeast', or 'southwest'
    model_name (str): Name of the model to use for prediction
    
    Returns:
    float: Predicted insurance cost
    """
    # Create a dataframe with the input data
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })
    
    # Load preprocessor and model
    preprocessor = load_preprocessor()
    model = load_model(model_name)
    
    # Preprocess the input data
    X = preprocessor.transform(data)
    
    # Make prediction
    prediction = model.predict(X)[0]
    
    return prediction

def main():
    """
    Example usage of the prediction function
    """
    # Sample input
    age = 30
    sex = 'male'
    bmi = 25.0
    children = 1
    smoker = 'no'
    region = 'northeast'
    
    # Try with different models
    models = ['linear_regression', 'ridge_regression', 'lasso_regression', 
              'random_forest', 'gradient_boosting']
    
    print("Insurance Cost Predictions for:")
    print(f"Age: {age}, Sex: {sex}, BMI: {bmi}, Children: {children}, " 
          f"Smoker: {smoker}, Region: {region}\n")
    
    for model in models:
        try:
            prediction = predict_insurance_cost(age, sex, bmi, children, smoker, region, model)
            print(f"{model.replace('_', ' ').title()}: ${prediction:.2f}")
        except FileNotFoundError as e:
            print(f"Could not use {model}: {str(e)}")

if __name__ == "__main__":
    main()