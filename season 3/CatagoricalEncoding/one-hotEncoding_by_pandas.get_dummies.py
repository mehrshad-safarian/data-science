import pandas as Pd
import numpy as np
df = Pd.DataFrame({
    'sex' : ['male', 'female', 'female', 'male'], 
    'city' : ['Tehran', 'Shiraz', 'Tehran', 'Isfahan'],
})
df_encoded = Pd.get_dummies(
    df,
    columns = ['city', 'sex'],
    prefix = ['city', 'sex']
)
print("after one-HotEncoding with pd.get_dummies():")
print(df_encoded)
print("n" + "-" * 30 + "\n")