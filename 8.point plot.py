#Point plot

#Point plot is used to show point
#estimtes and confidence intervals
#using scatter plot glyphs.

import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")
print(data)
sns.pointplot(x ="day", y="tip",data=data)
plt.show()