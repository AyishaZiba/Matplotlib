#Setting the title using Matplotlib

import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df = sns.load_dataset("iris")
print(df)

#draw lineplot
sns.lineplot(x = "sepal_length", y="sepal_width",data=df)

#setting the title using Matplotlib
plt.title('Title using Matplotlib Function')

plt.show()