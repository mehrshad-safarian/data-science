import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,25,30,40]
plt.plot(x,y)
plt.title("Monthly sale candle")
plt.xlabel("month")
plt.xlabel("unit sold")
# Changing color and the kind of the line and signs
plt.plot(x ,y ,color='red' ,linestyle  = '--', marker = 'o')
plt.show()