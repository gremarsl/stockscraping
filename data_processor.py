import options
from general_functions import filter_data
from plot_functions import stupid_plot_data_lists, plot_compare_symbols_one_indicator


class NoData(Exception):
    pass  # declare a label


class IncorrectExcelData(Exception):
    pass


class IncorrectAlphaData(Exception):
    pass


class NoEbitData(Exception):
    pass


class NoWorkingIndicatorData(Exception):
    pass


class NotWorkingToPlot(Exception):
    pass


def processor_filter_plot_data(data_list: list, relative_data: bool, all_symbols: bool, source: str):
    # all_data_list = [data_per_symbol_1]

    if len(data_list) == 0:
        raise Exception("No data")

    if (source != "alpha_vantage") and (source != "finnhub") and (source != "excel"):
        raise Exception("data is not from source alpha_vantage, finnhub or excel")

    else:
        if (not relative_data) and source == "excel":
            try:
                # filter
                indicators = filter_data(data_list, options.options_abs_indicator)
                # plot data
                stupid_plot_data_lists(indicators, source)

            except IncorrectExcelData:
                print("analyzing excel data failed")

        if relative_data and source == "excel":
            try:
                # filter
                indicators = filter_data(data_list, options.options_rel_indicator)
                # plot data
                stupid_plot_data_lists(indicators, source)

            except IncorrectExcelData:
                print("analyzing excel data failed")

        if relative_data and source == "alpha_vantage" and all_symbols is False:

            try:
                stupid_plot_data_lists(filter_data(data_list, options.options_rel_indicator), source)

            except IncorrectAlphaData:
                print("analyzing alpha data failed")

        if relative_data and source == "alpha_vantage" and all_symbols is True:

            try:

                # stupid_plot_data_lists(filter_data_all_symbols(data_list, options.options_rel_indicator), source)
                plot_compare_symbols_one_indicator(data_list, source)

            except IncorrectAlphaData:
                print("analyzing alpha data failed")

        if (not relative_data) and source == "alpha_vantage" and all_symbols is True:

            try:

                # stupid_plot_data_lists(filter_data_all_symbols(data_list, options.options_rel_indicator), source)
                plot_compare_symbols_one_indicator(data_list, source)

            except IncorrectAlphaData:
                print("analyzing alpha data failed")

        if (not relative_data) and source == "alpha_vantage" and all_symbols is False:

            try:
                stupid_plot_data_lists(filter_data(data_list, options.options_abs_indicator), source)

            except NoWorkingIndicatorData:
                print("no working indicators data")

        if (not relative_data) and source == "finnhub":
            except_grossmargin = list(filter(lambda x: (x[3] != "grossMargin"), data_list))

            except_grossmargin_debt = list(filter(lambda x: x[3] != "totalDebtToEquity", except_grossmargin))

            eps_ebit_per_share_plot_data = list(
                filter(lambda x: x[3] == "eps" or x[3] == "ebitPerShare", data_list))

            try:
                stupid_plot_data_lists(except_grossmargin_debt, source)
            except NotWorkingToPlot:
                print("Not working to plot ratios_eps_ebit_net_margin_data data in one plot {}".format(data_list))

            if len(eps_ebit_per_share_plot_data) == 0:
                raise NoEbitData()
