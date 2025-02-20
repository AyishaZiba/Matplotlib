#Regplot (regression plot)
#Regplot is one of the functions in Seaborn
#that are used to visualize  the linear relationship as
#determined through regression

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
ax = sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()