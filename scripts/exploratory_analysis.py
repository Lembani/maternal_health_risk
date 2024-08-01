import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loading import load_data

def perform_exploratory_analysis(df):
    # Explore the Distribution of Risk Level by Age Group
    age_bins = [15, 25, 35, 45, 55]
    age_labels = ['15-24', '25-34', '35-44', '45-54']
    df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='AgeGroup', hue='RiskLevel')
    plt.title('Risk Level Distribution by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.savefig('results/visualizations/risk_level_distribution_by_age_group.png')
    plt.close()

    # Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.savefig('results/visualizations/correlation_heatmap.png')
    plt.close()
