from typing import Dict, List
from requests import Response

from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, fundamental_data_from_finnhub, \
    get_one_relative_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub
from plot_functions import stupid_plot_data_lists, stupid_plot_data_list
from functions_for_alpha_vantage import \
    request_income_statement_from_alpha, \
    request_earnings_from_alpha, \
    request_cash_flow_from_alpha, \
    request_balance_sheet_from_alpha, \
    request_symbol_search_from_alpha, \
    request_overiew_from_alpha, \
    get_quaterly_report_alpha, \
    get_annual_report_alpha, \
    long_term_data_get_ebitda, \
    long_term_data_get_price_to_earning_ratio, calling_alpha_vantage_api

# Understand JSON
# object: {}
# array : []

class NoData(Exception): pass  # declare a label


class NoEbitData(Exception):    pass


class NoNetMarginData(object):
    print("Known Except: No net margin data in fundamental Data for")
    pass


def filter_plot_data_list_per_symbol(data_list: list, data_is_from_platform: str):
    # hier:  all_data_list = [data_per_symbol_1]


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
                                  3] == "grossProfit" or "ebit" or "netIncome" or "operatingIncome" or "incomeBeforeTax",
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


def get_data_from_alpha_vantage():
    source="alpha_vantage"


    test_symbol = "IBM"
    symbols = ["MSFT","IBM", "AAPL"]
    print("Income statement {}:".format(test_symbol))
    print("------------------------")

    indicator_absolute_income_statement = ["grossProfit", "ebit", "netIncome", "incomeBeforeTax", "operatingIncome"]

    test = ["grossProfit", "ebit"]

    for s in symbols:
        print(s)


        #TODO wenn ich sage jetzt hole dir die neuen, dann hole die neuen daten und überschreibe die alten Daten
        income_statement = request_income_statement_from_alpha(s)
        # balance_sheets = request_balance_sheet_from_alpha(s)
        # cash_flow = request_cash_flow_from_alpha(s)
        # earnings =request_earnings_from_alpha(s)
        overview = request_overiew_from_alpha(s)
        #long_term_data_get_ebitda(overview,s)
        #long_term_data_get_price_to_earning_ratio(overview,s)
        annual_data_per_symbol = []
        quaterly_data_per_symbol = []

        for i in indicator_absolute_income_statement:
            try:
                annual_data_per_symbol.append(get_annual_report_alpha(income_statement, i, symbol=s))
            except:
                print("error in annual data per symbol {}".format(s))

            try:
                quaterly_data_per_symbol.append(get_quaterly_report_alpha(income_statement, i, symbol=s))
            except:
                print("error in quaterly data {}".format(s))

        #filter_plot_data_list_per_symbol(annual_data_per_symbol, source)
        filter_plot_data_list_per_symbol(quaterly_data_per_symbol, source)

    pass


def get_data_from_finnhub():
    source="finnhub"
    all_plot_data = []
    all_plot_data_test = []

    symbol_dax_stocks = ["DAI.DE",
                         "BAS.DE",
                         "SIE.DE",
                         "BMW.DE",
                         "BAYN.DE",
                         "IFX.DE",
                         "1COV.DE",
                         "LIN.DE",
                         "BEI.DE",
                         "HEN3.DE",
                         "VOW3.DE"]
    # ALV.DE, "DBK.DE",

    test_symbol = ["BAS.DE"]

    for s in symbol_dax_stocks:
        data_per_symbol = []
        print(s)

        fundamental_data_json = fundamental_data_from_finnhub(s)

        indicators_per_share = ["eps", "ebitPerShare"]
        indicator_absolute_list = ["grossMargin"]  # netMargin
        indicators_ratio = ["cashRatio", "currentRatio"]
        indicators_percentage=["totalDebtToEquity"]

        for i in indicator_absolute_list:
            try:
                data_per_symbol.append(
                    get_one_absolute_indicator_from_finnhub(fundamental_data_json, i, s))
            except:
                print(" no {} data for {} ".format(i, s))

        for i in indicators_per_share:
            try:
                data = get_one_absolute_indicator_from_finnhub(fundamental_data_json, i, s)
                data_per_symbol.append(data)
            except:
                print("no {} data for {} ".format(i, s))

        for i in indicators_ratio:
            try:
                data_per_symbol.append(
                    get_one_ratio_indicator_from_finnhub(fundamental_data_json, i, s))
            except:
                print("no {} data  for  {} ".format(i, s))
        for i in indicators_percentage:
            try:
                data_per_symbol.append(
                    get_one_relative_indicator_from_finnhub(fundamental_data_json, i, s))
            except:
                print("no {} data  for  {} ".format(i, s))

        #unfiltered
        #stupid_plot_data_lists(data_per_symbol,source)

        filter_plot_data_list_per_symbol(data_per_symbol,source)
        all_plot_data.append(data_per_symbol)

if __name__ == '__main__':
    get_data_from_finnhub()

    get_data_from_alpha_vantage()

    symbols = ["MSFT", "IBM", "AAPL"]
    calling_alpha_vantage_api(symbols)

    # TODO use balance sheet -> goodwill unter anderem

    # TODO workflow erstellen wenn neues File auf neue Faktoren untersucht werden muss

    # TODO How TO HANDLE exception

    # TODO LONGTERM DATA checken

    #TODO log on log off