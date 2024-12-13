import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
option_1 = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity",
                                                           "Corruption", "Life Expectancy"))
option_2 = st.selectbox("Select the data for the Y-axis", ("Life Expectancy", "Corruption",
                                                           "Happiness", "Generosity", "GDP"))
st.subheader(f"{option_1} and {option_2}")

df = pd.read_csv("data/happy.csv")
x_plot = df[option_1.lower().replace(" ", "_")]
y_plot = df[option_2.lower().replace(" ", "_")]

figure = px.scatter(x=x_plot, y=y_plot, labels={"x":option_1, "y":option_2})
st.plotly_chart(figure)