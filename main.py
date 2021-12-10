import os
import json

from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, get_fundamental_data_from_finnhub, \
    get_one_relative_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub
from plot_functions import stupid_plot_data_lists
from functions_for_alpha_vantage import \
    get_quaterly_report_alpha, \
    get_annual_report_alpha, \
    calling_alpha_vantage_api


# Understand JSON
# object: {}
# array : []

class NoData(Exception): pass  # declare a label


class NoEbitData(Exception):    pass


class NoNetMarginData(object):
    print("Known Except: No net margin data in fundamental Data for")
    pass


def filter_plot_data_list_per_symbol(data_list: list, relativeData: bool, data_is_from_platform: str):
    # hier:  all_data_list = [data_per_symbol_1]
    if relativeData and data_is_from_platform == "alpha_vantage":
        try:
            if len(data_list) == 0: raise NoData()

            try:
                indicators = list(filter(
                    lambda x: x[3] == "researchAndDevelopment_to_totalRevenue" or "totalLiabilities_to_totalAssets",
                    data_list))
                stupid_plot_data_lists(indicators, data_is_from_platform)
            except:
                print("no working indicators data")

        except NoData:
            print("no income data ")
            pass

    else:
        eps_ebit_per_share_plot_data = []
        if data_is_from_platform == "finnhub":
            except_grossmargin = list(filter(lambda x: (x[3] != "grossMargin"), data_list))

            except_grossmargin_debt = list(filter(lambda x: x[3] != "totalDebtToEquity", except_grossmargin))

            eps_ebit_per_share_plot_data = list(
                filter(lambda x: x[3] == "eps" or x[3] == "ebitPerShare", data_list))

            ratios_eps_ebit_net_margin_data = list(filter(
                lambda x: (x[3] == "eps" or x[3] == "cashRatio" or x[3] == "currentRatio" or x[3] != "ebitPerShare" or
                           x[3] == "netMargin"), data_list))

            stupid_plot_data_lists(eps_ebit_per_share_plot_data, data_is_from_platform)

            try:
                stupid_plot_data_lists(except_grossmargin_debt, data_is_from_platform)
            except:
                print("Not working to plot ratios_eps_ebit_net_margin_data data in one plot {}".format(data_list))

        if data_is_from_platform == "alpha_vantage":
            try:
                if len(data_list) == 0: raise NoData()

                try:
                    indicators = list(filter(
                        lambda x: x[
                                      3] == "grossProfit" or "totalRevenue" or "ebit" or "netIncome" or "operatingIncome" or "incomeBeforeTax",
                        data_list))
                    stupid_plot_data_lists(indicators, data_is_from_platform)
                except:
                    print("no working indicators data")

            except NoData:
                print("no income data ")
                pass

        try:
            if len(eps_ebit_per_share_plot_data) == 0: raise NoEbitData()
        except NoEbitData:
            print("no ebit data skip")
            pass


def get_data_from_file(filename):
    if os.path.isfile(filename):
        with open(filename) as json_file:
            income_statement = json.load(json_file)
    else:
        print(
            "WARNING: alpha vantage was called but you filese are not found. Is get_alpha_data False? This should not be reached if get_alpha_data is True. maybe options fehlt für plot")

    return income_statement


def get_data_calculate_quotient(data_origin, indicator, symbol):
    dividend_str = indicator.split('_to_')[0]
    divisor_str = indicator.split('_to_')[1]

    # quotient: research and development:
    list_dividend = get_quaterly_report_alpha(data_origin, dividend_str, symbol=symbol)
    list_divisor = get_quaterly_report_alpha(data_origin, divisor_str, symbol=symbol)

    # convert to int
    list_dividend_converted = [int(x) for x in list_dividend[1]]

    list_divisor_converted = [int(x) for x in list_divisor[1]]

    quotient_list = [(x / y) * 100 for x, y in zip(list_dividend_converted, list_divisor_converted)]

    data = [list_dividend[0], quotient_list, symbol, indicator]

    return data


