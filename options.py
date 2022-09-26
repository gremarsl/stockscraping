def option_ratio_50_to_0():
    y_lim_top = 50
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_quotient_2_to_0():
    y_lim_top = 2
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_quotient_100_to_0():
    y_lim_top = 100
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_eps():
    y_lim_top = 20
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_per_share_30_to_minus_5():
    y_lim_top = 30
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_gross_margin():
    y_lim_top = 70
    y_lim_bottom = -5
    return y_lim_top, y_lim_bottom


def option_gross_profit():
    y_lim_top = 100 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_abs_50_to_30_billion():
    y_lim_top = 50 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_operating_income():
    y_lim_top = 50 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_color_eps():
    return "b"


def option_color_ebit_per_share():
    return "g"


def option_color_net_margin():
    return "blue"


def option_color_current_ratio():
    return "darkred"


def option_color_cash_ratio():
    return "red"


def option_color_totalDebtToEquity():
    return "purple"


def option_color_gross_profit():
    return "dimgray"


def option_color_ebit():
    return "yellow"


def option_color_net_income():
    return "darkgreen"


def option_color_income_before_tax():
    return "red"


def option_color_operating_income():
    return "purple"


def option_color_total_revenue():
    return "orange"


def option_color_operatingCashflow():
    return "darkred"


def option_color_changeInCashAndCashEquivalents():
    return "tomato"


def option_color_quotient_research_and_development_revenue():
    return "blue"


def option_color_quotient_netIncome_to_totalRevenue():
    return "orange"


def option_color_quotient_totalLiabilities_to_totalAssets():
    return "springgreen"


def option_color_gross_margin():
    return "red"


def option_color_quotient_operationsIncome_to_totalRevenue():
    return "green"


def option_color_quotient_totalShareholdersEquity_to_totalAssets():
    return "black"


## live data
def option_color_quotient_marketCap_to_totalRevenue():
    return "b"


def option_color_quotient_marketCap_to_netIncome():
    return "g"


def option_color_quotient_marketCap_to_totalAssets():
    return "g"


options_abs_indicator = [
    # yahoo:
    "GrossMargin",
    "NetMargin",
    "GrossProfit",
    "Ebit",
    "NetIncome",
    "IncomeBeforeTax",
    "OperatingIncome",
    "TotalRevenue",
    "operatingCashflow",
    "changeInCashAndCashEquivalents",
    "TotalAssets"
]

options_per_share_indicator = [
    "eps",
    "ebitPerShare"
]

options_rel_indicator = [
    # yahoo:
    "marketCap_to_NetIncome",
    "marketCap_to_TotalRevenue",
    "ResearchDevelopment_to_TotalRevenue",
    "TotalLiab_to_TotalAssets",
    "marketCap_to_TotalAssets",
    "NetIncome_to_totalRevenue",
    "TotalCurrentLiab_to_TotalCurrentAssets",
    "GrossProfit_to_TotalRevenue",
    "OperatingIncome_to_TotalRevenue",
    "TotalShareholdersEquity_to_TotalAssets",
]

options_for_plot_limit = {
    # yahoo:
    "TotalRevenue": option_abs_50_to_30_billion,
    "GrossProfit": option_gross_profit,
    "OperatingIncome": option_operating_income,
    "IncomeBeforeTax": option_abs_50_to_30_billion,
    "Ebit": option_abs_50_to_30_billion,
    "OperatingCashflow": option_abs_50_to_30_billion,
    "NetIncome": option_abs_50_to_30_billion,
    "TotalCurrentLiab_to_TotalCurrentAssets": option_ratio_50_to_0,
    "ResearchDevelopment_to_TotalRevenue": option_ratio_50_to_0,
    "TotalLiab_to_TotalAssets": option_quotient_2_to_0,
    "marketCap_to_TotalRevenue": option_quotient_100_to_0,
    "marketCap_to_NetIncome": option_quotient_100_to_0,
    "marketCap_to_TotalAssets": option_quotient_100_to_0,
    "netIncome_to_TotalRevenue": option_quotient_100_to_0,  # ROS
    "grossProfit_to_TotalRevenue": option_quotient_100_to_0,
    "operatingIncome_to_TotalRevenue": option_quotient_100_to_0,
    "TotalAssets": option_abs_50_to_30_billion,

}

# TODO color Total assets
options_for_plot_color = {
    # yahoo
    "TotalRevenue": option_color_total_revenue,
    "TotalAssets": option_color_total_revenue,
    # netSales
    # -costofgoods
    "GrossProfit": option_color_gross_profit,
    # -operating expenses
    "OperatingIncome": option_color_operating_income,
    "IncomeBeforeTax": option_color_income_before_tax,
    # -interest expenes
    "Ebit": option_color_ebit,
    "changeInCash": option_color_changeInCashAndCashEquivalents,
    # -taxes
    "NetIncome": option_color_net_income,
    "TotalCurrentLiab_to_TotalCurrentAssets": option_color_current_ratio,
    "ResearchDevelopment_to_totalRevenue": option_color_quotient_research_and_development_revenue,
    "TotalLiab_to_TotalAssets": option_color_quotient_totalLiabilities_to_totalAssets,
    "marketCap_to_NetIncome": option_color_quotient_marketCap_to_netIncome,
    "marketCap_to_TotalRevenue": option_color_quotient_marketCap_to_totalRevenue,
    "marketCap_to_TotalAssets": option_color_quotient_marketCap_to_totalAssets,
    "NetIncome_to_TotalRevenue": option_color_quotient_netIncome_to_totalRevenue,
    "GrossProfit_to_TotalRevenue": option_color_gross_margin,
    "OperatingIncome_to_TotalRevenue": option_color_quotient_operationsIncome_to_totalRevenue,
}
