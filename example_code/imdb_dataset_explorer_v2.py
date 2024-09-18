import streamlit as st                                                                                              #noqa
import pandas as pd
import plotly.express as px

 # STREAMLIT - give it a title
st.title('IMDB Top 1000 Movies Dataset Explorer')

# This time we're going to load our dataset in locally
# This tells streamlit to look up one level from the folder
# our app file is in, then go into the 'data' folder and look
# for a .csv file called 'imdb_top_1000.csv'
# Note that this might not work if you've called
# streamlit run example_code/imdb_dataset_explorer_v2.py
# but it should work if you have run
# cd example_code
# streamlit run imdb_dataset_explorer_v2.py
# i.e. the difference is in whether you
data = pd.read_csv("../data/imdb_top_1000.csv")

# STREAMLIT - make a dropdown selector box
chosen_certificate = st.selectbox(
    # We tell it what to display as a label next to the drop-down selector
    # You might want to more explicitly tell
    label="Certificate",
    # This looks at the 'Certificate' column of the dataframe 'data'
    # and returns only the unique values in the form of a list
    # So if we had, for example, a column of 'U', 'U', 'PG', 'U', '18', '18'
    # we'd get a list returned of ['U', 'PG', '18']
    # This is a nice robust way to populate our dropdown list with all
    # possible options rather than having to specify the possible options
    # manually, which is handy for a lot of situations where the options
    # may change over time
    options=data['Certificate'].unique()
    # Note that it will automatically select the first value in the options list
    # to be the default value for the selectbox
    )

# Here, we filter the dataframe 'data' down to only the certificate
# that the user has selected
#
# When the user made a selection from the selectbox we defined above,
# it got saved into the variable 'chosen_certificate'
#
# This syntax is effectively saying 'only keep instances in the dataframe 'data'
# where the value for the row in the column 'certificate' is equal to the
# chosen_certificate variable
#
# Here, we choose to overwrite the dataframe 'data' with just the
# filtered dataframe.
# As the code will run from top to bottom again - including loading in
# the dataframe 'data' from the csv when the user changes their selection -
# overwriting the dataframe won't cause any problems.
data = data[data['Certificate'] == chosen_certificate]

# STREAMLIT - display the filtered dataframe
st.dataframe(data)

# STREAMLIT - display a plotly chart
# A bar chart, given a column name where the column contains a
# numeric value or category/string for the x parameter,
# will count up the number of values for each value that appears in that
# column - so it's just doing a counting step for us rather than
# us having to manually count anything up.
st.plotly_chart(
    px.bar(
        data, # Pass in the dataframe 'data' (which has been filtered)
        x="Released_Year", # Look at the column 'released_year'
        # Add a title 'chart'
        title=f"Number of Movies Released per Year: Certificate {chosen_certificate}",
    ))
