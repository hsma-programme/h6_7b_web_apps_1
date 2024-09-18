import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Titanic Dataset Explorer')

# Import data
try:
    data = pd.read_csv("data/raw_data.csv")

except FileNotFoundError:
    address = 'https://raw.githubusercontent.com/MichaelAllen1966/' + \
                '1804_python_healthcare/master/titanic/data/train.csv'
    data = pd.read_csv(address)

# Display data
st.dataframe(data)
