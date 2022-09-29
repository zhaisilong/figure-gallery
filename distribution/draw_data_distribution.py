import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('../data/distribution/Distribution_Data.csv')
plt.figure(figsize=(16, 12), dpi=300)
# sns.color_palette("Paired", 8)
# ax = sns.distplot(df['E_gap'], color='#144A74', label="Measured E_gap", norm_hist=True,
#              hist_kws=dict(linewidth=0),kde=False,
#              bins=50)
ax = sns.distplot(df['value'], kde=False)
# ax.set(ylabel='Count', xlabel='E_gap (eV)')
ticklabels=35
ax.set_xticks(np.arange(2, 5.5, 0.5))
ax.set_xticklabels(np.arange(2, 5.5, 0.5), fontsize=ticklabels)
ax.set_ylabel('Count', fontsize=45)
ax.set_xlabel('X', fontsize=45)
ax2 = plt.twinx()
ax2 = sns.distplot(df['value'], kde=True, hist=False, ax=ax2)
ax2.set_ylabel('Density', fontsize=45)
ax.set_yticklabels([0, 100, 200, 300, 400, 500, 600, 700], fontsize=ticklabels)
ax2.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1], fontsize=ticklabels)
# plt.legend(fontsize=28)
# plt.title("Distribution of PBDD energy gap", fontsize=45, pad=20)
# plt.tick_params(labelsize=30)
# plt.xlabel("E_gap (eV)", fontsize=30, labelpad=20)
# plt.ylabel("Distribution", fontsize=30, labelpad=25)
plt.savefig('out/Distribution.png', dpi=300)
plt.show()
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt
#
# # generate some random test data
# y = np.abs(np.random.normal(np.random.choice([5, 9, 15], 2000, p=[3/9, 5/9, 1/9]), 2, 2000))
#
# ax = sns.distplot(y, kde=False)
# ax.set_title('Distribution of Flavor Purchases\nNumber Purchased')
# ax.set(ylabel='Count', xlabel='Number of Flavors Purchased')
# n = 20
# ax.set_xticks(range(n))
# ax.set_xticklabels(range(n))
#
# ax2 = plt.twinx()
# ax2 = sns.distplot(y, kde=True, hist=False, ax=ax2)
# ax2.set_ylabel('density')
# plt.show()
