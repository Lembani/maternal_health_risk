import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

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
    
    # Create the results/visualizations directory if it doesn't exist
    os.makedirs('results/visualizations', exist_ok=True)
    
    plt.savefig('results/visualizations/risk_level_distribution_by_age_group.png')
    plt.close()

    # Filter out non-numeric columns for correlation heatmap
    numeric_df = df.select_dtypes(include=[float, int])

    # Correlation Heatmap
    plt.figure(figsize=(12, 10))
    heatmap = sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap='coolwarm',
        linewidths=0.5,
        annot_kws={"size": 10},
        vmin=-1,
        vmax=1,
        cbar_kws={"shrink": 0.8, "ticks": [-1, -0.5, 0, 0.5, 1]}
    )
    
    heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=16)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    plt.savefig('results/visualizations/correlation_heatmap.png')
    plt.close()
