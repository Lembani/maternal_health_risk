from scripts.data_loading import load_data
from scripts.exploratory_analysis import perform_exploratory_analysis
from scripts.report_generation import generate_pdf_report

def main():
    df = load_data('data/maternal_health_risk_data.csv')
    perform_exploratory_analysis(df)
    generate_pdf_report(df)

if __name__ == "__main__":
    main()