import os
import json

import options
from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, get_fundamental_data_from_finnhub, \
    get_one_relative_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub
from functions_for_yahoo import get_last_price_for_symbol_from_yahoo_finance, get_market_cap_from_yahoo_finance
from general_functions import get_data_from_file, filter_data
from plot_functions import stupid_plot_data_lists
from functions_for_alpha_vantage import \
    extract_quarterly_report_data_from_alpha, \
    calling_alpha_vantage_api


# Understand JSON
# object: {}
# array : []

class NoData(Exception): pass  # declare a label


class IncorrectExcelData(Exception): pass


class IncorrectAlphaData(Exception): pass


class NoEbitData(Exception): pass



def processor_filter_plot_data(data_list: list, relativeData: bool, source: str):
    # all_data_list = [data_per_symbol_1]

    if len(data_list) == 0:
        raise Exception("No data")

    if (source != "alpha_vantage") and (source != "finnhub") and (source != "excel"):
        raise Exception("data is not from source alpha_vantage, finnhub or excel")


    else:
        if (not relativeData) and source == "excel":
            try:
                # filter
                indicators = filter_data(data_list, options.options_abs_indicator)
                # plot data
                stupid_plot_data_lists(indicators, source)

            except IncorrectExcelData:
                print("analyzing excel data failed")

        if relativeData and source == "excel":
            try:
                # filter
                indicators = filter_data(data_list, options.options_rel_indicator)
                # plot data
                stupid_plot_data_lists(indicators, source)

            except IncorrectExcelData:
                print("analyzing excel data failed")

        if relativeData and source == "alpha_vantage":

            try:
                stupid_plot_data_lists(filter_data(data_list, options.options_rel_indicator), source)

            except IncorrectAlphaData:
                print("analyzing alpha data failed")

        if (not relativeData) and source == "alpha_vantage":

            try:
                stupid_plot_data_lists(filter_data(data_list, options.options_abs_indicator), source)

            except:
                print("no working indicators data")

        if (not relativeData) and source == "finnhub":
            except_grossmargin = list(filter(lambda x: (x[3] != "grossMargin"), data_list))

            except_grossmargin_debt = list(filter(lambda x: x[3] != "totalDebtToEquity", except_grossmargin))

            eps_ebit_per_share_plot_data = list(
                filter(lambda x: x[3] == "eps" or x[3] == "ebitPerShare", data_list))

            try:
                stupid_plot_data_lists(except_grossmargin_debt, source)
            except:
                print("Not working to plot ratios_eps_ebit_net_margin_data data in one plot {}".format(data_list))

            if len(eps_ebit_per_share_plot_data) == 0:
                raise NoEbitData()

def convert_list_elements_to_int(y):
    return [int(x) for x in y]


def split_indicator_in_two(indicator):
    dividend_str = indicator.split('_to_')[0]
    divisor_str = indicator.split('_to_')[1]

    return dividend_str, divisor_str


def calculate_quotient(dividend_data,divisor_data, indicator, symbol):

    dividend_str, divisor_str = split_indicator_in_two(indicator)


    quotient_list = [(x / y) * 100 for x, y in zip(dividend_data, divisor_data)]

    return quotient_list

# TODO split - this func has two different purposes
def get_data(input_data, indicator, symbol):

    # quotient: research and development:
    list_dividend = extract_quarterly_report_data_from_alpha(input_data, indicator, symbol=symbol)

    # convert to int
    list_dividend_converted = convert_list_elements_to_int(list_dividend[1])

    data = [list_dividend[0],list_dividend_converted, symbol, indicator]

    return data

# TODO split - this func has two different purposes
def get_data_calculate_quotient(input_data, indicator, symbol):
    dividend_str = indicator.split('_to_')[0]
    divisor_str = indicator.split('_to_')[1]

    # quotient: research and development:
    list_dividend = extract_quarterly_report_data_from_alpha(input_data, dividend_str, symbol=symbol)
    list_divisor = extract_quarterly_report_data_from_alpha(input_data, divisor_str, symbol=symbol)

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
                quaterly_absolute_data_per_symbol.append(
                    extract_quarterly_report_data_from_alpha(income_statement, i, symbol=s))
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

        processor_filter_plot_data(quaterly_absolute_data_per_symbol, False, source)
        processor_filter_plot_data(quaterly_relative_data_per_symbol, True, source)

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

        processor_filter_plot_data(data_per_symbol, relativeData=False, source=source)
        all_plot_data.append(data_per_symbol)


def get_data_from_local_json_file():
    source = "excel"
    # read data
    filename = "D:\\Desktop\\Finanzreporte\\json\\testsymbol.json"
    data = get_data_from_file(filename)

    # my indicators I want to analyse from the json file
    my_abs_indicators = ["totalRevenue", "netIncome"]
    my_rel_indicators = ["researchAndDevelopment_to_totalRevenue", "totalLiabilities_to_totalAssets"]
    my_rel_indicators_live =["totalRevenue_to_marketCap"]

    my_per_share_indicator = ["eps", "ebitPerShare"]

    abs_data = []
    for i in my_abs_indicators:
        extracted_data = extract_quarterly_report_data_from_alpha(data_json=data, indicator=i, symbol="TEST")
        abs_data.append(extracted_data)

    rel_data = []
    for i in my_rel_indicators:
        return_data = get_data_calculate_quotient(data, indicator=i, symbol="TEST")
        rel_data.append(return_data)

    marketCap = get_market_cap_from_yahoo_finance("DAI.DE")

    for i in my_rel_indicators_live:
        dividend, divisor = split_indicator_in_two(i)
        return_data1 = get_data(data, indicator=dividend, symbol="TEST")

        #wenn parameter vorhanden, dann hole dir aus file:
        use_live_parameter=True

        if not use_live_parameter:
            return_data2 = get_data(data, indicator=divisor, symbol="TEST")
            quotient = calculate_quotient(return_data1[1],return_data2[1],i,symbol="TEST")

        if use_live_parameter:
            created_list = [marketCap] * len(return_data1[1])
            converted_list = convert_list_elements_to_int(created_list)

            quotient = calculate_quotient(return_data1[1],converted_list,i,symbol="TEST")


        #add another list around to make it work
        rel_data_live = [[return_data1[0],quotient,"TEST", i]]


    # plotdata

    processor_filter_plot_data(data_list=abs_data, relativeData=False, source=source)
    processor_filter_plot_data(data_list=rel_data, relativeData=True, source=source)
    processor_filter_plot_data(data_list=rel_data_live, relativeData=True, source=source)




    #TODO:
    # calculate ratio net income zu revenue
    # verhältnis goodwill zu marktkapitaliserung
    # verhältnis total assets zu marketkapitalisierung
    # verhältnis asset zu liabilites
    # verhältnis free cash flow zu revenue

    pass


# SWITCHES:
analyse_own_excel_data = 1
analyse_finnhub_data = 0
get_alpha_data = 0
analyse_alpha_data = 0
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
