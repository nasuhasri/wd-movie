import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Distribution of movie and tv series by year")

df = pd.DataFrame(pd.read_pickle(r'dataset\data-viz14.pkl'))

# get movies data
df_movies = df[df['titleType'] == 'movie']
# get series data
df_tvSeries = df[df['titleType'] == 'tvSeries']

chart_data = pd.DataFrame({
    "Year": df['startYear'],
    "Movies": df_movies['primaryTitle'],
    "TV Series": df_tvSeries['primaryTitle']
})

# draw chart
st.bar_chart(chart_data, x="Year", y=["Movies", "TV Series"], x_label='Released Year', y_label='Number of Movies and Series Titles')