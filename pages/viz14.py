import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.write("Distribution of movie and tv series by year")

df = pd.DataFrame(pd.read_pickle(r'dataset\data-viz14.pkl'))

# st.write(df)

df_movies = df[df['titleType'] == 'movie']
df_tvSeries = df[df['titleType'] == 'tvSeries']

movies_per_year = df_movies['startYear'].value_counts().sort_index()

chart_data = pd.DataFrame({
    "Year": df['startYear'],
    "Movies": df_movies['primaryTitle'],
    "TV Series": df_tvSeries['primaryTitle']
})

st.bar_chart(chart_data, x="Year", y=["Movies", "TV Series"], x_label='Released Year', y_label='Number of Movies and Series Titles')

# st.bar_chart(data=df, x=None, y=df['primaryTitle'], x_label='Released Year', y_label='Number of Movies and Series Titles', color=None, horizontal=False, width=None, height=None, use_container_width=True)