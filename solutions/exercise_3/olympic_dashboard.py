import streamlit as st
import pandas as pd
import geopandas
import folium
import plotly.express as px
import matplotlib.pyplot as plt
from io import StringIO
from streamlit_folium import st_folium

#####################################
# Streamlit Setup Steps
#####################################

# Start by making sure we use the full width; useful for a dashboard style
st.set_page_config(layout="wide")

st.title("Olympic History Dashboard")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Summary",
    "Country Statistics",
    "Map",
    "Athlete Statistics",
    "Athlete Details",
    "Event Statistics"
])

###################################
# Data imports
###################################

medals_per_country_per_year = pd.read_csv("../../exercises/exercise_3/medals_per_country_per_year.csv")
country_outlines = geopandas.read_file("../../exercises/exercise_3/countries_outlines.geojson")
athlete_statistics = pd.read_csv("../../exercises/exercise_3/athlete_details_eventwise.csv")

####################################
# Tab 1 - Summary Stats
####################################
with tab1:
    col1_1, col1_2 = st.columns(2)

    with col1_1:
        total_medals_all_time = (
            medals_per_country_per_year.drop(columns=["Year", "NOC"])
            .groupby('Country').sum()
            .reset_index()
            .sort_values('Total', ascending=False)
            )
        st.subheader("Total Medals")
        st.dataframe(total_medals_all_time, use_container_width=True, hide_index=True)

    with col1_2:
        st.subheader("Medals per Country Per Year - Highest First")
        st.dataframe(medals_per_country_per_year.sort_values("Total", ascending=False),
                     use_container_width=True, hide_index=True)

    rows_to_display = st.slider("Select the number of countries to display",
                                min_value=3,
                                max_value=len(total_medals_all_time),
                                value=10
                                )

    st.plotly_chart(
        px.bar(total_medals_all_time.head(rows_to_display), x='Country', y='Total',
       title=f"Total Number of Medals since 1896 - Top {rows_to_display} Countries")
    )

####################################
# Tab 2 - Country Stats
####################################

with tab2:
    col2_1, col2_2 = st.columns(2)

    with col2_1:
        chosen_country = st.selectbox(
            "Choose a country",
            options=medals_per_country_per_year['Country'].drop_duplicates().tolist()
        )

    with col2_2:
        chosen_medal = st.radio("Choose a Medal Type",
                                ["Total", "Gold", "Silver", "Bronze"])

    country_medal_chart = px.line(
        medals_per_country_per_year[medals_per_country_per_year["Country"] == chosen_country],
        y=chosen_medal,
        x="Year",
        title=f'{chosen_medal} medals for {chosen_country}'
        )

    st.plotly_chart(
        country_medal_chart
    )

    buffer = StringIO()
    country_medal_chart.write_html("country_medal_chart.html")

    with open("country_medal_chart.html", "rb") as chart_file_html:
        st.download_button(
            label='Download This Plot as an Interactive HTML file',
            data=chart_file_html,
            file_name=f'{chosen_medal} medals for {chosen_country}.html',
            mime='text/html'
        )

    medals_per_country_per_year_long = medals_per_country_per_year.melt(id_vars=["Year", "Country", "NOC"])

    country_medal_chart_all =  px.line(medals_per_country_per_year_long[medals_per_country_per_year_long["Country"] == chosen_country],
            y="value", x="Year", color="variable",
            color_discrete_sequence=["orange", "silver", "gold", "blue"])

    st.plotly_chart(
        country_medal_chart_all
    )

    buffer = StringIO()
    country_medal_chart_all.write_html("country_medal_chart_all.html")

    with open("country_medal_chart_all.html", "rb") as chart_file_all_html:
        st.download_button(
            label='Download This Plot as an Interactive HTML file',
            data=chart_file_all_html,
            file_name=f'Medals for {chosen_country}.html',
            mime='text/html'
        )
####################################
# Tab 3 - Map
####################################

with tab3:
    col3_1, col3_2 = st.columns([0.3,0.7])

    with col3_1:
        chosen_medal_map = st.radio("Choose a Medal Type",
                            ["Total", "Gold", "Silver", "Bronze"],
                            key="medal_select_2")

    medals_per_country_per_year_gdf = pd.concat([
                pd.merge(country_outlines, medals_per_country_per_year, left_on="id", right_on="NOC", how="inner"),
                pd.merge(country_outlines, medals_per_country_per_year, left_on="name", right_on="Country", how="inner")
            ]).drop_duplicates()

    with col3_2:
        selected_year = st.slider(
            "Select the Year to Display",
            value=2012,
            min_value=medals_per_country_per_year_gdf.Year.min(),
            max_value=medals_per_country_per_year_gdf.Year.max(),
            step=4
        )

    #create base map
    world_map_medals = folium.Map(
        location=[50.71671, -3.50668],
        zoom_start=2,
        tiles='cartodbpositron'
        )

    # create and add choropleth map
    choropleth = folium.Choropleth(
        geo_data=medals_per_country_per_year_gdf[medals_per_country_per_year_gdf["Year"] == selected_year], # dataframe with geometry in it
        data=medals_per_country_per_year_gdf[medals_per_country_per_year_gdf["Year"] == selected_year], # dataframe with data in - may be the same dataframe or a different one
        columns=['name', chosen_medal_map], # [key (field for geometry), field to plot]
        key_on='feature.properties.Country'
        )

    choropleth = choropleth.add_to(world_map_medals)

    choropleth = choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(
            ['name', chosen_medal_map],
            labels=True
            )
    )

    st_folium(world_map_medals, use_container_width=True)

    world_map_medals.save("country_medal_map.html")

    with open("country_medal_map.html", "rb") as map_file_html:
        st.download_button(
            label='Download This Map as an Interactive HTML file',
            data=map_file_html,
            file_name=f'{chosen_medal_map} Medals map for {selected_year}.html',
            mime='text/html'
        )

