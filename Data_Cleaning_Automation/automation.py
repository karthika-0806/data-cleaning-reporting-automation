import pandas as pd
import matplotlib.pyplot as plt

print("Loading Data...")

df = pd.read_csv("hotel_bookings.csv")

# Original records
original_rows = len(df)

# Missing values count
missing_before = df.isnull().sum().sum()

# Remove duplicates
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

# Fill numeric columns
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill text columns
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

# Report
report = f"""
DATA CLEANING REPORT
====================

Original Records : {original_rows}

Records After Cleaning : {len(df)}

Duplicates Removed : {duplicates_removed}

Missing Values Before Cleaning : {missing_before}

Missing Values After Cleaning : {df.isnull().sum().sum()}
"""

with open("report.txt", "w") as f:
    f.write(report)

print(report)

# Chart
if "Sales" in df.columns:

    plt.figure(figsize=(6,4))
    plt.bar(df["Name"], df["Sales"])
    plt.title("Sales by Person")
    plt.xlabel("Name")
    plt.ylabel("Sales")
    plt.savefig("sales_chart.png")

print("Automation Completed Successfully!")
import matplotlib.pyplot as plt

# Missing values chart
missing_values = df.isnull().sum()

missing_values.plot(kind='bar')

plt.title("Missing Values After Cleaning")
plt.tight_layout()
plt.savefig("missing_values_chart.png")
plt.close()
summary_stats = df.describe(include='all')

summary_stats.to_csv("summary_statistics.csv")