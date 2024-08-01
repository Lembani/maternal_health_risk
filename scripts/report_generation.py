import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

def generate_pdf_report(df):
    with PdfPages('results/reports/maternal_health_risk_report.pdf') as pdf:
        # Title Page
        plt.figure(figsize=(11, 8.5))
        plt.text(0.5, 0.5, 'Maternal Health Risk Data Analysis Report - Zambia', 
                 horizontalalignment='center', verticalalignment='center', 
                 fontsize=20, fontweight='bold')
        plt.axis('off')
        pdf.savefig()
        plt.close()

        # Risk Level Distribution by Age Group
        age_bins = [15, 25, 35, 45, 55]
        age_labels = ['15-24', '25-34', '35-44', '45-54']
        df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='AgeGroup', hue='RiskLevel')
        plt.title('Risk Level Distribution by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Count')
        pdf.savefig()
        plt.close()

        # Correlation Heatmap
        numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')
        pdf.savefig()
        plt.close()

        # Summary
        age_group_counts = df['AgeGroup'].value_counts().to_dict()
        risk_level_counts = df['RiskLevel'].value_counts().to_dict()
        correlation_matrix = numeric_df.corr()

        highest_corr = correlation_matrix.unstack().sort_values(ascending=False).drop_duplicates()
        highest_corr = highest_corr[highest_corr < 1].idxmax()

        summary_text = (
            "The analysis revealed several key insights:\n\n"
            "1. **Risk Level Distribution by Age Group:**\n"
            f"   - The majority of 'high risk' cases are concentrated in the age group '{max(age_group_counts, key=age_group_counts.get)}'.\n\n"
            "2. **Most Common Risk Level**:\n"
            f"   - The most common risk level across the dataset is '{max(risk_level_counts, key=risk_level_counts.get)}'.\n\n"
            "3. **Correlation Insights**:\n"
            f"   - The correlation heatmap indicates that the strongest correlation is between '{highest_corr[0]}' and '{highest_corr[1]}'.\n"
            f"     The correlation coefficient is {correlation_matrix.loc[highest_corr[0], highest_corr[1]]:.2f}.\n"
        )

        plt.figure(figsize=(11, 8.5))
        plt.text(0.1, 0.9, summary_text, fontsize=12, ha='left', va='top', wrap=True)
        plt.axis('off')
        pdf.savefig()
        plt.close()

        print("PDF report generated at 'results/reports/maternal_health_risk_report.pdf'")
