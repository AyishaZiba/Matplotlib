#Seaborn
import matplotlib.pyplot as plt
#Seaborn is a library that uses Matplotlib
# underneath to plot graphs.
# It will be used to visualize random distributions.

#Histogram
#Histograms represent the data distribution by forming bins
# along with the range of the data and then drawing bars to show
# the number of observations that fall in each bin.
# In Seaborn we use distplot() function to plot histograms.

#Plotting a Distplot  #(distribution plot)

import seaborn as sns
sns.distplot([0,1,2,3,4,5])
plt.show()

