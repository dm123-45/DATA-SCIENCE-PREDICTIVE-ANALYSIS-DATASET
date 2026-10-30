<div align="center">

# 📊 DataLab — Analytics Studio

### Turn raw CSV datasets into clear, interactive insights.

**A Python-powered exploratory data analysis dashboard built with Streamlit, Pandas and Plotly.**

[![Open Live Dashboard](https://img.shields.io/badge/🚀_Launch-Live_Dashboard-FF4B4B?style=for-the-badge)](https://dave-data-analytics.streamlit.app/)
[![View Source](https://img.shields.io/badge/GitHub-Source_Code-181717?style=for-the-badge&logo=github)](https://github.com/dm123-45/DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualisation-3F4F75?logo=plotly&logoColor=white)

</div>

---

## 📌 Project overview

**DataLab — Analytics Studio** is a web application designed to make **exploratory data analysis (EDA)** accessible to people who want to understand a dataset without writing Python code.

Users can upload CSV files, inspect data quality, filter records, explore distributions and relationships through interactive charts, and download filtered results.

The project evolved from **ILOOP data science and analytics work** and demonstrates practical skills in Python application development, data handling, visualisation and cloud deployment.

> **Try the live app:** https://dave-data-analytics.streamlit.app/

## 🎯 The problem

Raw datasets are often difficult to interpret. Before meaningful analysis, users need to answer basic questions: How many records are there? Are values missing? Which columns are numeric? Are there patterns, unusual values or relationships worth investigating?

DataLab brings these first steps together in one interactive interface.

## ✨ Key features

| Feature | Description |
| --- | --- |
| 📂 **CSV upload** | Upload a CSV file of up to 20 MB |
| 🌸 **Sample dataset** | Explore the built-in Iris dataset immediately |
| 📈 **Dataset overview** | See row counts, column counts, numeric features and missing-cell totals |
| 🔍 **Data quality inspection** | Review column data types, missing values and unique-value counts |
| 🎛️ **Interactive filters** | Select a column and filter by chosen values |
| 📊 **Histograms** | Explore numeric distributions |
| 📦 **Box plots** | Inspect spread and potential outliers |
| 🔵 **Scatter plots** | Explore relationships between numeric features |
| 🌡️ **Correlation heatmaps** | Compare correlations between numeric columns |
| ⬇️ **CSV export** | Download filtered records for further analysis |

## 🖥️ How to use DataLab

1. **Open the dashboard:** [dave-data-analytics.streamlit.app](https://dave-data-analytics.streamlit.app/).
2. **Choose a dataset:** Explore the Iris sample or upload your own CSV.
3. **Review the overview:** Check dimensions, missing values and numeric features.
4. **Inspect data quality:** Expand the column summary.
5. **Filter the records:** Choose a column and select values of interest.
6. **Visualise:** Switch between histograms, box plots, scatter plots and correlation heatmaps.
7. **Export:** Download the filtered CSV.

### Example use case

A retail analyst could upload a sales dataset and explore price distributions, differences between product categories, missing records, and correlations between numeric measures. Available analyses depend on the dataset's columns and data quality.

## 🧰 Technology stack

| Technology | Role |
| --- | --- |
| **Python** | Core application logic |
| **Streamlit** | Interactive web interface |
| **Pandas** | Data loading, inspection and filtering |
| **Plotly Express** | Interactive charts |
| **GitHub** | Version control and source hosting |
| **Streamlit Community Cloud** | Public application deployment |
| **Pytest / GitHub Actions** | Data utility tests and automated checks |

## 🏗️ Repository structure

```text
.
├── app.py                  # Streamlit interface and charts
├── data_utils.py           # CSV validation and filtering helpers
├── requirements.txt        # Python dependencies
├── .python-version         # Python runtime version
├── .streamlit/
│   └── config.toml         # Streamlit theme
├── .github/
│   └── workflows/
│       └── ci.yml          # Automated checks
├── tests/
│   └── test_data_utils.py  # Data helper unit tests
└── README.md               # Project documentation
```

## ⚙️ Run locally

**Prerequisite:** Python 3.11.

```bash
git clone https://github.com/dm123-45/DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET.git
cd DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install and launch:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit will display a local URL in your terminal.

## 🧪 Testing

Run the included data helper tests:

```bash
python -m pip install pytest
python -m pytest -q tests/
```

GitHub Actions also checks Python syntax and runs these tests on pushes and pull requests. **Unit tests do not guarantee that every browser interaction works**; manual UI testing is recommended.

## ☁️ Deployment

The project is configured for Streamlit Community Cloud:

- **Repository:** `dm123-45/DATA-SCIENCE-PREDICTIVE-ANALYSIS-DATASET`
- **Branch:** `main`
- **Entry point:** `app.py`
- **Python:** `3.11`
- **Live URL:** https://dave-data-analytics.streamlit.app/

## 💡 Skills demonstrated

- Exploratory data analysis and data quality assessment
- Python programming and modular code organisation
- Interactive data visualisation and dashboard development
- CSV processing, filtering and data export
- Automated testing and GitHub workflows
- Cloud deployment and technical documentation

## 🚧 Scope and limitations

DataLab currently focuses on **exploratory analysis**, not predictive modelling or machine-learning training. Charts help reveal patterns but do not establish causation. The dashboard may have limitations with large, unusually formatted or complex datasets. Avoid uploading sensitive or confidential information to public deployments.

**Potential future enhancements:** predictive modelling, model evaluation, time-series analysis, PDF report generation and richer dataset profiling. These are ideas, **not current features**.

## 👨‍💻 Developer

**Dave Tatenda Makamure**  
Information Technology graduate | Data Analytics & Software Development

[GitHub Profile](https://github.com/dm123-45) · [LinkedIn](https://www.linkedin.com/in/dave-tatenda-makamure-6b942632b/)

---

<div align="center">

**Built to make data exploration simpler, faster and more accessible.**

[**🚀 Explore DataLab**](https://dave-data-analytics.streamlit.app/)

</div>
