import sys
import os
import pandas as pd
import matplotlib.pyplot as pls
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import src.graficos as graficos


x = np.random.normal(loc=50, scale=10, size=50)
y_pos = x * 0.8 + np.random.normal(loc=0, scale=5, size=50)
y_neg = 100 - x + np.random.normal(loc=0, scale=5, size=50)
y_ind = np.random.normal(loc=50, scale=10, size=50)

df = pd.DataFrame({
    'x': x,
    'y_pos': y_pos,
    'y_neg': y_neg,
    'y_ind': y_ind
})

