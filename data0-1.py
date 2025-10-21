# تعریف متغیر
import pandas as pd
import numpy as np

# خواندن اطلاعات
df = pd.read_csv('C:/00/game_details.csv')
print('read OK!!!')

# نمایش اطلاعات اولیه 
print(df.head())

# نمایش داده های آخر دیتا فریم
print(df.tail())

# ارائه اطلاعات جامع درباره دیتافریم، از جمله تعداد ردیف‌ها، نوع داده‌ها و …
df.info()

# ارائه آماره‌های توصیفی برای ستون‌های عددی دیتافریم.
print(df.describe())

# تعداد سطر و ستون
print("تعداد سطر و ستون:", df.shape)

# تعداد فیلد و اسامی آنها
print("اسامی فیلدها:", df.columns)

# سطرهایی که دستگاه آنها ps3 است
print(df[df['platform'] == 'PS3'])

# سطرهایی که امتیاز آنها بیشتر از 80 است
print(df[df['metacritic_score'] > 80])

# میانگین
avg_score = df['metacritic_score'].mean()
print('Average of metacritic is :', avg_score)

# واریانس
variance_meta = df['metacritic_score'].var()
print("واریانس :", variance_meta)
