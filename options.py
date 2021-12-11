
options_test_indicator =[
    "totalRevenue",
    "netIncome"
]

options_abs_indicator =[
    "grossMargin",
    "netMargin",
    "grossProfit",
    "ebit",
    "netIncome",
    "incomeBeforeTax",
    "operatingIncome",
    "totalRevenue"
]

options_per_share_indicator =[
    "eps",
    "ebitPerShare"
]

options_rel_indicator =[
    "totalRevenue_to_marketCap",
    "totalDebtToEquity",
    "cashRatio",
    "currentRatio",
    "researchAndDevelopment_to_totalRevenue",
    "totalLiabilities_to_totalAssets"
]


def option_ratio_50_to_0():
    y_lim_top = 50
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_quotient_2_to_0():
    y_lim_top = 2
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_eps():
    y_lim_top = 20
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom



def option_ebit_per_share():
    y_lim_top = 30
    y_lim_bottom = 0
    return y_lim_top, y_lim_bottom


def option_gross_margin():
    y_lim_top = 70
    y_lim_bottom = -5
    return y_lim_top, y_lim_bottom


def option_net_margin():
    y_lim_top = 30
    y_lim_bottom = -5
    return y_lim_top, y_lim_bottom


def option_gross_profit():
    y_lim_top = 100 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_ebit():
    y_lim_top = 50 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_net_income():
    y_lim_top = 50 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_income_before_tax():
    y_lim_top = 50 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_operating_income():
    y_lim_top = 50 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_total_revenue():
    y_lim_top = 50 * 10 ** 9
    y_lim_bottom = 30 * 10 ** 9
    return y_lim_top, y_lim_bottom


def option_color_gross_margin():
    return "navy"


def option_color_net_margin():
    return "blue"


def option_color_eps():
    return "forestgreen"


def option_color_ebit_per_share():
    return "limegreen"


def option_color_cash_ratio():
    return "red"


def option_color_current_ratio():
    return "darkred"


def option_color_totalDebtToEquity():
    return "purple"


def option_color_gross_profit():
    return "black"


def option_color_ebit():
    return "yellow"


def option_color_net_income():
    return "orange"


def option_color_income_before_tax():
    return "red"


def option_color_operating_income():
    return "green"


def option_color_total_revenue():
    return "orange"


def option_color_quotient_research_and_development_revenue():
    return "blue"

def option_color_quotient_totalLiabilities_to_totalAssets():
    return "green"

def option_color_quotient_totalRevenue_to_marketCap():
    return "red"
