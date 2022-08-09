import global_vars
from analyse_data_from_alpha_vantage import compare_companies
from data_processor import processor_filter_plot_data
from general_functions import read_data_from_file, split_indicator_in_two, calculate_quotient, \
    convert_list_elements_to_int, extract_quarterly_report_data_from_my_json_file, get_float_data, \
    get_key_value_from_local_file

analyse_abs_indicator = 0
analyse_rel_indicator = 0
analyse_rel_live_indicator = 1


def one_company_only(symbol, source="my_json"):
    data = read_data_from_file(global_vars.filepath_my_json + symbol + ".json")

    # my indicators I want to analyse from the json file
    my_abs_indicators = ["totalRevenue", "grossProfit", "operatingIncome", "ebit", "netIncome"]
    my_rel_indicators = ["researchAndDevelopment_to_totalRevenue", "operatingIncome_to_totalRevenue",
                         "totalLiabilities_to_totalAssets", "totalCurrentLiabilities_to_totalCurrentAssets",
                         "grossProfit_to_totalRevenue",
                         ]  # , "totalShareholdersEquity_to_totalAssets" == ,"totalAssets_minus_totalLiabilities"
    my_rel_indicators_live = ["marketCap_to_totalRevenue", "marketCap_to_totalAssets","marketCap_to_netIncome"]

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

            if global_vars.market_cap == 0:
                # because in main the market cap was called from yahoo finance
                print("get live data did not work in order to calculate: {}".format(i))

            else:
                try:
                    marketCap = global_vars.market_cap
                except:
                    print("WARNING - live data not used - exception hit")
                    marketCap = get_key_value_from_local_file("marketCap", symbol)

                created_list = [marketCap] * len(dividend_data[1])
                converted_list = convert_list_elements_to_int(created_list)

                quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol=symbol)

            # add another list around to make it work
            temp_data = [dividend_data[0], quotient, symbol, i]
            rel_data_live.append(temp_data)

    # plotdata

    if analyse_abs_indicator == 1:
        processor_filter_plot_data(data_list=abs_data, relative_data=False, all_symbols=False, source=source)
    if analyse_rel_indicator == 1:
        processor_filter_plot_data(data_list=rel_data, relative_data=True, all_symbols=False, source=source)
    if analyse_rel_live_indicator == 1:
        processor_filter_plot_data(data_list=rel_data_live, relative_data=True, all_symbols=False, source=source)


def analyze_data_from_local_json_file(symbols: list, analyze_my_json_data_compare_companies: int):
    source = "my_json"

    if analyze_my_json_data_compare_companies:
        compare_companies(symbols, source)

    else:
        for s in symbols:
            one_company_only(s)

