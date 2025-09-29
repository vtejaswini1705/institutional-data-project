import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/sample_students.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
year_filter = st.sidebar.multiselect(
    "Select Enrollment Year(s):",
    options=df["enrollment_year"].unique(),
    default=df["enrollment_year"].unique()
)
major_filter = st.sidebar.multiselect(
    "Select Major(s):",
    options=df["major"].unique(),
    default=df["major"].unique()
)

filtered_df = df[
    (df["enrollment_year"].isin(year_filter)) &
    (df["major"].isin(major_filter))
]

# Main dashboard
st.title("📊 Institutional Data Dashboard")
st.markdown("Explore enrollment, retention, and demographics with interactive filters.")

# Enrollment by year
st.subheader("Enrollment by Year")
enrollment_by_year = filtered_df["enrollment_year"].value_counts().sort_index()

fig, ax = plt.subplots()
sns.barplot(x=enrollment_by_year.index, y=enrollment_by_year.values, ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Total Students")
st.pyplot(fig)

# Enrollment by major
st.subheader("Enrollment by Major")
enrollment_by_major = filtered_df["major"].value_counts()

fig, ax = plt.subplots()
sns.barplot(y=enrollment_by_major.index, x=enrollment_by_major.values, ax=ax)
ax.set_xlabel("Total Students")
ax.set_ylabel("Major")
st.pyplot(fig)

# Gender distribution
st.subheader("Gender Distribution")
gender_counts = filtered_df["gender"].value_counts()

fig, ax = plt.subplots()
ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

# Average age by major
st.subheader("Average Age by Major")
avg_age_by_major = filtered_df.groupby("major")["age"].mean()

fig, ax = plt.subplots()
sns.barplot(y=avg_age_by_major.index, x=avg_age_by_major.values, ax=ax)
ax.set_xlabel("Average Age")
ax.set_ylabel("Major")
st.pyplot(fig)

st.markdown("---")
st.markdown("⚙️ Built with Streamlit · Data is mock institutional dataset")
