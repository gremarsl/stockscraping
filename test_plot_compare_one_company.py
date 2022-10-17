import json

import pandas as pd

import global_vars
from general_functions import read_data_from_file, extract_indicator_from_my_json_file


def one_company_only(symbols):
    symbol = symbols[0]
    data = read_data_from_file(global_vars.filepath_yahoo + "yahoo_quarterly_balance_sheet_" + symbol + ".json")

    #get Data Frame with indicators
    df = pd.read_csv(global_vars.filepath_yahoo + "yahoo_quarterly_balance_sheet_" + symbol + ".csv", sep=';', decimal=",")

    if data is None:
        raise Exception("There was no data read from file. Please check if the file exists")

    #TODO if you want to calculate a new indicator - call calculate_quotient

    rel_data = []
    if global_vars.ANALYZE_YAHOO_REL == 1:
        for i in global_vars.REL_INDICATORS_LIST:
            dividend, divisor = split_indicator_in_two(i)
            dividend_data = get_float_data(data, indicator=dividend, symbol=symbol)

            divisor_data = get_float_data(data, indicator=divisor, symbol=symbol)
            quotient = calculate_quotient(dividend_data[1], divisor_data[1])

            temp_data = [dividend_data[0], quotient, symbol, i]
            rel_data.append(temp_data)

    rel_data_live = []
    if global_vars.ANALYZE_YAHOO_REL_LIVE == 1:
        for i in global_vars.REL_LIVE_INDICATOR_LIST:
            dividend, divisor = split_indicator_in_two(i)
            divisor_data = get_float_data(data, indicator=divisor, symbol=symbol)
            # try to get data live from yahoo
            try:
                marketCap = get_market_cap_from_yahoo_finance(symbol)

            except Exception:
                raise print("No market cap available")

            quotient = list(map(lambda x: marketCap / x, divisor_data[1]))
            temp_data = [divisor_data[0], quotient, symbol, i]

            rel_data_live.append(temp_data)

    # plot data
    if global_vars.ANALYZE_YAHOO_ABS:
        processor_filter_plot_data(data_list=abs_data, relative_data=False, all_symbols=False)
    if global_vars.ANALYZE_YAHOO_REL:
        processor_filter_plot_data(data_list=rel_data, relative_data=True, all_symbols=False)
    if global_vars.ANALYZE_YAHOO_REL_LIVE:
        processor_filter_plot_data(data_list=rel_data_live, relative_data=True, all_symbols=False)


# plot 1
'''


totalrevenue 
costofrevenue
grossprofit
net profit 

grossmargin
net margin
'''

indicator = ["TotalRevenue", "CostOfRevenue", "GrossProfit", "NetIncome"]
# TODO calculate indicator

file = "D:\\Desktop\\GOOGL\\balanceAnnual.csv"

df = pd.read_csv(file, sep=';', decimal=",")

symbols = ["GOOGL"]
one_company_only(symbols)
