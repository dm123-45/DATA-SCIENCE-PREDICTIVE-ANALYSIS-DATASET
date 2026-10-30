"""Interactive exploratory data analysis dashboard for CSV datasets."""
import pandas as pd
import plotly.express as px
import streamlit as st
from data_utils import read_csv_bytes, filter_frame, numeric_columns

st.set_page_config(page_title="DataLab | Analytics Studio", page_icon="📊", layout="wide")
st.markdown("""<style>
.block-container{padding-top:2rem;max-width:1400px}
[data-testid="stMetric"]{border:1px solid #dbe4ee;border-radius:14px;padding:14px;background:rgba(128,128,128,.04)}
h1,h2,h3{letter-spacing:-.025em}
</style>""", unsafe_allow_html=True)
st.title("📊 DataLab")
st.caption("Analytics Studio · Explore, visualise and export your datasets")
with st.sidebar:
    st.header("Workspace")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    sample = st.checkbox("Use Iris sample data", value=True)
    st.divider()
    st.caption("Data is processed during this session. Avoid uploading sensitive information.")

@st.cache_data(show_spinner=False)
def load_csv(data: bytes) -> pd.DataFrame:
    return read_csv_bytes(data)

if uploaded is not None:
    if uploaded.size > 20 * 1024 * 1024:
        st.error("File exceeds the 20 MB limit.")
        st.stop()
    try:
        df = load_csv(uploaded.getvalue())
    except (ValueError, UnicodeError, pd.errors.ParserError, pd.errors.EmptyDataError) as exc:
        st.error(f"Unable to read CSV: {exc}")
        st.stop()
    source = uploaded.name
elif sample:
    df = px.data.iris()
    source = "Iris sample"
else:
    st.info("Upload a CSV or enable the sample dataset to begin.")
    st.stop()

if not len(df.columns):
    st.warning("No columns detected.")
    st.stop()
df.columns = [str(c) for c in df.columns]
st.subheader(source)
c1,c2,c3,c4 = st.columns(4)
c1.metric("Rows", f"{len(df):,}")
c2.metric("Columns", len(df.columns))
c3.metric("Missing cells", f"{int(df.isna().sum().sum()):,}")
numeric = numeric_columns(df)
c4.metric("Numeric features", len(numeric))

with st.expander("Data quality and column types", expanded=False):
    quality = pd.DataFrame({"Type": df.dtypes.astype(str), "Missing": df.isna().sum(), "Unique": df.nunique(dropna=True)})
    st.dataframe(quality, use_container_width=True)

st.subheader("Explore your data")
left,right = st.columns([1,2])
with left:
    filter_column = st.selectbox("Filter column", ["All columns"] + df.columns.tolist(), key="filter_column")
    filtered = df.copy()
    if filter_column != "All columns":
        values = sorted(df[filter_column].dropna().astype(str).unique().tolist())[:500]
        chosen = st.multiselect("Values", values)
        if chosen:
            filtered = filter_frame(df, filter_column, chosen)
    st.caption(f"{len(filtered):,} matching rows")
with right:
    st.dataframe(filtered.head(1000), use_container_width=True, hide_index=True)
st.download_button("⬇ Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"),
                   "datalab_export.csv", "text/csv")

st.subheader("Visual analytics")
if filtered.empty:
    st.info("No matching rows. Change your filters or upload another dataset.")
elif not numeric:
    st.info("No numeric columns detected. Data preview and export are still available.")
else:
    chart = st.selectbox("Chart", ["Histogram", "Box plot", "Scatter plot", "Correlation heatmap"])
    if chart == "Histogram":
        x = st.selectbox("Measure", numeric)
        bins = st.slider("Bins", 5, 100, 25)
        fig = px.histogram(filtered, x=x, nbins=bins, color_discrete_sequence=["#6366f1"])
    elif chart == "Box plot":
        x = st.selectbox("Measure", numeric)
        fig = px.box(filtered, y=x, points="outliers", color_discrete_sequence=["#6366f1"])
    elif chart == "Scatter plot":
        if len(numeric) < 2:
            st.info("Scatter plots require two numeric columns.")
            fig = None
        else:
            x = st.selectbox("X axis", numeric)
            y = st.selectbox("Y axis", numeric, index=1)
            color = st.selectbox("Colour group", ["None"] + df.columns.tolist())
            fig = px.scatter(filtered, x=x, y=y, color=None if color=="None" else color)
    else:
        if len(numeric) < 2:
            st.info("Correlation requires two numeric columns.")
            fig = None
        else:
            fig = px.imshow(filtered[numeric].corr(), text_auto=".2f", aspect="auto",
                            color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
    if fig is not None:
        fig.update_layout(template="plotly_white", margin=dict(l=20,r=20,t=30,b=20))
        st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("DataLab · Built with Streamlit, Pandas and Plotly · Exploratory analysis, not automated decision-making")
