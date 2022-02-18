import matplotlib.pyplot as plt
from general_functions import convert_list_elements_to_float, convert_list_elements_to_date_instance, save_figure
from options import *




options_for_plot_limit = {
    "totalRevenue": option_abs_50_to_30_billion,
    "grossProfit": option_gross_profit,
    "operatingIncome": option_operating_income,
    "incomeBeforeTax": option_abs_50_to_30_billion,
    "ebit": option_abs_50_to_30_billion,
    "netIncome": option_abs_50_to_30_billion,
    "eps": option_eps,
    "cashRatio": option_ratio_50_to_0,
    "currentRatio": option_ratio_50_to_0,
    "totalCurrentLiabilities_to_totalCurrentAssets": option_ratio_50_to_0,
    "researchAndDevelopment_to_totalRevenue": option_ratio_50_to_0,
    "ebitPerShare": option_per_share_30_to_minus_5,
    "netMargin": option_per_share_30_to_minus_5,
    "grossMargin": option_quotient_100_to_0,
    "totalDebtToEquity": option_quotient_2_to_0,
    "totalLiabilities_to_totalAssets": option_quotient_2_to_0,
    "totalRevenue_to_marketCap": option_quotient_100_to_0,
    "totalAssets_to_marketCap": option_quotient_100_to_0,
    "netIncome_to_totalRevenue": option_quotient_100_to_0,  # ROS
    "grossProfit_to_totalRevenue": option_quotient_100_to_0,
    "operatingIncome_to_totalRevenue": option_quotient_100_to_0,
    "operatingMargin": option_quotient_100_to_0,
    "totalShareholdersEquity_to_totalAssets": option_quotient_100_to_0,
}

options_for_plot_color = {
    "totalRevenue": option_color_total_revenue,
    # netSales
    # -costofgoods
    "grossProfit": option_color_gross_profit,
    # -operating expenses
    "operatingIncome": option_color_operating_income,
    "incomeBeforeTax": option_color_income_before_tax,
    # -interest expenes
    "ebit": option_color_ebit,
    # -taxes
    "netIncome": option_color_net_income,
    "eps": option_color_eps,
    "cashRatio": option_color_cash_ratio,
    "currentRatio": option_color_current_ratio,
    "totalCurrentLiabilities_to_totalCurrentAssets": option_color_current_ratio,
    "ebitPerShare": option_color_ebit_per_share,
    "grossMargin": option_color_gross_margin,
    "netMargin": option_color_net_margin,
    "totalDebtToEquity": option_color_totalDebtToEquity,
    "researchAndDevelopment_to_totalRevenue": option_color_quotient_research_and_development_revenue,
    "totalLiabilities_to_totalAssets": option_color_quotient_totalLiabilities_to_totalAssets,
    "totalRevenue_to_marketCap": option_color_quotient_totalRevenue_to_marketCap,
    "totalAssets_to_marketCap": option_color_quotient_totalAssets_to_marketCap,
    "netIncome_to_totalRevenue": option_color_quotient_netIncome_to_totalRevenue,
    "grossProfit_to_totalRevenue": option_color_gross_margin,
    "operatingIncome_to_totalRevenue": option_color_quotient_operationsIncome_to_totalRevenue,
    "operatingMargin": option_color_quotient_operationsIncome_to_totalRevenue,
    "totalShareholdersEquity_to_totalAssets": option_color_quotient_totalShareholdersEquity_to_totalAssets,
}


def transform_indicator(indicator: str):
    if indicator == "grossProfit_to_totalRevenue":
        indicator = "grossMargin"

    if indicator == "operatingIncome_to_totalRevenue":
        indicator = "operatingMargin"
    return indicator


def stupid_plot_data_lists(data_list: list, source: str) -> None:
    # x: list, y: list, symbol: str, indicator: str

    # data_per_symbol = [[[x_1],[y_1],symbol_1,indicator_1],...,[x_i],[y_i],symbol_i,indicator_i]]
    plt.figure()

    for i in data_list:

        x = i[0]
        y = i[1]
        y = convert_list_elements_to_float(y)
        symbol = i[2]
        indicator = i[3]

        indicator = transform_indicator(indicator)

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
    plt.title('{} source: {}'.format(symbol, source))
    plt.xlabel('Year')

    # mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle()
    plt.legend()

    save_figure(indicator)
    plt.cla()
    print("plt.show is commented, this is why the plot will not show up")
    plt.show()


def plot_compare_symbols_one_indicator(data_list, source):
    # show grid
    indicator = data_list[0][3]

    for i in data_list:
        x = i[0]
        x = convert_list_elements_to_date_instance(x)
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

            plt.plot(x, y, label=symbol)
            plt.scatter(x, y)

        else:
            print("ERROR - Length of x is {} and length of y is {} - must be same".format(len(x), len(y)))

    plt.grid(b=None, which='major', axis='both')
    plt.xticks(data_list[0][0], rotation="vertical")
    plt.title('{} source: {}'.format(indicator, source))
    plt.xlabel('Year')

    # mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle()

    plt.legend()
    save_figure(indicator)


    print("plt.show is commented, this is why the plot will not show up")
    plt.show()
    plt.cla()

