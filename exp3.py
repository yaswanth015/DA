import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\yaswa\OneDrive\Desktop\DA\diabetes.csv")

# Convert numeric columns if necessary
numeric_cols = ["Glucose", "BloodPressure", "BMI", "Age", "Insulin"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

### 🔹 Line Plot: Age vs Glucose
plt.plot(df["Age"], df["Glucose"], marker="o", linestyle="-", color="b")
plt.xlabel("Age")
plt.ylabel("Glucose Level")
plt.title("Age vs Glucose Level")
plt.show()

### 🔹 Scatter Plot: BMI vs Insulin
plt.scatter(df["BMI"], df["Insulin"], color="r", alpha=0.5)
plt.xlabel("BMI")
plt.ylabel("Insulin")
plt.title("BMI vs Insulin Levels")
plt.show()

### 🔹 Bar Chart: Average Blood Pressure by Outcome
bp_avg = df.groupby("Outcome")["BloodPressure"].mean()
plt.bar(["No Diabetes", "Diabetes"], bp_avg, color=["green", "red"])
plt.xlabel("Diabetes Outcome")
plt.ylabel("Average Blood Pressure")
plt.title("Blood Pressure Comparison")
plt.show()

### 🔹 Box Plot: Distribution of Glucose
sns.boxplot(x=df["Glucose"], color="blue")
plt.title("Glucose Level Distribution")
plt.show()