import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Title
st.title("Titanic Survival Dashboard")

# Sidebar filters
gender = st.sidebar.multiselect("Select Gender:", df['sex'].unique(), default=df['sex'].unique())
pclass = st.sidebar.multiselect("Select Class:", df['class'].unique(), default=df['class'].unique())

# Filter data
filtered = df[df['sex'].isin(gender) & df['class'].isin(pclass)]

# Show table
st.write(filtered.head())

# Plot survival count
fig, ax = plt.subplots()
sns.countplot(x='survived', data=filtered, ax=ax)
st.pyplot(fig)
