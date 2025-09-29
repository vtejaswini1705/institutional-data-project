import pandas as pd

# Load sample student data
df = pd.read_csv("data/sample_students.csv")

# Basic cleaning
df.dropna(inplace=True)  # remove missing values
df['major'] = df['major'].str.title()  # standardize major names

# Save cleaned version
df.to_csv("data/cleaned_students.csv", index=False)

print("✅ Data cleaned and saved to data/cleaned_students.csv")
