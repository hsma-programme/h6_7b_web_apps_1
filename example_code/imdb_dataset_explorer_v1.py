import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title('IMDB Dataset Explorer')

# Import data
try:
    data = pd.read_csv("data/imdb_top_1000.csv")
except FileNotFoundError:
    data = pd.read_csv("https://github.com/hsma-programme/h6_7b_web_apps_1/raw/main/data/imdb_top_1000.csv")

# Display data
st.dataframe(data)

st.plotly_chart(
    px.histogram(data, x="Released_Year")
)
