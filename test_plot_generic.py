import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# TODO units - multiply with 1000
# TODO check if all data has the same data length

'''
Pipeline / Procedure: From data to plot
'''

symbol = "GOOGL"

# Get data - e.g. .csv
file = "D:\\Desktop\\GOOGL\\balanceAnnual_total.csv"

# Transform data to a panda dataframe;
df = pd.read_csv(file, sep=';', decimal=",")

# reverse the rows - so that latest quarter is last element in the list
df = df[::-1]

# Plot Types
plot_list = [
    # PLOT 1
    ["TotalRevenue", "CostOfRevenue", "GrossProfit", "GrossMargin"],
    # PLOT 2
    ["OperatingExpenses", "OperatingIncome", "OperatingMargin"],  # ,"NetIncome"
    # PLOT 3
    ["CurrentAssets", "CashAndEquivalents", "CurrentLiabilities", "CashRatio", "CurrentRatio"],
    # PLOT 4
    ["TotalAssets", "StockholdersEquity", "TotalLiabilities", "EquityRatio"],
    # PLOT 5
    ["StockholdersEquity", "Goodwill", "IntangibleAssets", "GoodwillRatio"],
    # PLOT 6
    ["OperatingExpenses", "SellingGeneralAdministrative", "ResearchAndDevelopment"],
    # PLOT 7
    ["TotalOtherExpenses", "TaxProvision", "NetInterestExpenses"] , # TaxRate
    # PLOT 8
    ["OperatingCashflow", "CapitalExpenditures", "FreeCashflow"]  # "FCFRatio","OCFRatio"

]

color_list = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]

plot_type = 3

relative_indicator = ["GrossMargin", "OperatingMargin", "CashRatio", "CurrentRatio", "EquityRatio", "GoodwillRatio",
                      "ResearchRatio", "InterestRatio", "TaxRate","FCFratio","OCFRatio"]


def plot(plot_idx):
    # Create Figure Object
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Get Time Scale
    x = df["index"]

    ind = np.arange(len(x))

    # Bar Plotting
    w = 0
    width = 0.15

    for i, item in enumerate(plot_list[plot_idx]):
        ax1.set_xticklabels(x)

        if item in relative_indicator:
            ax2.plot(ind + w, df[item], label=item, color=color_list[i])
            ax2.scatter(ind + w, df[item], color=color_list[i])
            # annotate the values
            for i,j in zip(ind + w, df[item]):
                ax2.annotate(str(round(j,2)), xy=(i, j))

            y_lim = max(df[item])
            if y_lim > 1:
                ax2.set_ylim([0, y_lim])
            else:
                ax2.set_ylim([0, 1])

        else:
            #series = df[item]
            # TODO annotate the values
            #change = series.pct_change(periods=1)
            #array = change.to_numpy()
            #print(array)
            # annotate the values

            ax1.bar(ind + w, df[item], width=0.15, label=item, color=color_list[i])

            w += width

    # show grid
    ax1.grid(visible=None, which='major', axis='both')
    plt.xticks(ind + width / 2, rotation="vertical")

    plt.title(f'GOOGL Data')

    ax1.set_ylabel('USD')
    ax2.set_ylabel('Ratio')
    # plot_full_screen()

    ax1.legend(loc='center left', bbox_to_anchor=(0, 0.5))
    ax2.legend(loc='center right', bbox_to_anchor=(1, 0.5))
    plt.show()


for idx in range(0, len(plot_list)):
    plot(idx)
