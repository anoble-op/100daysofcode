#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

df = pd.read_csv('worldcupmatches.csv')

sb.lmplot(x = 'Home Team Goals', y = 'Away Team Goals', data = df,
          fit_reg = False,)

sb.despine()

plt.show()
