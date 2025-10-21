# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt   

# # خواندن فایل
# df = pd.read_csv('C:/00/game_details.csv')
# print('read ok!!!')
# print(df.head())

# # فقط از df استفاده کن
# left = df['platform']   
# height = df['metacritic_score'] 
# tick_label = df['platform']

# # رسم نمودار ستونی
# plt.bar(left, height, tick_label=tick_label, width=0.8,
#         color=['blue', 'green', 'red', 'yellow', 'black'])

# plt.xlabel('platform')   
# plt.ylabel('metacritic_score')   
# plt.title('bar chart!')   
# plt.show()



# تعریف متغیر
import pandas as pd
import numpy as np

# خواندن اطلاعات
df = pd.read_csv('C:/00/game_details.csv')
print('read OK!!!')

# نمایش اطلاعات اولیه 
df.head()

# نمایش داده های آخر دیتا فریم
df.tail()

# ارائه اطلاعات جامع درباره دیتافریم، از جمله تعداد ردیف‌ها، نوع داده‌ها و …
df.info()

# ارائه آماره‌های توصیفی برای ستون‌های عددی دیتافریم.
df.describe()

# تعداد سطر و ستون
df.shape

# تعداد فیلد و اسامی آنها
df.columns

# سطرهایی که دستگاه آنها ps3 است
df[df['platform'] == 'PS3']

# سطرهایی که امتیاز آنها بیشتر از 80 است
df[df['metacritic_score'] > 80]

# میانگین
avg_score = df['metacritic_score'].mean()
print('Average of metacritic is : ', avg_score)

# واریانس
variance_meta = df['metacritic_score'].var()
print("واریانس : ", variance_meta)
