import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="EcoPulse: Inflation Forecasting Dashboard",
    layout="wide"
)

st.title("EcoPulse: Macroeconomic Inflation Forecasting Engine")
st.markdown("### Developed by Sunbal Sharif")
st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Project Data Status")

    if os.path.exists("EcoPulse_Master_Dataset.csv"):
        df = pd.read_csv("EcoPulse_Master_Dataset.csv")

        st.success("Master Dataset Connected")
        st.metric("Total Records", f"{len(df):,}")

        st.subheader("Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

    else:
        st.error("Master Dataset file not found.")

with col2:
    st.subheader("Statistical Analysis and Trends")

    if os.path.exists("EcoPulse_Analysis_Chart.png"):
        st.image(
            "EcoPulse_Analysis_Chart.png",
            caption="Crude Oil Prices and Inflation Trends",
            use_container_width=True
        )
    else:
        st.warning("Analysis chart not found.")
