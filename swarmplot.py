#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#read file
df = pd.read_csv('pokemon.csv', index_col=0)

#define color palette
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

sns.set(style="whitegrid")

#create swarmplot of Attack damage sorted by Type
sns.swarmplot(x='Type 1', y='Attack', data=df, 
              palette=pkmn_type_colors)

#show output in window
plt.show()
