#Loading dataset -scatterplot

import seaborn as sns
import matplotlib.pyplot as plt

#Loading dataset
data = sns.load_dataset("iris")

sns.scatterplot(x="sepal_length", y="sepal_width", data=data)
plt.title("ABC")
plt.show()
