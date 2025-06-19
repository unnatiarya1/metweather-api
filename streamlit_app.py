import streamlit as st
import pandas as pd
import requests
import altair as alt

API = "https://metweather-api.onrender.com/api/climate/"

st.title("🌤️ UK Climate Data Visualizer")

year = st.selectbox("Year", list(range(1990, 2024))[::-1])
region = st.selectbox("Region", ["UK"])
parameter = st.selectbox("Parameter", ["Tmax"])

params = {
    "year": year,
    "region": region,
    "parameter": parameter
}

response = requests.get(API, params=params)

if response.status_code == 200:
    data = response.json()
    if data:
        df = pd.DataFrame(data)
        df["Month"] = df["month"]
        df["Temperature"] = df["value"]

        chart = alt.Chart(df).mark_line().encode(
            x='Month:O',
            y='Temperature:Q',
            tooltip=['month', 'value']
        ).properties(title=f"{parameter} in {year} ({region})")

        st.altair_chart(chart, use_container_width=True)
    else:
        st.warning("No data available for selection.")
else:
    st.error("Failed to fetch data.")
