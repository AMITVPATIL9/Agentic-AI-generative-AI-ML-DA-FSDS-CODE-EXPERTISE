import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load data
movies = pd.read_csv(r"C:\Users\ammyg\Desktop\DATA SCIENCE\clasroom material\25 nov\MOVIE RATINGS _ ADVANCE VISUALIZATION _ EDA 1\Movie-Rating.csv")



# Page Title
st.title("Movie Data Explorer Dashboard")

# Sidebar selections
st.sidebar.header("Chart Controls")

x_axis = st.sidebar.selectbox("Select X Axis", movies.columns)
y_axis = st.sidebar.selectbox("Select Y Axis", movies.columns)
chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ("Scatter Plot", "Line Chart", "Bar Chart", "KDE Plot")
)

# Display Dataframe option
if st.checkbox("Show Dataset"):
    st.dataframe(movies)

# Generate chart
st.subheader(f"{chart_type} of {y_axis} vs {x_axis}")

fig, ax = plt.subplots()

if chart_type == "Scatter Plot":
    sns.scatterplot(data=movies, x=x_axis, y=y_axis, ax=ax)
elif chart_type == "Line Chart":
    sns.lineplot(data=movies, x=x_axis, y=y_axis, ax=ax)
elif chart_type == "Bar Chart":
    sns.barplot(data=movies, x=x_axis, y=y_axis, ax=ax)
elif chart_type == "KDE Plot":
    sns.kdeplot(data=movies, x=x_axis, y=y_axis, fill=True, ax=ax)

st.pyplot(fig)
