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

