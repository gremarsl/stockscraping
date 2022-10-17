# **********************************************************************************************************************
# Imports
# **********************************************************************************************************************
import global_vars
from general_functions import keep_every_nth
from plot_functions import stupid_plot_data_lists, plot_compare_symbols_one_indicator


class NoData(Exception):
    pass  # declare a label


class IncorrectJsonData(Exception):
    pass


class IncorrectAlphaData(Exception):
    pass


class NoEbitData(Exception):
    pass


class NoWorkingIndicatorData(Exception):
    pass


class NotWorkingToPlot(Exception):
    pass


def get_number_of_symbols_in_list(data_list):
    symbol_list = []

    for i in data_list:
        if i[2] not in symbol_list:
            symbol_list.append(i[2])

    return len(symbol_list)


def count_number_of_entries(data_list):
    element_to_count = data_list[0][2]
    counter = 0
    for i in data_list:
        if i[2] == element_to_count:
            counter += 1

    return counter


def processor_filter_plot_data(data_list: list, relative_data: bool, all_symbols: bool):
    # all_data_list = [data_per_symbol_1]
    source = global_vars.SOURCE
    if len(data_list) == 0:
        raise Exception("No data")

    if all_symbols is True:
        if data_list[0][3] != data_list[1][3]:

            number_of_symbols_in_data_list = get_number_of_symbols_in_list(data_list)
            number_of_indicators_per_symbol = count_number_of_entries(data_list)

            for x in range(0,number_of_indicators_per_symbol):
                new_data_list = keep_every_nth(x,data_list,number_of_indicators_per_symbol)
                plot_compare_symbols_one_indicator(new_data_list,source)

        else:
            try:
                plot_compare_symbols_one_indicator(data_list, source)
            except IncorrectAlphaData:
                print("analyzing alpha data failed")

    if (not relative_data) and all_symbols is False:
        try:
            # plot data
            stupid_plot_data_lists(data_list, source)

        except IncorrectJsonData:
            print("analyzing my_json data failed")

    # if one symbol and multiple indicators
    if relative_data and all_symbols is False:
        try:
            # plot data
            stupid_plot_data_lists(data_list, source)

        except IncorrectJsonData:
            print("analyzing my_json data failed")
