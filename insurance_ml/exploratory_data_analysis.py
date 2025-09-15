"""
Exploratory Data Analysis for Insurance Cost Prediction
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set display options for pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)

# Load the dataset
def load_data():
    data_path = Path('../insurance.csv')
    df = pd.read_csv(data_path)
    return df

def explore_data(df):
    """
    Perform exploratory data analysis on the insurance dataset
    """
    print("Dataset Information:")
    print(f"Shape: {df.shape}")
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nSummary Statistics:")
    print(df.describe())
    
    print("\nChecking for missing values:")
    print(df.isnull().sum())
    
    # Distribution of insurance charges
    plt.figure(figsize=(10, 6))
    plt.hist(df['charges'], bins=30, edgecolor='black')
    plt.title('Distribution of Insurance Charges')
    plt.xlabel('Charges')
    plt.ylabel('Frequency')
    plt.savefig('charges_distribution.png')
    
    # Correlation between numerical features
    plt.figure(figsize=(10, 8))
    numerical_df = df.select_dtypes(include=['float64', 'int64'])
    correlation = numerical_df.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png')
    
    # Relationship between age and charges
    plt.figure(figsize=(10, 6))
    plt.scatter(df['age'], df['charges'])
    plt.title('Age vs Charges')
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.savefig('age_vs_charges.png')
    
    # Relationship between BMI and charges
    plt.figure(figsize=(10, 6))
    plt.scatter(df['bmi'], df['charges'])
    plt.title('BMI vs Charges')
    plt.xlabel('BMI')
    plt.ylabel('Charges')
    plt.savefig('bmi_vs_charges.png')
    
    # Charges by smoker status
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='smoker', y='charges', data=df)
    plt.title('Charges by Smoker Status')
    plt.savefig('charges_by_smoker.png')
    
    # Charges by region
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='region', y='charges', data=df)
    plt.title('Charges by Region')
    plt.savefig('charges_by_region.png')
    
    # Charges by sex
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='sex', y='charges', data=df)
    plt.title('Charges by Sex')
    plt.savefig('charges_by_sex.png')
    
    # Charges by number of children
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='children', y='charges', data=df)
    plt.title('Charges by Number of Children')
    plt.savefig('charges_by_children.png')
    
    print("\nAnalysis complete! Visualizations saved in the current directory.")

if __name__ == "__main__":
    df = load_data()
    explore_data(df)