def analyse_data_from_alpha_vantage(symbols: list):
    source = "alpha_vantage"
    print("------------------------")
    indicator_absolute_income_statement = ["grossProfit", "totalRevenue", "ebit", "netIncome", "incomeBeforeTax",
                                           "operatingIncome"]
    indicator_percentage_income_statement = ["researchAndDevelopment_to_totalRevenue"]

    indicator_percentage_balance_sheet = ["totalLiabilities_to_totalAssets"]
    test = ["grossProfit", "ebit"]

    for s in symbols:

        income_statement = get_data_from_file("income_statement_alpha_" + s + ".json")


        #TODO delete annaul
        annual_absolute_data_per_symbol = []
        quaterly_absolute_data_per_symbol = []
        quaterly_relative_data_per_symbol = []

        for i in indicator_absolute_income_statement:
            try:
                annual_absolute_data_per_symbol.append(get_annual_report_alpha(income_statement, i, symbol=s))
            except:
                print("error in annual data per symbol {}".format(s))

            try:
                quaterly_absolute_data_per_symbol.append(get_quaterly_report_alpha(income_statement, i, symbol=s))
            except:
                print("error in quaterly data {}".format(s))

    for s in symbols:

        for i in indicator_percentage_income_statement:
            # TODO erweitere mit request_cash_flow_from_alpha(s),request_earnings_from_alpha(s), request_overiew_from_alpha(s)

            try:
                quaterly_relative_data_per_symbol.append(
                    get_data_calculate_quotient(data_origin=income_statement, indicator=i, symbol=s))

            except:
                print(
                    "calculate quotient of {} didint work".format(i))

    for s in symbols:

        balance_sheet = get_data_from_file("balance_sheet_alpha_" + s + ".json")

        for i in indicator_percentage_balance_sheet:

            try:
                quaterly_relative_data_per_symbol.append(
                    get_data_calculate_quotient(data_origin=balance_sheet, indicator=i, symbol=s))

            except:
                print(
                    "calculate quotient of {} didint work".format(i))


        # filter_plot_data_list_per_symbol(annual_data_per_symbol, source)
        filter_plot_data_list_per_symbol(quaterly_absolute_data_per_symbol, False, source)
        filter_plot_data_list_per_symbol(quaterly_relative_data_per_symbol, True, source)

    pass


def get_data_from_finnhub():
    source = "finnhub"
    all_plot_data = []
    all_plot_data_test = []

    # TODO switch annual or quaterly
    period = 'annual'
    period = 'quarterly'

    symbol_dax_stocks = ["BAS.DE",
                         "SIE.DE",
                         "BAYN.DE",
                         "IFX.DE",
                         "1COV.DE",
                         "LIN.DE",
                         "BEI.DE",
                         "HEN3.DE",
                         ]
    # ALV.DE, "DBK.DE",

    automotive_dax_stocks = ["DAI.DE",
                             "BMW.DE",
                             "VOW.DE"]
    test_symbol = ["BAS.DE"]

    for s in automotive_dax_stocks:
        data_per_symbol = []
        print(s)

        fundamental_data_json = get_fundamental_data_from_finnhub(s)

        indicator_absolute_list = ["grossMargin"]  # netMargin
        indicators_per_share = ["eps", "ebitPerShare"]
        indicators_ratio = ["cashRatio", "currentRatio"]
        indicators_percentage = ["totalDebtToEquity"]

        for i in indicator_absolute_list:
            try:
                data_per_symbol.append(
                    get_one_absolute_indicator_from_finnhub(fundamental_data_json, period, i, s))
            except:
                print(" no {} data for {} ".format(i, s))
        for i in indicators_per_share:
            try:
                data = get_one_absolute_indicator_from_finnhub(fundamental_data_json, period, i, s)
                data_per_symbol.append(data)
            except:
                print("no {} data for {} ".format(i, s))
        for i in indicators_ratio:
            try:
                data_per_symbol.append(
                    get_one_ratio_indicator_from_finnhub(fundamental_data_json, period, i, s))
            except:
                print("no {} data  for  {} ".format(i, s))
        for i in indicators_percentage:
            try:
                data_per_symbol.append(
                    get_one_relative_indicator_from_finnhub(fundamental_data_json, period, i, s))
            except:
                print("no {} data  for  {} ".format(i, s))

        filter_plot_data_list_per_symbol(data_per_symbol, source)
        all_plot_data.append(data_per_symbol)


# SWITCHES:
analyse_finnhub_data = False
get_alpha_data = False
analyse_alpha_data = True
alpha_vantage_symbols = ["AVGO"]  # "IBM", "AAPL"

if __name__ == '__main__':

    if analyse_finnhub_data:
        get_data_from_finnhub()

    if get_alpha_data:
        calling_alpha_vantage_api(alpha_vantage_symbols)

    if analyse_alpha_data:
        analyse_data_from_alpha_vantage(alpha_vantage_symbols)
