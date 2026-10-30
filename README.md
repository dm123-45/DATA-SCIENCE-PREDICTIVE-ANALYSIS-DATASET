# ILOOP — Interactive Data Analysis Dashboard

A Streamlit application for exploratory data analysis of CSV datasets. Built with Python, pandas, NumPy and Plotly.

## Features
- CSV upload and Iris sample dataset
- Summary statistics and missing-value overview
- Histograms, boxplots, scatterplots, correlation heatmaps and scatter matrices
- Column filtering and CSV export

## Local setup
1. Install Python 3.10 or later.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it and install: `pip install -r requirements.txt`
4. Start: `streamlit run app.py`

## Online deployment
Deploy this repository using [Streamlit Community Cloud](https://share.streamlit.io/). Set the main file path to `app.py`. Configure the deployment to use the branch containing the reviewed code.

## Data privacy
Do not upload confidential or personally identifiable datasets to publicly hosted demos. Uploaded files are processed by the application runtime.

## Status
Portfolio improvement branch; functionality and hosting must be tested before describing the deployment as production-ready.
