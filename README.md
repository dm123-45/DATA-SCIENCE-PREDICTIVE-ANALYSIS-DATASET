# DataLab — Analytics Studio

**An interactive data analytics portfolio project built with Python, Streamlit, Pandas and Plotly.** Originally developed from the ILOOP data science and exploratory data analysis work.

### [🚀 Launch the live dashboard](https://dave-data-analytics.streamlit.app/)

[![Live app](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://dave-data-analytics.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://github.com/dm123-45/DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET/actions/workflows/ci.yml/badge.svg)](https://github.com/dm123-45/DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET/actions/workflows/ci.yml)

## Project overview

DataLab helps users upload and explore CSV data without writing code. It surfaces dataset dimensions, missing values, column types and interactive visualisations, and allows users to export filtered results.

**Live application:** https://dave-data-analytics.streamlit.app/

## Features

| Feature | What it does |
| --- | --- |
| CSV upload | Read user-supplied CSV files up to 20 MB |
| Demo dataset | Explore the built-in Iris sample without uploading a file |
| Dataset metrics | Display row counts, columns, numeric features and missing cells |
| Data quality | Inspect data types, missing counts and unique values |
| Filtering | Select a column and filter to selected values |
| Visualisation | Interactive histograms, box plots, scatter plots and correlation heatmaps |
| Export | Download the filtered dataset as CSV |

## How to explore the app

1. Open the [live dashboard](https://dave-data-analytics.streamlit.app/).
2. Start with the Iris sample data. Confirm that dataset metrics and preview appear.
3. Open **Data quality and column types** to review missing values and data types.
4. Use **Filter column** and choose one or more values.
5. Switch between **Histogram**, **Box plot**, **Scatter plot** and **Correlation heatmap**.
6. Download the filtered CSV and inspect it.
7. Upload your own CSV and repeat the workflow.

## Run locally

Requires Python 3.11.

```bash
git clone https://github.com/dm123-45/DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET.git
cd DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET
python -m venv .venv
# Activate your virtual environment, then:
pip install -r requirements.txt
streamlit run app.py
```

## Automated checks

```bash
pip install pytest
python -m pytest -q tests/
```

The repository includes a GitHub Actions workflow for Python syntax checks and data helper tests. The automated tests do **not** replace full browser-based testing.

## Deployment

Streamlit Community Cloud configuration:

- Repository: `dm123-45/DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET`
- Branch: `main`
- Main file: `app.py`
- Python: `3.11`

## Technologies and skills demonstrated

**Python**, **Pandas**, **Plotly**, **Streamlit**, data cleaning fundamentals, exploratory data analysis, data quality inspection, interactive visualisation, CSV processing and GitHub-based deployment.

## Privacy and limitations

Avoid uploading confidential or sensitive data to public deployments. Data is processed on the app's hosting infrastructure. Charts are exploratory and do not establish causality. CSV parsing, filtering and charting may have limitations on unusual or large datasets.

## Portfolio status

The user has confirmed the public app opens successfully. Individual feature tests and CI results should be verified independently; no claim of complete end-to-end test coverage is made.
