import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout = "wide")

df  = pd.read_csv("india.csv")
list_of_states = list(df["State"].unique())
list_of_states.insert(0,"Overall India")


st.sidebar.title('India Census 2011')
selected_state = st.sidebar.selectbox("Select State",list_of_states)
primary = st.sidebar.selectbox("Select Primary Parameter",list(df.columns[6:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[6:]))

plot  = st.sidebar.button("Plot Graph")

if plot:
    st.subheader("Size represents "+ primary)
    st.subheader("Color represents "+ secondary)
    if (selected_state == "Overall India"):
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            zoom=4,
            mapbox_style="carto-positron",
            size=primary,
            color=secondary,
            size_max=25,
            width=2000,
            height=800,
            color_continuous_scale=px.colors.sequential.Viridis,
            hover_name = "District"
        )
        st.plotly_chart(fig,use_container_width = True)
    else:
        state_df =df[df["State"] == selected_state]
        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            zoom=6,
            mapbox_style="carto-positron",
            size=primary,
            color=secondary,
            size_max=25,
            width=2000,
            height=800,
            color_continuous_scale=px.colors.sequential.Viridis,
            hover_name="District"
        )
        st.plotly_chart(fig,use_container_width = True)

