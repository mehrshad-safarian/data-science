import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.scatterplot(data = data, x="total_bill" ,y="tip")
plt.title("The rel between the amount and amount of the tip")
plt.show()