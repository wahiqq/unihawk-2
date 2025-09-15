# Insurance Cost Prediction Project

This project uses machine learning to predict insurance costs based on individual characteristics.

## Dataset

The dataset (`insurance.csv`) contains the following features:

- `age`: Age of the insured person
- `sex`: Gender of the insured person (male, female)
- `bmi`: Body Mass Index of the insured person
- `children`: Number of children/dependents covered
- `smoker`: Smoking status (yes, no)
- `region`: Residential area (northeast, northwest, southeast, southwest)
- `charges`: Insurance cost (target variable)

## Project Structure

```
insurance_ml/
├── exploratory_data_analysis.py - Performs EDA and generates visualizations
├── preprocessing.py - Preprocesses data for model training
├── model_training.py - Trains and evaluates various regression models
├── prediction.py - Contains function for making predictions with trained models
├── main.py - Runs the entire pipeline
├── api.py - Flask API to serve the prediction model
├── static/ - Frontend files (HTML, CSS, JavaScript)
├── README.md - This file
```

## Models Implemented

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Random Forest
5. Gradient Boosting

## How to Run

1. Make sure you have Python installed with required packages:
   - pandas
   - numpy
   - scikit-learn
   - matplotlib
   - seaborn
   - joblib
   - flask
   - flask-cors

2. Run the main script to train the models:
   ```
   python insurance_ml/main.py
   ```

3. Start the API and web interface:
   ```
   python insurance_ml/api.py
   ```
   Or simply run the `start_api_server.bat` file.

4. Open a web browser and navigate to:
   ```
   http://localhost:5000
   ```

5. To make predictions programmatically with a trained model:
   ```python
   from insurance_ml.prediction import predict_insurance_cost
   
   cost = predict_insurance_cost(
       age=30,
       sex='male',
       bmi=25.0,
       children=1,
       smoker='no',
       region='northeast',
       model_name='gradient_boosting'  # or another trained model
   )
   print(f"Predicted insurance cost: ${cost:.2f}")
   ```

## Results

After running the pipeline, you'll find:
- Visualization plots in the `insurance_ml` directory
- Model evaluation results in `model_evaluation_results.csv`
- Trained models saved as pickle files for future use

## Web Interface

The project includes a user-friendly web interface that allows users to:

- Enter their personal information (age, sex, BMI, etc.)
- Select a prediction model
- Get an estimated insurance cost
- View factors that affect their insurance cost

## API Endpoints

The Flask API provides the following endpoints:

- `GET /api/models` - List all available trained models
- `POST /api/predict` - Make a prediction based on input data
  - Required JSON payload: `age`, `sex`, `bmi`, `children`, `smoker`, `region`
  - Optional parameter: `model_name` (defaults to 'gradient_boosting')

## Next Steps

- Feature engineering to improve model performance
- Hyperparameter tuning for better accuracy
- Add visualization of feature importance in the frontend
- Implement user accounts for saving predictions