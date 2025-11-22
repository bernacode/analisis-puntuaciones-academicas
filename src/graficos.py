import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import scipy as stats


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
