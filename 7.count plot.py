#Count Plot
#The count plot can be thought of
# as a histogram across a categorical variable.

import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
titanic = sns.load_dataset('titanic')
print(titanic)

#create plot
sns.countplot(x='class',hue='who',data=titanic ,palette='magma')
plt.title('Survivors')
plt.show()