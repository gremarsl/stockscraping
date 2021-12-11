import os
import json

import options
from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, get_fundamental_data_from_finnhub, \
    get_one_relative_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub
from plot_functions import stupid_plot_data_lists
from functions_for_alpha_vantage import \
    get_quaterly_report_alpha, \
    calling_alpha_vantage_api


# Understand JSON
# object: {}
# array : []

class NoData(Exception): pass  # declare a label


class IncorrectExcelData(Exception): pass


class IncorrectAlphaData(Exception): pass


class NoEbitData(Exception): pass


def filter_data(data_list,options):
    packed_indicators = []
    indicators = []
    for i in options:
        indicator = filter(lambda x: x[3] == i, data_list)
        indicator_list = list(indicator)
        if(len(indicator_list) !=0):
            packed_indicators.append(indicator_list)

    #unpacking the list because with append to indicators - we have one list element to much - what we didnt have when doing list(filter(...))
    for i in packed_indicators:
        [unpack] = i
        indicators.append(unpack)

    return indicators

def filter_excel_data_origin(data_list,options):
    indicators = list(filter(
        lambda x: x[3] == "totalRevenue" or "netIncome",
        data_list))
    return indicators


def filter_relative_alpha_vantage_data(data_list):
    indicators = list(filter(
        lambda x: x[3] == "researchAndDevelopment_to_totalRevenue" or "totalLiabilities_to_totalAssets",
        data_list))
    return indicators


def filter_plot_data_list_per_symbol(data_list: list, relativeData: bool, source: str):
    # all_data_list = [data_per_symbol_1]

    if (len(data_list) == 0) or ((source != "alpha_vantage") and (source != "finnhub") and (source != "excel")):
        raise Exception("No data or data is not from source alpha_vantage, finnhub or excel")

    else:
        if source == "excel":
            try:
                # filter
                indicators_origin = filter_excel_data_origin(data_list,options.options_test_indicator)

                indicators = filter_data(data_list,options.options_test_indicator)
                # plot data
                stupid_plot_data_lists(indicators, source)

            except IncorrectExcelData:
                print("analyzing excel data failed")

        if relativeData and source == "alpha_vantage":

            try:
                stupid_plot_data_lists(filter_data(data_list,options.options_rel_indicator), source)

                #stupid_plot_data_lists(filter_relative_alpha_vantage_data(data_list), source)
            except IncorrectAlphaData:
                print("analyzing alpha data failed")

        if relativeData == False and source == "alpha_vantage":

            try:
                indicators = list(filter(
                    lambda x: x[
                                  3] == "grossProfit" or "totalRevenue" or "ebit" or "netIncome" or "operatingIncome" or "incomeBeforeTax",
                    data_list))
                stupid_plot_data_lists(indicators, source)
            except:
                print("no working indicators data")

        if relativeData == False and source == "finnhub":
            except_grossmargin = list(filter(lambda x: (x[3] != "grossMargin"), data_list))

            except_grossmargin_debt = list(filter(lambda x: x[3] != "totalDebtToEquity", except_grossmargin))

            eps_ebit_per_share_plot_data = list(
                filter(lambda x: x[3] == "eps" or x[3] == "ebitPerShare", data_list))

            ratios_eps_ebit_net_margin_data = list(filter(
                lambda x: (x[3] == "eps" or x[3] == "cashRatio" or x[3] == "currentRatio" or x[3] != "ebitPerShare" or
                           x[3] == "netMargin"), data_list))

            try:
                stupid_plot_data_lists(except_grossmargin_debt, source)
            except:
                print("Not working to plot ratios_eps_ebit_net_margin_data data in one plot {}".format(data_list))

            if len(eps_ebit_per_share_plot_data) == 0:
                raise NoEbitData()


def get_data_from_file(filename):
    if os.path.isfile(filename):
        with open(filename) as json_file:
            data = json.load(json_file)
    else:
        print(
            "WARNING: file not found - This should not be reached")

    return data


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

    quaterly_absolute_data_per_symbol = []
    quaterly_relative_data_per_symbol = []

    for s in symbols:

        income_statement = get_data_from_file("income_statement_alpha_" + s + ".json")

        for i in indicator_absolute_income_statement:
            try:
                quaterly_absolute_data_per_symbol.append(get_quaterly_report_alpha(income_statement, i, symbol=s))
            except:
                print("error in quaterly data {}".format(s))

        for i in indicator_percentage_income_statement:

            try:
                quaterly_relative_data_per_symbol.append(
                    get_data_calculate_quotient(data_origin=income_statement, indicator=i, symbol=s))

            except:
                print(
                    "calculate quotient of {} didint work".format(i))

        balance_sheet = get_data_from_file("balance_sheet_alpha_" + s + ".json")

        for i in indicator_percentage_balance_sheet:

            try:
                quaterly_relative_data_per_symbol.append(
                    get_data_calculate_quotient(data_origin=balance_sheet, indicator=i, symbol=s))

            except:
                print(
                    "calculate quotient of {} didint work".format(i))

        filter_plot_data_list_per_symbol(quaterly_absolute_data_per_symbol, False, source)
        filter_plot_data_list_per_symbol(quaterly_relative_data_per_symbol, True, source)

    pass


def get_data_from_finnhub():
    source = "finnhub"
    all_plot_data = []
    all_plot_data_test = []

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

        filter_plot_data_list_per_symbol(data_per_symbol, relativeData=False, source=source)
        all_plot_data.append(data_per_symbol)




def get_data_from_local_json_file():
    source = "excel"
    # read data
    filename = "D:\\Desktop\\Finanzreporte\\json\\testsymbol.json"
    data = get_data_from_file(filename)

    plotdata = []

    # extract quaterly data
    my_indicators = ["totalRevenue", "netIncome"]

    for i in my_indicators:
        return_data = get_quaterly_report_alpha(data_json=data, indicator=i, symbol="TEST")
        plotdata.append(return_data)

    # plotdata
    filter_plot_data_list_per_symbol(plotdata, False, source)

    # TODO - live price of symbol - live marketkapitalisierung
    pass

# SWITCHES:
analyse_own_excel_data = 1
analyse_finnhub_data = 0
get_alpha_data = 0
analyse_alpha_data = 1
alpha_vantage_symbols = ["AVGO"]  # "IBM", "AAPL"

if __name__ == '__main__':
    if analyse_own_excel_data == 1:
        get_data_from_local_json_file()

    if analyse_finnhub_data == 1:
        get_data_from_finnhub()

    if get_alpha_data == 1:
        calling_alpha_vantage_api(alpha_vantage_symbols)

    if analyse_alpha_data == 1:
        analyse_data_from_alpha_vantage(alpha_vantage_symbols)
