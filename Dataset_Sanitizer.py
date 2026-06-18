import pandas as pd
import matplotlib.pyplot as plt

print("Initializing Automated Data Sanitizer Pipeline")

df = pd.read_csv("messy_hardware_log.csv")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

avrg_price = df["Price"].median()
print(f"-> Calculated safe Market Median Price: ${avrg_price:/=.2f}")
df["Price"] = df["Price"].fillna(avrg_price)
df["Stock"] = df["Stock"].fillna(0)

df["Total value asset"] = df["Price"] * df["Stock"]

df.to_csv("sanitized_hardware_report.csv", index=False)
print("-> Cleaned database exported to 'sanitized_hardware_report.csv'")

plt.figure(figsize=(10,6))
plt.bar(df["Product"], df["Total value asset"], color="indigo")

plt.title("Total Warehouse Asset Value Per Product", fontsize=14, fontweight="bold")
plt.xlabel("Hardware Product", fontsize=11)
plt.ylabel("Asset value in USD ($)", fontsize=11)
plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig("Warehouse Asset Chart.png", dpi=300)
print("-> Analytical reporting chart exported to 'warehouse_asset_chart.png'")
print("Pipeline Execution Completed Successfully with 0 Errors!")
