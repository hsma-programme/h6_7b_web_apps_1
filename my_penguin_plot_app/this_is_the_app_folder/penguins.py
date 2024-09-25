import streamlit as st
import pandas as pd
import palmerpenguins
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide", page_title="My Amazing HSMA App")

st.title("Penguins Dashboard")

penguins_df = pd.read_csv("penguins_df.csv")

with st.expander("Click here for additional information"):
    st.write("Some really useful information")

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Brown_Bluff-2016-Tabarin_Peninsula%E2%80%93Gentoo_penguin_%28Pygoscelis_papua%29_03.jpg/1280px-Brown_Bluff-2016-Tabarin_Peninsula%E2%80%93Gentoo_penguin_%28Pygoscelis_papua%29_03.jpg")

tab1, tab2 = st.tabs(
    ["Penguins per Island Graph",
     "Penguins per Island Dataframe"]
     )

with tab1:
    st.plotly_chart(
        px.bar(
            penguins_df['species'].value_counts(),
            title="Penguins Per Island"
        )
    )

with tab2:
    st.write("There's nothing here yet!")

st.divider()

island_select = st.multiselect("Please select an island",
                             penguins_df["island"].unique()
                             )

penguins_df = penguins_df[penguins_df["island"].isin(island_select)]

col_1, col_2 = st.columns([0.7, 0.3])

with col_1:

    # penguins_df = palmerpenguins.load_penguins()

    st.dataframe(
        penguins_df,
        use_container_width=True,
        column_config={
            "year": st.column_config.NumberColumn(
                "Year Measurement Collected",
                format="%f"
            )
        }
        )

with col_2:
    penguin_scatter = px.scatter(
        penguins_df,
        x="bill_length_mm",
        y="bill_depth_mm",
        color="species"
        )

    st.plotly_chart(
        penguin_scatter
    )
