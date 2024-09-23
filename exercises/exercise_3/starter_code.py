import pandas as pd
import plotly.express as px
import geopandas
import matplotlib.pyplot as plt

##################################################################
# Display a table of just the medal winners in Athletics in 2012
##################################################################

# ========================== #
sport = "Athletics"
year = 2012
# ========================== #

country_medals_by_event = pd.read_csv("country_medals_by_event.csv")

country_medals_by_event_filtered = (
    country_medals_by_event[
        (country_medals_by_event["Sport"] == sport) &
        (country_medals_by_event["Year"] == year)
    ])

print(country_medals_by_event_filtered[['Event', 'Bronze', 'Silver', 'Gold']])

###########################################################
# Display a plot of the medals won by a country over time
###########################################################

# ========================== #
chosen_country = "UK"
# ========================== #

medals_per_country_per_year = pd.read_csv("medals_per_country_per_year.csv")

medals_per_country_per_year_long = medals_per_country_per_year.melt(id_vars=["Year", "Country", "NOC"])

fig = px.line(medals_per_country_per_year_long[medals_per_country_per_year_long["Country"] == chosen_country],
        y="value", x="Year", color="variable",
        color_discrete_sequence=["orange", "silver", "gold", "blue"],
        title=f"Medals Won over Time - {chosen_country}")

fig.show()

###############################################################
# Print out the country that won the most gold medals in 2012
###############################################################

medals_per_country_per_year = pd.read_csv("medals_per_country_per_year.csv")

medals_per_country_per_year_filtered = medals_per_country_per_year[medals_per_country_per_year["Year"] == year]

top_gold_medal_winner_row = medals_per_country_per_year.sort_values(["Gold"], ascending=False).head(1)

print(f"The country that won the most medals in 2012 was {top_gold_medal_winner_row['Country'].values[0]}" +
      f" with {top_gold_medal_winner_row['Gold'].values[0]:.0f} gold medals.")


###############################################################
# Print out the number of gold medals won by the select country in 2012
###############################################################

medals_chosen_country = (
    medals_per_country_per_year[
        (medals_per_country_per_year["Year"] == year) &
        (medals_per_country_per_year["Country"] == chosen_country)
        ]
    )

print(f"The {chosen_country} won {medals_chosen_country['Gold'].values[0]:.0f} gold medals in 2012.")

#########################################
# Print a map of medal winners in 2012
#########################################

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
