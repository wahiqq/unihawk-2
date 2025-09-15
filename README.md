# 💰 Insurance Cost Predictor

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/scikit--learn-1.3+-orange.svg" alt="Scikit-learn Version">
  <img src="https://img.shields.io/badge/Flask-API-green.svg" alt="Flask API">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</div>

> A comprehensive machine learning solution for predicting health insurance costs based on personal attributes, complete with data exploration, model training, and an intuitive web interface.

## 📊 Project Overview

This project uses machine learning to predict health insurance costs based on individual characteristics. It implements a complete end-to-end solution, from exploratory data analysis to model training to a user-friendly web interface for making predictions.

## ✨ Features

- **Comprehensive Data Analysis**: Visualizations and statistical analysis of the insurance dataset
- **Multiple ML Models**: Implementation of 5 regression models with performance comparison
- **Interactive Web UI**: User-friendly interface for entering data and getting predictions
- **RESTful API**: Backend API for serving predictions to applications
- **Detailed Results**: Analysis of factors affecting insurance costs

## 📂 Project Structure

```
insurance_ml/
├── exploratory_data_analysis.py # EDA and data visualization
├── preprocessing.py             # Data preprocessing pipeline
├── model_training.py            # ML model training and evaluation
├── prediction.py                # Prediction functions
├── main.py                      # Pipeline orchestration
├── api.py                       # Flask API server
├── start_api_server.bat         # Windows batch file to start server
├── static/                      # Frontend files
│   ├── index.html               # Web UI HTML
│   ├── styles.css               # CSS styling
│   └── script.js                # JavaScript functionality
└── README.md                    # This documentation
```

## 📊 Dataset

The dataset (`insurance.csv` in the parent directory) contains information about insurance policyholders:

| Feature    | Description                                      | Type        |
|------------|--------------------------------------------------|-------------|
| `age`      | Age of the insured person                        | Numeric     |
| `sex`      | Gender of the insured (male, female)             | Categorical |
| `bmi`      | Body Mass Index                                  | Numeric     |
| `children` | Number of dependents covered                     | Integer     |
| `smoker`   | Smoking status (yes, no)                         | Categorical |
| `region`   | Residential area (NE, NW, SE, SW)                | Categorical |
| `charges`  | Annual health insurance cost (target variable)   | Numeric     |

## 🧠 Machine Learning Models

The project implements and compares the following regression models:

1. **Linear Regression**: Basic linear model
2. **Ridge Regression**: Linear regression with L2 regularization
3. **Lasso Regression**: Linear regression with L1 regularization
4. **Random Forest**: Ensemble of decision trees
5. **Gradient Boosting**: Sequential ensemble technique (best performer)

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or later
- Required Python packages (can be installed using `pip`):
  ```
  pandas numpy scikit-learn matplotlib seaborn joblib flask flask-cors
  ```

### Setup and Installation

1. **Clone the repository or download the files** to your local machine

2. **Set up a Python virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   pip install pandas numpy scikit-learn matplotlib seaborn joblib flask flask-cors
   ```

3. **Train the models** by running:
   ```bash
   cd path\to\insurance_ml
   python main.py
   ```
   This will:
   - Perform exploratory data analysis
   - Generate visualization plots
   - Preprocess the data
   - Train and evaluate multiple regression models
   - Save the models for future use

4. **Start the API server** using one of these methods:
   - Double-click on `start_api_server.bat` in Windows Explorer
   - Run in PowerShell or Command Prompt:
     ```bash
     cd path\to\insurance_ml
     python api.py
     ```
   - If using a custom Python environment:
     ```bash
     cd path\to\insurance_ml
     path\to\python\executable api.py
     ```

5. **Access the web interface** by opening a browser and navigating to:
   ```
   http://localhost:5000
   ```

## 🖥️ Using the Web Interface

The web interface allows you to:

1. **Input Personal Information**:
   - Age (between 18-64)
   - Sex (male or female)
   - BMI (Body Mass Index)
   - Number of children/dependents
   - Smoking status
   - Region of residence

2. **Choose a Prediction Model**:
   - Gradient Boosting (recommended based on performance)
   - Random Forest
   - Linear Regression
   - Ridge Regression
   - Lasso Regression

3. **Get Prediction Results**:
   - Estimated annual insurance cost
   - Analysis of key factors affecting the cost
   - Model information

## 🔌 API Documentation

The Flask API provides endpoints for making predictions programmatically:

### List Available Models

**Request:**
```
GET /api/models
```

**Response:**
```json
{
  "models": [
    "gradient_boosting",
    "random_forest",
    "linear_regression",
    "ridge_regression",
    "lasso_regression"
  ]
}
```

### Make a Prediction

**Request:**
```
POST /api/predict
Content-Type: application/json

{
  "age": 30,
  "sex": "male",
  "bmi": 25.0,
  "children": 1,
  "smoker": "no",
  "region": "northeast",
  "model_name": "gradient_boosting"  // Optional
}
```

**Response:**
```json
{
  "prediction": 6270.77,
  "model_used": "gradient_boosting"
}
```

## 🐍 Programmatic Usage

You can also use the trained models programmatically:

```python
from insurance_ml.prediction import predict_insurance_cost

# Make a prediction
estimated_cost = predict_insurance_cost(
    age=30,
    sex="male",
    bmi=25.0,
    children=1,
    smoker="no",
    region="northeast",
    model_name="gradient_boosting"  # or another trained model
)

print(f"Estimated annual insurance cost: ${estimated_cost:.2f}")
```

## 📈 Model Performance

The models are evaluated using the following metrics:

| Model             | MSE         | RMSE        | MAE         | R²       |
|-------------------|-------------|-------------|-------------|----------|
| Gradient Boosting | 1.87e+07    | 4329.57     | 2443.48     | 0.879    |
| Random Forest     | 2.09e+07    | 4567.78     | 2543.98     | 0.866    |
| Linear Regression | 3.36e+07    | 5796.28     | 4181.19     | 0.784    |
| Ridge Regression  | 3.36e+07    | 5800.46     | 4193.20     | 0.783    |
| Lasso Regression  | 3.36e+07    | 5796.36     | 4181.30     | 0.784    |

The Gradient Boosting model performs best with the highest R² and lowest error metrics.

## 🔍 Key Insights

Analysis of the dataset revealed several key insights:

- **Smoking is the most significant factor** affecting insurance costs
- **Age has a strong positive correlation** with insurance charges
- **BMI above 30** (obesity) leads to higher insurance costs
- **Regional variations exist** in average insurance costs
- **The number of dependents** has a modest impact on insurance charges

## 🛠️ Troubleshooting

### Web Interface Not Loading
- Ensure the API server is running (check terminal for errors)
- Verify you're accessing the correct URL (http://localhost:5000)
- Check browser console for JavaScript errors

### Prediction Errors
- Make sure all model files were generated correctly
- Verify all input fields have valid values
- Check terminal logs for API errors

## 🔮 Future Enhancements

- Feature engineering to improve model performance
- Hyperparameter tuning for better accuracy
- Advanced visualizations of feature importance
- User accounts for saving prediction history
- Deployment to cloud platforms for public access

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <p>Built with ❤️ using Python, Scikit-learn, and Flask</p>
  <p>© 2025 Insurance Cost Predictor</p>
</div>