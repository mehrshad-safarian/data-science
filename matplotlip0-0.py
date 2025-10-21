import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.show()

plt.plot(x, y)
plt.title("monthly sale candle") # نمودار رشد فروش
plt.xlabel("month") #ماه
plt.ylabel("unit sold") # تعداد فروش 
plt.show()

# تغییر رنگ، نوع خط و نشانه‌ها :
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.show()


# رسم چند نمودار در یک شکل
y2 = [5, 15, 20, 25, 35]

plt.plot(x, y, label = "year : 1401")
plt.plot(x, y2, label = "year : 1402")
plt.legend()
plt.show()


# نمودار میله‌ای
cities = ['Tehran', 'Shiraz', 'Khuzestan', 'Kermanshah']
values = [30, 25, 20, 15]

plt.bar(cities, values, color='orange')
plt.title("sales in diffrent cities ")  # میزان فروش در شهرهای مختلف
plt.show()


# نمودار دایره‌ای
labels = ['item A', 'item B', 'item C']
sizes = [50, 30, 20]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('shares of items sold')  # سهم اقلام فروخته شده
plt.show()
