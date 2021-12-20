from data_processor import processor_filter_plot_data
from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub, \
    get_one_relative_indicator_from_finnhub
from general_functions import get_data_from_file


def analyse_data_from_finnhub(symbols: list):
    source = "finnhub"
    all_plot_data = []

    period = 'quarterly'

    for s in symbols:
        data_per_symbol = []

        # new:
        fundamental_data_json = get_data_from_file("fundamental_data_finnhub_" + s + ".json")

        indicator_absolute_list = ["grossMargin"]  # netMargin
        indicators_per_share = ["eps", "ebitPerShare"]
        indicators_ratio = ["cashRatio", "currentRatio"]
        indicators_percentage = ["totalDebtToEquity"]
        indicators_live = ["totalRevenue_to_marketCap", "totalAssets_to_marketCap"]

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

        processor_filter_plot_data(data_per_symbol, relative_data=False, all_symbols=False, source=source)
        all_plot_data.append(data_per_symbol)
