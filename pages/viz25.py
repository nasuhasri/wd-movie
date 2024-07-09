import streamlit as st
import pandas as pd
import numpy as np

st.write("Distribution of women according to region")

df = pd.DataFrame(pd.read_pickle(r'dataset\data-viz25.pkl'))

chart_data = pd.DataFrame({
    "Region": df['region'],
    "Female Count": df['primaryName']
})

st.line_chart(chart_data, x="Region", y="Female Count", x_label="Region", y_label="Number of Female(s)")