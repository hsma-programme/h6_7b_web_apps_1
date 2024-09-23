import pandas as pd
import plotly.express as px
import geopandas
import matplotlib.pyplot as plt

###########################################################
# Display a plot of the medals won by a country over time
###########################################################

# ========================== #
chosen_country = "UK"
# ========================== #

medals_per_country_per_year = pd.read_csv("medals_per_country_per_year.csv")

# Turn the dataframe into a 'long' format for plotting - don't worry about what that means!
# What we'll end up with is a dataframe with columns for Year, Country, Medal Type (called 'variable')
# and number of medals (called 'value')
medals_per_country_per_year_long = medals_per_country_per_year.melt(id_vars=["Year", "Country", "NOC"])

# Create a line plot using the plotly express library
fig = px.line(
    # Filter our dataframe to just our 'chosen_country'
    medals_per_country_per_year_long[medals_per_country_per_year_long["Country"] == chosen_country],
    # The value to plot on the vertical axis - this corresponds to the number of medals
    y="value",
    # Plot the year on the x axis
    x="Year",
    # Plot the number of medals on the y axis
    color="variable",
    # Colour the medals as orange for bronze, silver for silver, gold for gold, and blue for total
    color_discrete_sequence=["orange", "silver", "gold", "blue"],
    # Add a title, using an f-string to include the name of the chosen country
    title=f"Medals Won over Time - {chosen_country}"
    )

# Display the plotly plot in an interactive window
fig.show()

##################################################################
# Display a table of just the medal winners in Athletics in 2012
##################################################################

# ========================== #
year = 2012
# ========================== #

# ========================== #
sport = "Athletics"
# ========================== #

country_medals_by_event = pd.read_csv("country_medals_by_event.csv")

country_medals_by_event_filtered = (
    country_medals_by_event[
        (country_medals_by_event["Sport"] == sport) &
        (country_medals_by_event["Year"] == year)
    ])

print(country_medals_by_event_filtered[['Event', 'Bronze', 'Silver', 'Gold']])

############################################################################
# Print out the country that won the most gold medals in the selected year
############################################################################
# Hint - this might make a nice metric card!

# ========================== #
year = 2012
# ========================== #

medals_per_country_per_year = pd.read_csv("medals_per_country_per_year.csv")

# Filter the dataframe to just the rows for the selected year
medals_per_country_per_year_filtered = (
    medals_per_country_per_year[medals_per_country_per_year["Year"] == year]
    )

# Sort by number of gold medals won in descending order (so the most medals is at the top of the table)
# Then just keep the first row (i.e. the one for the country with the most gold medals in the
# selected year)
top_gold_medal_winner_row = (
    medals_per_country_per_year
    .sort_values(["Gold"], ascending=False)
    .head(1)
    )

# Using an f string, populate the text with the number of gold medals this country won
print(f"The country that won the most medals in 2012 was" +
      f" {top_gold_medal_winner_row['Country'].values[0]}" +
      f" with {top_gold_medal_winner_row['Gold'].values[0]:.0f} gold medals.")


###########################################################################
# Print out the number of gold medals won by the selected country in 2012
###########################################################################
# Hint - this might make a nice metric card!

# ========================== #
year = 2012
# ========================== #

# ========================== #
chosen_country = "UK"
# ========================== #

# Filter the medals table down to the selected year and country
medals_chosen_country = (
    medals_per_country_per_year[
        (medals_per_country_per_year["Year"] == year) &
        (medals_per_country_per_year["Country"] == chosen_country)
        ]
    )

# Print out how many medals the country won
print(f"The {chosen_country} won {medals_chosen_country['Gold'].values[0]:.0f}" +
      f" gold medals in {year}.")

# Calculate the difference between this country and the top scorer
# Hint - this might be an interesting value to display as part of a metric card...
difference = medals_chosen_country['Gold'].values[0] - top_gold_medal_winner_row['Gold'].values[0]

# Print out a message with the difference
if difference < 0:
    print(f"This was {abs(difference):.0f} fewer" +
          f" than {top_gold_medal_winner_row['Country'].values[0]}")
# Unless the difference = 0, in which case the selected country is also the most successful country
else:
    print("They were the top country for gold medals in that year.")


#########################################
# Print a map of medal winners in 2012
#########################################

# ========================== #
year = 2012
# ========================== #

# ========================== #
selected_medal_type="Gold"
# ========================== #

medals_per_country_per_year = pd.read_csv("medals_per_country_per_year.csv")

country_outlines = geopandas.read_file("countries_outlines.geojson")

medals_per_country_per_year_gdf = pd.concat([
    pd.merge(country_outlines, medals_per_country_per_year, left_on="id", right_on="NOC", how="inner"),
    pd.merge(country_outlines, medals_per_country_per_year, left_on="name", right_on="Country", how="inner")
]).drop_duplicates()

fig, ax = plt.subplots(figsize=(15, 8))

ax = medals_per_country_per_year_gdf[medals_per_country_per_year_gdf["Year"] == year].plot(
    selected_medal_type, legend=True, ax=ax
    )

ax.axis('off')

plt.title(f"Number of {selected_medal_type} Medals in {year}")

fig.show()


###################################################
# Print out possible countries to select from for
# the next run of the script
###################################################

print("The countries you could choose from are: " +
      f"{medals_per_country_per_year['Country'].unique().tolist()}")

print(f"Choose a year between {medals_per_country_per_year['Year'].min()}" +
      f" and {medals_per_country_per_year['Year'].max()}")

print("The sports you could choose from are: " +
      f"{country_medals_by_event['Sport'].unique().tolist()}")
