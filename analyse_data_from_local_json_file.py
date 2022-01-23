from data_processor import processor_filter_plot_data
from functions_for_alpha_vantage import extract_quarterly_report_data_from_alpha
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import read_data_from_file, split_indicator_in_two, calculate_quotient, \
    convert_list_elements_to_int, get_data, extract_quarterly_report_data_from_my_json_file, get_float_data, \
    get_key_value_from_local_file

analyse_abs_indicator = 1
analyse_rel_indicator = 1
analyse_rel_live_indicator = 1


def analyse_data_from_local_json_file(symbol):

    filename = "D:\\Desktop\\Finanzreporte\\json\\" + symbol[0] + ".json"
    data = read_data_from_file(filename)

    # my indicators I want to analyse from the json file
    my_abs_indicators = ["totalRevenue", "netIncome"]
    my_rel_indicators = ["researchAndDevelopment_to_totalRevenue","operatingIncome_to_totalRevenue", "totalLiabilities_to_totalAssets",
                         "grossProfit_to_totalRevenue",
                         ] #, "totalShareholdersEquity_to_totalAssets" == ,"totalAssets_minus_totalLiabilities"
    my_rel_indicators_live = ["totalRevenue_to_marketCap", "totalAssets_to_marketCap"]

    abs_data = []
    if analyse_abs_indicator == 1:
        for i in my_abs_indicators:
            extracted_data = extract_quarterly_report_data_from_my_json_file(data_json=data, indicator=i, symbol=symbol)
            abs_data.append(extracted_data)

    rel_data = []
    if analyse_rel_indicator == 1:
        for i in my_rel_indicators:
            dividend, divisor = split_indicator_in_two(i)
            dividend_data = get_float_data(data, indicator=dividend, symbol=symbol)

            divisor_data = get_float_data(data, indicator=divisor, symbol=symbol)
            quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=symbol)

            temp_data = [dividend_data[0], quotient, symbol, i]
            rel_data.append(temp_data)

    rel_data_live = []
    if analyse_rel_live_indicator == 1:
        for i in my_rel_indicators_live:
            dividend, divisor = split_indicator_in_two(i)
            dividend_data = get_float_data(data, indicator=dividend, symbol=symbol)

            use_live_parameter = True

            if not use_live_parameter:
                return_data2 = get_data(data, indicator=divisor, symbol=symbol)
                quotient = calculate_quotient(dividend_data[1], return_data2[1], i, symbol=symbol)

            if use_live_parameter:
                try:
                    try:
                        marketCap = get_market_cap_from_yahoo_finance(symbol)
                    except:
                        marketCap = get_key_value_from_local_file("marketCap",symbol)

                    created_list = [marketCap] * len(dividend_data[1])
                    converted_list = convert_list_elements_to_int(created_list)

                    quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol=symbol)
                except:
                    print("get live data did not work in order to calculate: {}".format(i))
            # add another list around to make it work
            temp_data = [dividend_data[0], quotient, symbol, i]
            rel_data_live.append(temp_data)

    # plotdata
    source = "my_json"
    if analyse_abs_indicator == 1:
        processor_filter_plot_data(data_list=abs_data, relative_data=False, all_symbols=True, source=source)
    if analyse_rel_indicator == 1:
        processor_filter_plot_data(data_list=rel_data, relative_data=True, all_symbols=True, source=source)

    if analyse_rel_live_indicator == 1:
        processor_filter_plot_data(data_list=rel_data_live, relative_data=True, all_symbols=True, source=source)

    pass
