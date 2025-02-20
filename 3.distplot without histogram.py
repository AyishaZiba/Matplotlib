#Plotting a Distplot Without the Histogram

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot([0,1,2,3,4,5], hist=False) #(kde=False ) to disable the curve line (kde) , only hist will come
plt.show()

