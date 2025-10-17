import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

# خواندن فایل
df = pd.read_csv('C:/00/game_details.csv')
print('read ok!!!')
print(df.head())

# فقط از df استفاده کن
left = df['platform']   
height = df['metacritic_score'] 
tick_label = df['platform']

# رسم نمودار ستونی
plt.bar(left, height, tick_label=tick_label, width=0.8,
        color=['blue', 'green', 'red', 'yellow', 'black'])

plt.xlabel('platform')   
plt.ylabel('metacritic_score')   
plt.title('bar chart!')   
plt.show()
