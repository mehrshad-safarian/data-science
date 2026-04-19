import matplotlib.pyplot as plt 
import seaborn as sns
data = sns.load_dataset("tips")
sns.barplot(data = data ,x = 'day' ,y = 'total_bill')
plt.title("Avg bill on diffrent days")
plt.show()
