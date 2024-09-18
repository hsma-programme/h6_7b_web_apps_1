import streamlit as st
import pandas as pd
import plotly.express as px

# Set up a title that will appear at the top of the page
st.title('IMDB Dataset Explorer')

# Import data
# Here, we're pointing towards a URL of a csv dataset hosted on github in a public repository
url = "https://github.com/hsma-programme/h6_7b_web_apps_1/raw/main/data/imdb_top_1000.csv"
# Then we load this in directly with pandas, saving it to a variable called 'data'
data = pd.read_csv(url)

# We use the st.dataframe command to display the dataframe nicely.
# This won't always
st.dataframe(data)

# Finally, we display a very simple chart
# We're going to use a plotly chart, so we start with the st.plotly_chart
# command so that streamlit can correctly display the chart we pass in
st.plotly_chart(
    # Next, we create a simple histogram with the plotly express library
    px.histogram(
        data, # First, we pass in the dataframe we want to display
        x="Released_Year" # Now we pass in the column name of interest in quotation marks
        # we can use single or double quotes around a column name
        # In this case, it will create a histogram from every single
        # value in the 'Released_Year' column, which will help us to identify
        # the periods with the highest number of 'good' films
        )
)
