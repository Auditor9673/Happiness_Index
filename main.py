import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Happiness Index data 2022")
option_1 = st.selectbox("Select the data for the X-axis", ("GDP", "Corruption", "Generosity",
                                                           "Freedom to Make Life Choices", "Life Expectancy",
                                                           "Social Support", "Happiness"))
option_2 = st.selectbox("Select the data for the Y-axis", ( "Happiness", "Social Support",
                                                            "Life Expectancy", "Freedom to Make Life Choices",
                                                            "Generosity", "Corruption", "GDP"))
st.subheader(f"Comparing {option_1} and {option_2}")

df = pd.read_csv("data/happy.csv")
x_plot = df[option_1.lower().replace(" ", "_")]
y_plot = df[option_2.lower().replace(" ", "_")]

figure = px.scatter(x=x_plot, y=y_plot, labels={"x":option_1, "y":option_2})
st.plotly_chart(figure)

if option_1 == "Corruption" or option_2 == "Corruption":
    st.text("This is corruption by ranking for countries, so the lower the number, the higher the corruption.")