import streamlit as st
import folium
import geopandas
import pandas as pd
from streamlit_folium import st_folium # New import

st.set_page_config(layout="wide")

st.title('Simple Map Example')

# Read in our dataframe
# Notice here I'm just loading it from a repository - we could also load it from local storage
# as long as the same data will be available in the same relative position when we deploy our web app
car_travel_time_lookup = pd.read_csv("https://github.com/hsma-programme/h6_3c_interactive_plots_travel/raw/main/h6_3c_interactive_plots_travel/example_code/travel_matrix_minutes.zip",
                                     index_col="LSOA")

car_travel_time_lookup['shortest'] = (
    # axis = 1 means row-wise minimum (instead of columnwise)
    car_travel_time_lookup.min(axis=1)
)

###########################
# Create the map in Folium
###########################
# This is no different to usual!

lsoa_geojson_path = 'https://github.com/hsma-programme/h6_3c_interactive_plots_travel/raw/main/h6_3c_interactive_plots_travel/example_code/LSOA_2011_Boundaries_Super_Generalised_Clipped_BSC_EW_V4.geojson'

lsoa_boundaries = geopandas.read_file(lsoa_geojson_path).rename(columns={"LSOA11NM":"LSOA"})
lsoa_boundaries = lsoa_boundaries.cx[53:55, -4.5:-2.5]

# Create the blank map object
travel_time_map_interactive = folium.Map(
    location=[55, -3.5],
    zoom_start=5.25,
    tiles='cartodbpositron'
    )

choropleth = folium.Choropleth(
    geo_data=lsoa_boundaries, # dataframe with geometry in it
    data=car_travel_time_lookup.reset_index(), # dataframe with data in - may be the same dataframe or a different one
    columns=['LSOA', 'shortest'], # [key (field for geometry), field to plot]
    key_on='feature.properties.LSOA',
    fill_color='OrRd',
    fill_opacity=0.4,
    line_weight=0.3,
    legend_name='Travel Time',
    highlight=True, # highlight the LSOA shape when mouse pointer enters it
    smooth_factor=0
    )

choropleth = choropleth.add_to(travel_time_map_interactive)

###################################
# KEY NEW BIT
###################################
# Display the map
####################################
# This is the only code we need to add in to display the map in Streamlit!
# We can pass in use_container_width=True to ensure it uses the maximum available space
st_folium(travel_time_map_interactive, use_container_width=True)

# Let's display the dataframe too
st.dataframe(car_travel_time_lookup)
