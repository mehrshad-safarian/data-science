import pandas as pd
import numpy as np
import time
# Reading the informations
df = pd.read_csv("I:/begining og data_scince/Playstation_Games_Info/" \
"game_details.csv")
print("Reading the data...")
time.sleep(3)
print('read OK!!!')
print()
time.sleep(1.5)
# Showing the first 5 
print(df.head())
print()
# Showing the tail of the dataset
print(df.tail())
print()
# Showing overall info about the dataframe
print(df.info())
print()
# Showing descriptive statics for numeric columns of the dataframe 
print(df.describe())
print()
# Number of lines and columns
print("lines and columns: " ,df.shape)
print()
# Number of the fields and the name of them 
print("name of the fields: " ,df.columns)
print()
# Lines that the console is playstation 3
print(df[df['platform'] == 'PS3'])
print()
# Lines that the meta score is more than 87
print(df[df['metacritic_score'] > 87])
print()
# Average meta score
avg_score = df['metacritic_score'].mean()
print("Average meta score is: " ,avg_score)
print()
# Calculating the variance of the meta score
meta_variance = df['metacritic_score'].var()
print("meta score variance: ", meta_variance)
print()


# A bit of pandas preliminary operations on data's

# Choosing specific line and columns by loc
print(df.loc[[5,7,9],['platform','genre']])
print()
# Checking missing values
print(df.isnull())
print(df.isnull().sum()) #finding the missing values
print()
# Removing the line with missing values
print(df.dropna()) # \|/
# It removes all the lines with at least one NaN it is useful while the numbr of missing data s are low
print()
# Filling missing values with a constant number
print(df.fillna(0)) # All the NaN values will be replaced by 0
# This method is useful in those kinda dataset that are include counting data's
print()
# Filling with avg of a column
print(df.fillna(df['metacritic_score'].mean())) # The missing score of a column will be replaced by that column avg score
print()
# Filtering data's based on conditions 
print(df[df['metacritic_score'] >= 96])
print()