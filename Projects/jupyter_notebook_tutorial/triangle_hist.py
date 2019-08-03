import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

if __name__ == '__main__':
    h = plt.hist(np.random.triangular(0, 5, 9, 1000), bins=100, linewidth=0)
    plt.show()