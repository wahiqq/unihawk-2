"""
Data preprocessing for Insurance Cost Prediction
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path

def load_data():
    """Load the insurance dataset"""
    data_path = Path('../insurance.csv')
    df = pd.read_csv(data_path)
    return df

def preprocess_data(df, test_size=0.2, random_state=42):
    """
    Preprocess the insurance dataset:
    - Handle categorical variables
    - Scale numerical features
    - Split data into train and test sets
    """
    # Separate features and target
    X = df.drop('charges', axis=1)
    y = df['charges']
    
    # Identify categorical and numerical columns
    categorical_cols = ['sex', 'smoker', 'region']
    numerical_cols = ['age', 'bmi', 'children']
    
    # Create preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(drop='first'), categorical_cols)
        ])
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Fit the preprocessor on the training data
    preprocessor.fit(X_train)
    
    # Transform the training and test data
    X_train_processed = preprocessor.transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    
    # Save the preprocessor
    joblib.dump(preprocessor, 'insurance_ml/preprocessor.pkl')
    
    # Get feature names after one-hot encoding
    ohe = preprocessor.named_transformers_['cat']
    ohe_feature_names = ohe.get_feature_names_out(categorical_cols)
    feature_names = numerical_cols + list(ohe_feature_names)
    
    print(f"Preprocessed data shapes:")
    print(f"X_train: {X_train_processed.shape}")
    print(f"X_test: {X_test_processed.shape}")
    print(f"y_train: {y_train.shape}")
    print(f"y_test: {y_test.shape}")
    print(f"\nFeatures after preprocessing: {feature_names}")
    
    return X_train_processed, X_test_processed, y_train, y_test, feature_names

if __name__ == "__main__":
    df = load_data()
    X_train, X_test, y_train, y_test, feature_names = preprocess_data(df)
    print("Preprocessing complete! Preprocessor saved as 'insurance_ml/preprocessor.pkl'.")