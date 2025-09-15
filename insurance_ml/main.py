"""
Main script to run the entire insurance cost prediction pipeline
"""

import os
import sys
from pathlib import Path

def run_pipeline():
    """
    Run the entire insurance cost prediction pipeline:
    1. Exploratory Data Analysis
    2. Data Preprocessing
    3. Model Training and Evaluation
    4. Prediction Example
    """
    # Make sure we're in the correct directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    try:
        # 1. Run Exploratory Data Analysis
        print("\n" + "="*80)
        print("Step 1: Running Exploratory Data Analysis...")
        print("="*80)
        os.system(f"{sys.executable} exploratory_data_analysis.py")
        
        # 2. Run Data Preprocessing
        print("\n" + "="*80)
        print("Step 2: Running Data Preprocessing...")
        print("="*80)
        os.system(f"{sys.executable} preprocessing.py")
        
        # 3. Run Model Training and Evaluation
        print("\n" + "="*80)
        print("Step 3: Running Model Training and Evaluation...")
        print("="*80)
        os.system(f"{sys.executable} model_training.py")
        
        # 4. Run Prediction Example
        print("\n" + "="*80)
        print("Step 4: Running Prediction Example...")
        print("="*80)
        os.system(f"{sys.executable} prediction.py")
        
        print("\n" + "="*80)
        print("Pipeline completed successfully!")
        print("="*80)
        print("\nYou can now use the trained models to predict insurance costs for new individuals.")
        print("Check the generated CSV files and plots in the insurance_ml directory for results.")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()