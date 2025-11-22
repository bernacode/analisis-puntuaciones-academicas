import sys
import os
import pandas as pd
import matplotlib.pyplot as pls
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import src.graficos as graficos

colors_test = ["red", "green", "blue"]

N = 100 

df_test = pd.DataFrame({

    "Normal": np.random.normal(loc=10, scale=2, size=N),
    "Uniforme": np.random.uniform(low=0, high=10, size=N),
    "LogNormal": np.exp(np.random.normal(loc=0.5, scale=0.5, size=N)),
    "Exponencial": np.random.exponential(scale=3, size=N) 

})

graficos.multiple_density_graph(df_test, colors_test)