import matplotlib.pyplot as plt
import seaborn as sns
from data_loading import load_data

def generate_visualizations(df):
    # Box Plot of Blood Pressure by Risk Level
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='RiskLevel', y='SystolicBP')
    plt.title('Systolic Blood Pressure by Risk Level')
    plt.xlabel('Risk Level')
    plt.ylabel('Systolic Blood Pressure (mmHg)')
    plt.savefig('results/visualizations/systolic_bp_by_risk_level.png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='RiskLevel', y='DiastolicBP')
    plt.title('Diastolic Blood Pressure by Risk Level')
    plt.xlabel('Risk Level')
    plt.ylabel('Diastolic Blood Pressure (mmHg)')
    plt.savefig('results/visualizations/diastolic_bp_by_risk_level.png')
    plt.close()

    # Violin Plot of Blood Glucose Levels by Risk Level
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=df, x='RiskLevel', y='BS')
    plt.title('Blood Glucose Levels by Risk Level')
    plt.xlabel('Risk Level')
    plt.ylabel('Blood Glucose Levels (mmol/L)')
    plt.savefig('results/visualizations/blood_glucose_by_risk_level.png')
    plt.close()
