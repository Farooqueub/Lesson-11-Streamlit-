
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

# Title
st.title("Umaiza Farooque's Penguin App")

# Load the penguins dataset
penguins = sns.load_dataset("penguins").dropna()

# First Plot: Flipper Length vs Body Mass
st.subheader("Penguin Flipper Length vs Body Mass")
fig1 = px.scatter(
    penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    color="species",
    title="Flipper Length vs Body Mass"
)
st.plotly_chart(fig1)

# Second Plot: Violin Plot
st.subheader("Violin Plot: Penguin Body Mass by Species and Sex")
fig2 = px.violin(
    penguins,
    x="species",
    y="body_mass_g",
    color="sex",
    box=True,
    points="all"
)
fig2.update_layout(title="Penguin Body Mass by Species and Sex")
st.plotly_chart(fig2)
