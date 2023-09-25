# import uniform distribution
import matplotlib.pyplot as plt
# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image
# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(5,5)})
from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(size=10000, loc=0, scale=1)
ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.show()  # Show the plot
