options_abs_indicator = [
    "grossMargin",
    "netMargin",
    "grossProfit",
    "ebit",
    "netIncome",
    "incomeBeforeTax",
    "operatingIncome",
    "totalRevenue"
]

options_per_share_indicator = [
    "eps",
    "ebitPerShare"
]

options_rel_indicator = [
    "totalRevenue_to_marketCap",
    "totalDebtToEquity",
    "cashRatio",
    "currentRatio",
    "researchAndDevelopment_to_totalRevenue",
    "totalLiabilities_to_totalAssets",
    "totalAssets_to_marketCap",
    "netIncome_to_totalRevenue",
    "totalCurrentLiabilities_to_totalCurrentAssets",
    "grossProfit_to_totalRevenue",
    "operatingIncome_to_totalRevenue",
    "totalShareholdersEquity_to_totalAssets"

]


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


def option_color_gross_margin():
    return "navy"


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


def option_color_quotient_research_and_development_revenue():
    return "blue"


def option_color_quotient_netIncome_to_totalRevenue():
    return "orange"


def option_color_quotient_totalLiabilities_to_totalAssets():
    return "springgreen"


def option_color_quotient_grossProfit_to_totalRevenue():
    return "red"


def option_color_quotient_operationsIncome_to_totalRevenue():
    return "green"


def option_color_quotient_totalShareholdersEquity_to_totalAssets():
    return "black"

## live data
def option_color_quotient_totalRevenue_to_marketCap():
    return "b"


def option_color_quotient_totalAssets_to_marketCap():
    return "g"
