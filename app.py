import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Title
st.title("Student Semester-wise Performance Analysis")

# Load data
df = pd.read_csv("data/student_performance.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

semester_cols = ['Semester_1', 'Semester_2', 'Semester_3', 'Semester_4']

# Mean calculation
mean_scores = df[semester_cols].mean()

st.subheader("Average Marks per Semester")
st.bar_chart(mean_scores)

# Growth calculation
df['Total_Growth'] = df['Semester_4'] - df['Semester_1']

df['Performance_Status'] = np.where(
    df['Total_Growth'] > 0, 'Improving',
    np.where(df['Total_Growth'] < 0, 'Declining', 'Stable')
)

st.subheader("Performance Status")
st.dataframe(df[['Name', 'Total_Growth', 'Performance_Status']])

# Line chart
st.subheader("Performance Trend")
for i in range(len(df)):
    plt.plot(semester_cols, df.loc[i, semester_cols], marker='o', label=df.loc[i, 'Name'])

plt.xlabel("Semester")
plt.ylabel("Marks")
plt.legend()
st.pyplot(plt)
