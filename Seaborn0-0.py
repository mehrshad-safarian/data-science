# داده‌های نمونه در Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data.head())

# رسم نمودار پراکندگی (Scatter Plot)
sns.scatterplot(data=data, x="total_bill", y="tip")
plt.title("The relationship between the total amount and the tip amount") # رابطه بین مبلغ کل و مبلغ انعام
plt.show()

# نمودار خطی (Line Plot)
sns.lineplot(data=data, x="size", y="tip")
plt.title("Average tip relative to the number of people") # میانگین انعام نسبت به تعداد افراد
plt.show()

# نمودار میله‌ای (Bar Plot)
sns.barplot(data=data, x="day", y="total_bill")
plt.title("Average bill on different days") # میانگین صورت‌حساب در روزهای مختلف
plt.show()

# نمودار جعبه‌ای (Box Plot)
sns.boxplot(data=data, x="day", y="total_bill")
plt.title("Distribution of total amount on different days") #پراکندگی مبلغ کل در روزهای مختلف
plt.show()

# تنظیم رنگ‌ها و استایل‌ها
sns.set_style("darkgrid")
sns.barplot(data=data, x="sex", y="tip", palette="coolwarm")
plt.title("Comparison of average tip based on gender") # مقایسه میانگین انعام بر اساس جنسیت
plt.show()

