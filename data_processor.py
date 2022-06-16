import options
from general_functions import filter_data
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


def processor_filter_plot_data(data_list: list, relative_data: bool, all_symbols: bool, source: str):
    # all_data_list = [data_per_symbol_1]

    if len(data_list) == 0:
        raise Exception("No data")

    match source:
        case "alpha_vantage":
            if all_symbols is True:
                try:
                    plot_compare_symbols_one_indicator(data_list, source)
                except IncorrectAlphaData:
                    print("analyzing alpha data failed")

            else:
                if relative_data is True:
                    try:
                        stupid_plot_data_lists(filter_data(data_list, options.options_rel_indicator), source)

                    except IncorrectAlphaData:
                        print("analyzing alpha data failed")

                if relative_data is False:

                    try:
                        stupid_plot_data_lists(filter_data(data_list, options.options_abs_indicator), source)

                    except NoWorkingIndicatorData:
                        print("no working indicators data")

        case "finnhub":
            if all_symbols is True:
                try:
                    plot_compare_symbols_one_indicator(data_list, source)
                except NotWorkingToPlot:
                    print("Not working to plot")

            else:
                if not relative_data:
                    except_grossmargin = list(filter(lambda x: (x[3] != "grossMargin"), data_list))
                    except_grossmargin_debt = list(filter(lambda x: x[3] != "totalDebtToEquity", except_grossmargin))

                    eps_ebit_per_share_plot_data = list(
                        filter(lambda x: x[3] == "eps" or x[3] == "ebitPerShare", data_list))

                    try:
                        stupid_plot_data_lists(except_grossmargin_debt, source)
                    except NotWorkingToPlot:
                        print(
                            "Not working to plot ratios_eps_ebit_net_margin_data data in one plot {}".format(data_list))

                    if len(eps_ebit_per_share_plot_data) == 0:
                        raise NoEbitData()
                else:
                    print("ERROR - this case is not catched")

        case "my_json":
            if (not relative_data) and all_symbols is True:
                try:
                    # filter
                    indicators = filter_data(data_list, options.options_abs_indicator)
                    # plot data
                    plot_compare_symbols_one_indicator(data_list, source)

                    # stupid_plot_data_lists(indicators, source)

                except IncorrectJsonData:
                    print("analyzing my_json data failed")

            if relative_data and all_symbols is True:
                try:
                    # filter
                    indicators = filter_data(data_list, options.options_rel_indicator)
                    # plot data
                    plot_compare_symbols_one_indicator(data_list, source)

                    # stupid_plot_data_lists(indicators, source)

                except IncorrectJsonData:
                    print("analyzing my_json data failed")

            # if one symbol and multiple indicators
            if  relative_data and all_symbols is False:
                try:
                    # filter
                    indicators = filter_data(data_list, options.options_rel_indicator)
                    # plot data
                    stupid_plot_data_lists(data_list, source)

                    # stupid_plot_data_lists(indicators, source)

                except IncorrectJsonData:
                    print("analyzing my_json data failed")

        case _:
            raise Exception("data is not from source alpha_vantage, finnhub or my_json")