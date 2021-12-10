import matplotlib.pyplot as plt
from general_functions import reverse_lists, convert_list_elements_to_float
from options import *

options_for_plot_limit = {
    "totalDebtToEquity": option_total_debt_to_equity,
    "eps": option_eps,
    "cashRatio": option_cash_ratio,
    "currentRatio": option_current_ratio,
    "ebitPerShare": option_ebit_per_share,
    "grossMargin": option_gross_margin,
    "netMargin": option_net_margin,
    "grossProfit": option_gross_profit,
    "ebit": option_ebit,
    "netIncome": option_net_income,
    "incomeBeforeTax": option_income_before_tax,
    "operatingIncome": option_operating_income,
    "totalRevenue":option_total_revenue,
    "resarch&dev/totalRevenue":option_quotient_research_and_development_revenue
}

options_for_plot_color = {
    "totalDebtToEquity": option_color_totalDebtToEquity,
    "eps": option_color_eps,
    "cashRatio": option_color_cash_ratio,
    "currentRatio": option_color_current_ratio,
    "ebitPerShare": option_color_ebit_per_share,
    "grossMargin": option_color_gross_margin,
    "netMargin": option_color_net_margin,
    "grossProfit": option_color_gross_profit,
    "ebit": option_color_ebit,
    "netIncome": option_color_net_income,
    "incomeBeforeTax": option_color_income_before_tax,
    "operatingIncome": option_color_operating_income,
    "totalRevenue": option_color_operating_income,
    "resarch&dev/totalRevenue":option_color_quotient_research_and_development_revenue
}


def stupid_plot_data_lists(data_list: list, data_is_from_platform: str) -> None:
    # x: list, y: list, symbol: str, indicator: str

    # data_per_symbol = [[[x_1],[y_1],symbol_1,indicator_1],...,[x_i],[y_i],symbol_i,indicator_i]]

    plt.figure()

    for i in data_list:

        x = i[0]
        y = i[1]
        y = convert_list_elements_to_float(y)
        symbol = i[2]
        indicator = i[3]

        if len(x) == len(y):
            if len(data_list) > 6:
                y_lim_top = 200
                y_lim_bottom = 0
            else:
                y_lim_top, y_lim_bottom = options_for_plot_limit[indicator]()

            '''
            # plt.ylim(top=y_lim_top)  # ymax is your value
            # plt.ylim(bottom=y_lim_bottom)  # ymin is your value
           
            if data_is_from_platform == "alpha_vantage":
                y = list(map(lambda i: i / 1000000000, y))
                plt.ylabel("[[Mrd]]")
            '''
            plt.plot(x, y, label=indicator, color=options_for_plot_color[indicator]())
            plt.scatter(x, y, color=options_for_plot_color[indicator]())

        else:
            print("ERROR - Length of x is {} and length of y is {} - must be same".format(len(x), len(y)))

    # show grid
    plt.grid(b=None, which='major', axis='both')
    plt.xticks(data_list[0][0], rotation="vertical")
    plt.title('{}: '.format(symbol))
    plt.xlabel('Year')
    plt.legend()
    plt.show()


def stupid_plot_data_list(data_list: list, data_is_from_platform: str) -> None:
    # x: list, y: list, symbol: str, indicator: str

    # data_list = [[x],[y],symbol,indicator]]
    x = data_list[0]
    y = data_list[1]
    y = convert_list_elements_to_float(y)

    symbol = data_list[2]
    indicator = data_list[3]

    plt.figure()

    if len(x) == len(y):
        if len(data_list) > 6:
            y_lim_top = 200
            y_lim_bottom = 0
        else:
            y_lim_top, y_lim_bottom = options_for_plot_limit[indicator]()
            # recompute the ax.dataLim
            # update ax.viewLim using the new dataLim

        # plt.ylim(top=y_lim_top)  # ymax is your value
        # plt.ylim(bottom=y_lim_bottom)  # ymin is your value

        '''
        if data_is_from_platform == "alpha_vantage":
            y = list(map(lambda i: i / 1000000000, y))
            plt.ylabel("[[Mrd]]")
        '''

        plt.plot(x, y, label=indicator, color=options_for_plot_color[indicator]())
        plt.scatter(x, y, color=options_for_plot_color[indicator]())

    else:
        print("ERROR - Length of x is {} and length of y is {} - must be same".format(len(x), len(y)))

    # show grid
    plt.grid(b=None, which='major', axis='both')
    plt.xticks(x, rotation="vertical")

    plt.title('{}: '.format(symbol))
    plt.xlabel('Year')
    plt.legend()
    plt.show()
