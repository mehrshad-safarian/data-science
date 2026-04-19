import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Creating the dataset
df = pd.DataFrame({
    'user' : [0,1,2,3,],
    'sex' : ['male', 'female', 'female', 'male'],
    'city' : ['Tehran', 'Shiraz', 'Tehran', 'Lahijan'],
    'loyalty_level' : ['low', 'mid', 'high', 'mid'],
    'purched_product' : ['clothes', 'purse', 'shoes', 'clothes']
})
print("main_dataset:")
print(df)
print("\n" + "=" * 50 + "\n") 

# Loyalty levels Encoding
loyalty_level = {"low":0, "midrate":1, "high":2}
df['loyalty_level'] = df['loyalty_level'].map(loyalty_level)
print("after label encoding satisfaction grade for:")
print("\n" + "-" * 30 + "\n")

# One-HotEncoding for nominal variables
df_encoded = pd.get_dummies(
    df,
    columns = ['sex', 'city', 'purched_product'],
    prefix = ['sex', 'city', 'purched_product']
)
print("after one-HotEncoding with pd.get_dummies():")
print(df_encoded)
print("n" + "-" * 30 + "\n")
