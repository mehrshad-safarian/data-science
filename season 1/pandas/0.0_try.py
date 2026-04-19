import pandas as pd 
df = pd.read_csv("I:/begining og data_scince/pandas/data.csv")
print (df.head())
print()
print (df.info)
print()
print (df["Name"])