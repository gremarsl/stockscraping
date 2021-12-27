from data_processor import processor_filter_plot_data
from functions_for_finnhub import get_one_indicator_from_finnhub, \
    get_one_relative_indicator_from_finnhub
from general_functions import read_data_from_file


class NoData:
    pass


def analyse_data_from_finnhub(symbols: list):
    source = "finnhub"
    all_plot_data = []

    period = 'quarterly'

    all_symbols_per_share = []


    for s in symbols:
        data_per_symbol = []

        # new:
        fundamental_data_json = read_data_from_file("fundamental_data_finnhub_" + s + ".json")

        indicator_absolute_list = ["grossMargin"]  # netMargin
        indicators_per_share = ["eps", "ebitPerShare"]
        indicators_ratio = ["cashRatio", "currentRatio"]
        indicators_percentage = ["totalDebtToEquity"]

        counter = 0
        for i in indicator_absolute_list:
            try:
                temp_data = get_one_indicator_from_finnhub(fundamental_data_json, period, i, s)
                data_per_symbol.append(temp_data)
            except NoData:
                print(" no {} data for {} ".format(i, s))

        counter = 0
        for i in indicators_per_share:
            try:
                temp_data = get_one_indicator_from_finnhub(fundamental_data_json, period, i, s)
                data_per_symbol.append(temp_data)

                if counter < 1:
                    all_symbols_per_share.append(temp_data)
                    counter = 1
            except NoData:
                print("no {} data for {} ".format(i, s))
        for i in indicators_ratio:
            try:
                temp_data = get_one_indicator_from_finnhub(fundamental_data_json, period, i, s)
                data_per_symbol.append(temp_data)
            except NoData:
                print("no {} data  for  {} ".format(i, s))
        for i in indicators_percentage:
            try:
                temp_data = get_one_relative_indicator_from_finnhub(fundamental_data_json, period, i, s)
                data_per_symbol.append(temp_data)

            except NoData:
                print("no {} data  for  {} ".format(i, s))

        processor_filter_plot_data(data_per_symbol, relative_data=False, all_symbols=False, source=source)

    analyse_all_companies = 1
    if analyse_all_companies ==1:
        processor_filter_plot_data(all_symbols_per_share, relative_data=False, all_symbols=True, source=source)
