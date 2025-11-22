import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import scipy as stats
from itertools import combinations


def multiple_density_graph(df_values, colors):

    columns = df_values.columns.tolist()

    fig, ax = plt.subplots(1, len(columns), figsize=(15,5))

    for i, (col, color) in enumerate(zip(columns,colors)):
        df_values[col].plot.kde(
            bw_method=0.3,
            ax=ax[i],
            label= col,
            color=color,
            linestyle='-',
        )

        ax[i].set_title(f" Densidad de {col}")
        ax[i].set_xlabel("Valor")

        ax[i].set_xlim(df_values[col].min(), df_values[col].max())
        
        ax[i].grid(alpha=0.3)
        ax[i].legend()
    
    plt.tight_layout()
    plt.show()


def correlation_graph(x,y, c):

    fig, ax = plt.subplots(figsize=(15,5))

    x_name = x.name
    y_name = y.name

    values_x = x.to_numpy()
    values_y = y.to_numpy()

    ax.set_title(f"'{x_name}' vs '{y_name}'")
    
    ax.scatter(values_x,values_y, color = c, linestyle="-")

    ax.set_xlabel(f"{x_name}")
    ax.set_ylabel(f"{y_name}")



    ax.legend()


    plt.show()


def multiple_correlation_graph(df,c):

    columns = df.columns.to_list()
    columns_combination = list(combinations(columns,2))
    n_columns_combinations =  len(columns_combination )
    fig, ax =  plt.subplots(1,n_columns_combinations,figsize=(5*n_columns_combinations,5))


    for i, tupla in enumerate(columns_combination):

        value_x = df[tupla[0]].to_numpy()
        value_y = df[tupla[1]].to_numpy()

        xlabel = tupla[0]
        ylabel = tupla[1]

        m, b = np.polyfit(value_x,value_y,1)

        ax[i].set_title(f"{xlabel} vs {ylabel}")
        ax[i].set_xlabel(f"{xlabel}")
        ax[i].set_ylabel(f"{ylabel}")
        ax[i].scatter(value_x,value_y, color=c, label=tupla)
        ax[i].legend()
        ax[i].plot(value_x, m * value_x + b, color='black', linestyle="-",label="Tendencia")

plt.tight_layout()
plt.show()