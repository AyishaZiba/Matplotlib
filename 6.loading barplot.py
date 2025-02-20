#Loading dataset as bar plot

import seaborn as sns
import matplotlib.pyplot as plt

#Loading dataset
data = sns.load_dataset("iris")

sns.barplot(x="species", y="sepal_length", data=data)
plt.title("ABC")
plt.show()
