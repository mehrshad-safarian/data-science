import pandas as pd
df = pd.DataFrame({
    'color' : ['red', 'green', 'blue', 'red'],
    'size' : ['small', 'medium', 'large', 'medium']
})
print(df)
size_order = {'small' : 0, 'medium' : 1, 'large' : 2}
df['size_order'] = df['size'].map(size_order)
print(df)