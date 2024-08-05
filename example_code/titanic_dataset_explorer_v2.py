import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Titanic Dataset Explorer')


# Import data
try:
    data = pd.read_csv("data/raw_data.csv")

except FileNotFoundError:

    # Download raw data:
    address = 'https://raw.githubusercontent.com/MichaelAllen1966/' + \
                '1804_python_healthcare/master/titanic/data/train.csv'

    data = pd.read_csv(address)

    # Create a data subfolder if one does not already exist
    import os
    data_directory ='./data/'
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    # Save data
    data.to_csv(data_directory + 'raw_data.csv', index=False)


gender_picker = st.radio("Choose a Gender", ["All", "Male Only", "Female Only"])

if gender_picker == "Male Only":
    data_filtered = data[data["Sex"] == "male"].copy()
elif gender_picker == "Female Only":
    data_filtered = data[data["Sex"] == "female"].copy()
else:
    data_filtered = data.copy()

# Display data
st.dataframe(data_filtered)

st.plotly_chart(
    px.bar(
        data_filtered['Survived'].value_counts(),
        title="Number of Passengers"
        )
    )

st.plotly_chart(
    px.box(
        data_filtered[['Pclass', 'Age']],
        x="Pclass",
        y="Age",
        title="Age by Class"
        )
    )
