import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,25,30,40]
y2 = [15,25,20,35,-35]
plt.plot(x ,y ,label = "year : 2021")
plt.plot(x ,y2 ,label = "year : 2022")
plt.legend()
plt.show()