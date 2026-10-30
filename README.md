# DataLab — Analytics Studio

An interactive data exploration dashboard built with **Streamlit, Pandas and Plotly**, developed from the ILOOP data analytics project.

## Features
- Upload CSV datasets (up to 20 MB) or explore the built-in Iris sample
- Dataset overview and missing-value indicators
- Column-level filtering, data preview and CSV export
- Interactive histogram, box plot, scatter plot and correlation heatmap
- Responsive analytics layout

## Run locally
```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud
1. Visit https://share.streamlit.io/ and sign in with GitHub.
2. Choose this repository and the `main` branch.
3. Set the entry point to `app.py` and deploy.
4. Add the resulting live URL to the repository's About section.

## Privacy and limitations
Do not upload sensitive or confidential data to public deployments. Uploaded datasets are processed in the hosting environment. Visualisations are exploratory and should be interpreted in context.

## Technology
Python · Streamlit · Pandas · Plotly

## Status
Source updated. Hosted deployment and full browser testing are not yet verified.
