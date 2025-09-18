import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("sample_labs.csv")

# Print the data
print("Here is the lab data:\n")
print(df)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Plot the lab values
plt.plot(df["date"], df["value"], marker='o', label="Lab Value")

# Add reference range as shaded area
plt.fill_between(df["date"], df["ref_low"], df["ref_high"], color='green', alpha=0.1, label="Normal Range")

# Highlight abnormal values in red
abnormal = df[(df["value"] < df["ref_low"]) | (df["value"] > df["ref_high"])]
plt.scatter(abnormal["date"], abnormal["value"], color="red", zorder=5, label="Abnormal")

# Labels and title
plt.xlabel("Date")
plt.ylabel(df["unit"].iloc[0])  # use the first row unit
plt.title(f"Trend of {df['test_name'].iloc[0]} Levels")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
