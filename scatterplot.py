#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv', index_col=0)

sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False,
           hue='Type 1')
sns.despine()
plt.show()
