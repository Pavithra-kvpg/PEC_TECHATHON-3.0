import streamlit as st
import requests
import pandas as pd

st.title("🏥 Hospital Resource Optimisation Dashboard")

if st.button("Get Oxygen Forecast"):
    res = requests.get("http://127.0.0.1:8000/predict?steps=24")
    data = res.json()["forecast"]
    st.line_chart(data)

st.write("Use this dashboard to view forecasted oxygen usage and plan resources.")
