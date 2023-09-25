# import uniform distribution
import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(5,5)})
from scipy.stats import uniform

# random numbers from uniform distribution
n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc=start, scale=width)

ax = sns.distplot(data_uniform, bins=100, kde=True, color='skyblue', hist_kws={"linewidth": 15, 'alpha': 1})
ax.set_xlabel('Uniform Distribution')  # Set the x-axis label
ax.set_ylabel('Frequency')            # Set the y-axis label

plt.show()  # Show the plot
