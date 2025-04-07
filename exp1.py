import pandas as pd
df=pd.read_csv(r"C:\Users\yaswa\OneDrive\Desktop\DA\diabetes.csv")
print(df.head())
df.describe()
print(df.isnull().sum())