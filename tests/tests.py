import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations


df = pd.DataFrame({
    "math score": [1,2,3,4,5,6,7,8,9,10],
    "reading score": [1,2,3,4,5,6,7,8,9,10],
    "writing score": [1,2,3,4,5,6,7,8,9,10],

})

columns = df.columns.to_list()
columns_combination = list(combinations(columns,2))
n_columns_combinations =  len(columns_combination )



fig, ax =  plt.subplots(1,n_columns_combinations,figsize=(5*n_columns_combinations,5))

for i, tupla in enumerate(columns_combination):

    print(i)


    value_x = df[tupla[0]].to_numpy()
    value_y = df[tupla[1]].to_numpy()

    xlabel = tupla[0]
    ylabel = tupla[1]

    m, b = np.polyfit(value_x,value_y,1)

    ax[i].set_title(f"{xlabel} vs {ylabel}")
    ax[i].set_xlabel(f"{xlabel}")
    ax[i].set_ylabel(f"{ylabel}")
    ax[i].scatter(value_x,value_y)
    ax[i].legend()
    ax[i].plot(value_x, m * value_x + b, color='black', linestyle="-",label="Tendencia")


plt.tight_layout()
plt.show()