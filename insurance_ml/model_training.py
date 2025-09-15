"""
Model training for Insurance Cost Prediction
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from pathlib import Path

# Import preprocessing to get preprocessed data
from preprocessing import load_data, preprocess_data

def train_models(X_train, y_train):
    """
    Train multiple regression models on the insurance dataset
    """
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(alpha=1.0),
        'Lasso Regression': Lasso(alpha=0.1),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    # Train each model
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        
        # Save the trained model
        joblib.dump(model, f'{name.lower().replace(" ", "_")}.pkl')
        print(f"{name} trained and saved successfully.")
    
    return models

def evaluate_models(models, X_test, y_test):
    """
    Evaluate trained models on test data
    """
    results = []
    
    for name, model in models.items():
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Store results
        results.append({
            'Model': name,
            'MSE': mse,
            'RMSE': rmse,
            'MAE': mae,
            'R²': r2
        })
    
    # Convert to DataFrame for better display
    results_df = pd.DataFrame(results)
    print("\nModel Evaluation Results:")
    print(results_df)
    
    # Save results to CSV
    results_df.to_csv('model_evaluation_results.csv', index=False)
    
    # Find best model based on RMSE
    best_model_idx = results_df['RMSE'].idxmin()
    best_model = results_df.loc[best_model_idx, 'Model']
    print(f"\nBest performing model: {best_model}")
    
    return results_df

if __name__ == "__main__":
    # Load and preprocess data
    df = load_data()
    X_train, X_test, y_train, y_test, feature_names = preprocess_data(df)
    
    # Train models
    models = train_models(X_train, y_train)
    
    # Evaluate models
    results = evaluate_models(models, X_test, y_test)
    print("\nModel training and evaluation complete!")