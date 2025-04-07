import pandas as pd
df=pd.read_csv(r"C:\Users\yaswa\OneDrive\Desktop\DA\diabetes.csv")
subset1 = df[["Pregnancies", "Glucose", "Outcome"]]  
print(subset1.head())
high_glucose = df[df["Glucose"] > 140]
print(high_glucose.head())
subset2 = df.iloc[0:10, 1:4]  
print(subset2)
#AGGREGATION FUNCTIONS
print(df[["Glucose", "BloodPressure"]].mean())  
print(df[["Age", "BMI"]].sum())  
grouped = df.groupby("Outcome").mean()
print(grouped)