####################################
# Tab 4 - Athlete Statistics
####################################

with tab4:
    distinct_athletes_per_year = athlete_statistics[['Name', 'Year','Country','Sex', 'Age', 'Height', 'Weight']].drop_duplicates()

    athlete_counts_by_sex_by_year = distinct_athletes_per_year.value_counts(['Sex', 'Year']).reset_index()

    athlete_counts_by_sex_by_year['total_athletes_both_sex_in_year'] = athlete_counts_by_sex_by_year['count'].groupby(athlete_counts_by_sex_by_year['Year']).transform('sum')
    athlete_counts_by_sex_by_year['Percentage of Athletes'] = athlete_counts_by_sex_by_year['count'] / athlete_counts_by_sex_by_year['total_athletes_both_sex_in_year']

    st.plotly_chart(
        px.bar(athlete_counts_by_sex_by_year,
        x="Year", y="Percentage of Athletes", color="Sex",
        title=f"Change in Gender Split Over Time")
    )

    col4_1, col4_2, col4_3, col4_4 = st.columns(4)

    col4_1.metric("Oldest Athlete",
              athlete_statistics.Age.max(skipna=True))

    col4_2.metric("Youngest Athlete",
              athlete_statistics.Age.min(skipna=True))

    col4_3.metric("Tallest Athlete (cm)",
              athlete_statistics.Height.max(skipna=True))

    col4_4.metric("Shortest Athlete (cm)",
              athlete_statistics.Height.min(skipna=True))


    st.subheader(f"Most Successful Athletes up to and including {athlete_statistics.Year.max():.0f} games")

    medallers = athlete_statistics[~athlete_statistics['Medal'].isna()]

    st.dataframe(medallers.value_counts(['Name', 'Country', 'NOC']))

####################################
# Tab 5 - Athlete Details
####################################

with tab5:
    search_string = st.text_input("Enter an athlete name to search for", value="Simone")

    st.dataframe(
        athlete_statistics[athlete_statistics["Name"].str.contains(search_string)]
    )


####################################
# Tab 6 - Event Details
####################################

with tab6:
    st.subheader("Sports with the most distinct events")

    selected_year_event = selected_year = st.slider(
            "Select the Year to Display",
            value=2012,
            min_value=medals_per_country_per_year_gdf.Year.min(),
            max_value=medals_per_country_per_year_gdf.Year.max(),
            step=4,
            key="year_select_event"
        )

    athlete_statistics_year = athlete_statistics[athlete_statistics["Year"] == selected_year_event]

    events_by_sport_in_year = athlete_statistics_year[['Sport', 'Event']].drop_duplicates().value_counts('Sport').reset_index()

    col6_1, col6_2 = st.columns([0.3, 0.7])

    with col6_1:
        st.dataframe(events_by_sport_in_year, hide_index=True, use_container_width=True)

    with col6_2:
        st.plotly_chart(
            px.bar(events_by_sport_in_year, x="Sport", y="count")
        )

    st.subheader("Explore Events by Sport")

    selected_sport = st.selectbox(
        "Select a sport",
        athlete_statistics["Sport"].drop_duplicates().tolist()
    )

    athlete_statistics_year_sport = athlete_statistics_year[athlete_statistics_year["Sport"] == selected_sport]

    events_in_year = athlete_statistics_year_sport[['Sport', 'Event']].drop_duplicates().reset_index(drop=True)

    st.metric(
        f"{selected_sport} Events in {selected_year}",
        len(events_in_year)
    )

    col6_3, col6_4 = st.columns([0.4, 0.6])

    with col6_3:
        st.dataframe(
            events_in_year,
            hide_index=True,
            use_container_width=True
        )

    athlete_statistics_sport = athlete_statistics[athlete_statistics["Sport"] == selected_sport]

    events_per_year_by_sport = (
        athlete_statistics_sport[['Year', 'Event']]
        .drop_duplicates()
        .value_counts(['Year'])
        .reset_index()
    )

    with col6_4:
        st.plotly_chart(
            px.line(events_per_year_by_sport.sort_values("Year"), x="Year", y="count",
                    markers=True, title=f"{selected_sport} Events Per Olympics",
                    range_x=[athlete_statistics.Year.min(), athlete_statistics.Year.max()])
        )
