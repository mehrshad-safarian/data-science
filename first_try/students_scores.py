import pandas as pd

df = pd.read_csv("C:/Users/mehrshad/Desktop/Data-science/data-science/first_try/students.csv")
mean_age = df["Age"].mean()
print("Age av:", mean_age)
mean_grade = df["Grade"].mean()
print("Grade av:", mean_grade)