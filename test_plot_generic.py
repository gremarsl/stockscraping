import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import global_vars

# TODO units - multiply with 1000

'''
Pipeline / Procedure: From data to plot
'''

symbol = "GOOGL"

# Get data - e.g. .csv
file = "D:\\Desktop\\GOOGL\\balanceAnnual_total.csv"

# Transform data to a panda dataframe;
df = pd.read_csv(file, sep=';', decimal=",")
print(df.columns)

# check if all data has the same data length

# Plot Types
plot_list = [
    # PLOT 1
    ["TotalRevenue", "CostOfRevenue", "GrossProfit"],  # GrossProfit
    # PLOT 2
    ["OperatingExpenses", "OperatingIncome"]
]  # calc gross margin
color_list = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]

plot_type = 1

match plot_type:

    case 0:

        # Create Figure Object
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()

        # Get Time Scale
        x = df["index"]

        ind = np.arange(len(x))

        # Bar Plotting
        w = 0
        width = 0.15

        for i, item in enumerate(plot_list[plot_type]):
            ax1.set_xticklabels(x)
            print(x)
            print(item)
            ax1.bar(ind + w, df[item], width=0.15, label=item, color=color_list[i])
            w += width

        # show grid
        plt.grid(visible=None, which='major', axis='both')
        plt.xticks(ind + width / 2, rotation="vertical")

        plt.title(f'GOOGL Data')

        ax1.set_ylabel('USD')
        ax2.set_ylabel('Ratio')
        # plot_full_screen()

        ax1.legend(loc='center left', bbox_to_anchor=(0, 0.5))
        ax2.legend(loc='center right', bbox_to_anchor=(1, 0.5))
        plt.show()

    case 1:

        # Create Figure Object
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()

        # Get Time Scale
        x = df["index"]

        ind = np.arange(len(x))

        # Bar Plotting
        w = 0
        width = 0.15

        for i, item in enumerate(plot_list[plot_type]):
            ax1.set_xticklabels(x)
            print(x)
            print(item)
            ax1.bar(ind + w, df[item], width=0.15, label=item, color=color_list[i])
            w += width

        # show grid
        plt.grid(visible=None, which='major', axis='both')
        plt.xticks(ind + width / 2, rotation="vertical")

        plt.title(f'GOOGL Data')

        ax1.set_ylabel('USD')
        ax2.set_ylabel('Ratio')
        # plot_full_screen()

        ax1.legend(loc='center left', bbox_to_anchor=(0, 0.5))
        ax2.legend(loc='center right', bbox_to_anchor=(1, 0.5))
        plt.show()
