import pandas as pd
import matplotlib.pyplot as plt

# Simulated authentication logs dataset
data = {
    "user_id": ["A123", "B456", "C789", "D012", "E345", "F678", "G901", "H234", "I567", "J890"],
    "failed_attempts": [1, 3, 12, 5, 20, 2, 7, 15, 8, 11],
    "geo_location": ["US", "Germany", "Russia", "India", "China", "US", "Russia", "China", "US", "Germany"],
    "time_of_attempt": ["08:12", "12:45", "03:30", "17:50", "23:15", "14:10", "04:20", "02:05", "21:45", "10:30"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Identify users with high failed attempts
threshold = 10
high_risk_accounts = df[df["failed_attempts"] > threshold]

# Print flagged accounts
print("🚨 High-Risk Accounts Identified:")
print(high_risk_accounts)

# Generate a bar chart for failed attempts
plt.figure(figsize=(8, 5))
plt.bar(df["geo_location"], df["failed_attempts"], color="orange")
plt.title("Failed Login Attempts by Country")
plt.xlabel("Country")
plt.ylabel("Total Failed Attempts")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Save the visualization
plt.savefig("failed_logins_chart.png")
plt.show()
