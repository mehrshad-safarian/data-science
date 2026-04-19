import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
df = pd.DataFrame({
    'sex' : ['male', 'female', 'female', 'male'], 
    'city' : ['Tehran', 'Shiraz', 'Tehran', 'Isfahan'],
    'satisfaction_grade' : ['low', 'average', 'high', 'average']
})
print("main_dataset:")
print(df)
print("\n" + "=" * 50 + "\n") 
satisfaction_order = {"low":0, "midrate":1, "high":2}
df['satisfaction_grade_code'] = df['satisfaction_grade'].map(satisfaction_order)
print("after label encoding satisfaction grade for:")
print("\n" + "-" * 30 + "\n")
