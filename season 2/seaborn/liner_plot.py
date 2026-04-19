import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.lineplot(data = data ,x = "size", y = "tip")
plt.title("Avg tip reltive to the number of the people")
plt.show()