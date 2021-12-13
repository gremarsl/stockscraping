import matplotlib.pyplot as plt
from general_functions import convert_list_elements_to_float
from options import *

options_for_plot_limit = {
    "totalRevenue":option_abs_50_to_30_billion,
    "grossProfit": option_gross_profit,
    "operatingIncome": option_operating_income,
    "incomeBeforeTax": option_abs_50_to_30_billion,
    "ebit": option_abs_50_to_30_billion,
    "netIncome": option_abs_50_to_30_billion,
    "eps": option_eps,
    "cashRatio": option_ratio_50_to_0,
    "currentRatio": option_ratio_50_to_0,
    "researchAndDevelopment_to_totalRevenue":option_ratio_50_to_0,
    "ebitPerShare": option_per_share_30_to_minus_5,
    "netMargin": option_per_share_30_to_minus_5,
    "grossMargin": option_gross_margin,
    "totalDebtToEquity": option_quotient_2_to_0,
    "totalLiabilities_to_totalAssets": option_quotient_2_to_0,
    "totalRevenue_to_marketCap": option_quotient_100_to_0,
    "totalAssets_to_marketCap": option_quotient_100_to_0,
    "netIncome_to_totalRevenue":option_quotient_100_to_0, #ROS
}


options_for_plot_color = {
    "totalRevenue": option_color_total_revenue,
    #netSales
    #-costofgoods
    "grossProfit": option_color_gross_profit,
    #-operating expenses
    "operatingIncome": option_color_operating_income,
    "incomeBeforeTax": option_color_income_before_tax,
    #-interest expenes
    "ebit": option_color_ebit,
    #-taxes
    "netIncome": option_color_net_income,
    "eps": option_color_eps,
    "cashRatio": option_color_cash_ratio,
    "currentRatio": option_color_current_ratio,
    "ebitPerShare": option_color_ebit_per_share,
    "grossMargin": option_color_gross_margin,
    "netMargin": option_color_net_margin,
    "totalDebtToEquity": option_color_totalDebtToEquity,
    "researchAndDevelopment_to_totalRevenue":option_color_quotient_research_and_development_revenue,
    "totalLiabilities_to_totalAssets": option_color_quotient_totalLiabilities_to_totalAssets,
    "totalRevenue_to_marketCap": option_color_quotient_totalRevenue_to_marketCap,
    "totalAssets_to_marketCap": option_color_quotient_totalAssets_to_marketCap,
    "netIncome_to_totalRevenue":option_color_quotient_netIncome_to_totalRevenue
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