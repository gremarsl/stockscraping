import global_vars
from data_processor import processor_filter_plot_data
from functions_for_alpha_vantage import extract_quarterly_report_data_from_alpha
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import read_data_from_file, split_indicator_in_two, calculate_quotient, \
    extract_quarterly_report_data_from_my_json_file, get_float_data, get_data


'''
Improvement: Merge of json data to one file -> this reduces the effort of different files -> having different data in different files
'''
abs_indicators = ["TotalRevenue","NetIncome"]
rel_indicators = ["NetIncome_to_TotalRevenue", "ResearchDevelopment_to_TotalRevenue", "TotalLiab_to_TotalAssets",
                  "TotalCurrentLiab_to_TotalCurrentAssets"]  # ,

rel_live_indicators = ["marketCap_to_TotalRevenue", "marketCap_to_NetIncome", "marketCap_to_TotalAssets"]


def compare_companies(symbols, source):
    all_symbols_quarterly_abs_data = []

    all_symbols_quarterly_rel_data = []

    all_symbols_quarterly_rel_live_data = []

    for s in symbols:
        match source:
            case "my_json":
                data = read_data_from_file(global_vars.filepath_yahoo + "yahoo_total_data_" + s + ".json")

                if global_vars.analyze_abs_yahoo:

                    for i in abs_indicators:
                        try:
                            temp_data = extract_quarterly_report_data_from_alpha(data, i, symbol=s)
                            all_symbols_quarterly_abs_data.append(temp_data)

                        except BaseException:
                            print(f"error in quaterly data {s}")

                if global_vars.analyze_rel_yahoo:

                    for i in rel_indicators:

                        try:
                            # extract data for every indicator
                            dividend, divisor = split_indicator_in_two(i)
                            dividend_data = get_data(data, indicator=dividend, symbol=s)

                            divisor_data = get_data(data, indicator=divisor, symbol=s)
                            quotient = calculate_quotient(dividend_data[1], divisor_data[1])

                            temp_data = [dividend_data[0], quotient, s, i]

                            all_symbols_quarterly_rel_data.append(temp_data)

                        except:
                            print(f"-{s}- calculate quotient of {i} didnt work")

                if global_vars.analyze_rel_live_yahoo:

                    for i in rel_live_indicators:

                        try:
                            dividend, divisor = split_indicator_in_two(i)
                            divisor_data = get_data(data, indicator=divisor, symbol=s)

                            marketCap = get_market_cap_from_yahoo_finance(s)

                            quotient = list(map(lambda x: marketCap / x, divisor_data[1]))

                            temp_data = [divisor_data[0], quotient, s, i]
                            all_symbols_quarterly_rel_live_data.append(temp_data)


                        except:
                            print(f"-{s}- calculate quotient of {i} didnt work")

    match source:
        case "my_json":
            if global_vars.analyze_abs_yahoo:
                processor_filter_plot_data(all_symbols_quarterly_abs_data, False, True,source)

            if global_vars.analyze_rel_yahoo:
                processor_filter_plot_data(all_symbols_quarterly_rel_data, True, True,source)

            if global_vars.analyze_rel_live_yahoo:
                processor_filter_plot_data(all_symbols_quarterly_rel_live_data, True, True,source)

        case _:
            raise Exception("invalid source")


def one_company_only(symbol, source="my_json"):
    # data = read_data_from_file(global_vars.filepath_my_json + symbol + ".json")
    data = read_data_from_file(global_vars.filepath_yahoo + "yahoo_total_data_" + symbol + ".json")

    if data is None:
        raise Exception("There was no data read from file. Please check if the file exists")

    abs_indicators = ["TotalRevenue", "GrossProfit"]
    rel_indicators = ["ResearchDevelopment_to_TotalRevenue", "OperatingIncome_to_TotalRevenue",
                      "TotalCurrentLiab_to_TotalCurrentAssets"]
    my_rel_indicators_live = ["marketCap_to_TotalAssets"]

    abs_data = []
    if global_vars.analyze_abs_yahoo == 1:
        for i in abs_indicators:
            extracted_data = extract_quarterly_report_data_from_my_json_file(data_json=data, indicator=i, symbol=symbol)
            abs_data.append(extracted_data)

    rel_data = []
    if global_vars.analyze_rel_yahoo == 1:
        for i in rel_indicators:
            dividend, divisor = split_indicator_in_two(i)
            dividend_data = get_float_data(data, indicator=dividend, symbol=symbol)

            divisor_data = get_float_data(data, indicator=divisor, symbol=symbol)
            quotient = calculate_quotient(dividend_data[1], divisor_data[1])

            temp_data = [dividend_data[0], quotient, symbol, i]
            rel_data.append(temp_data)

    rel_data_live = []
    if global_vars.analyze_rel_live_yahoo == 1:
        for i in my_rel_indicators_live:
            dividend, divisor = split_indicator_in_two(i)
            divisor_data = get_float_data(data, indicator=divisor, symbol=symbol)
            # try to get data live from yahooo
            try:
                marketCap = get_market_cap_from_yahoo_finance(symbol)

            except:
                raise Exception("No market cap available")

            quotient = list(map(lambda x: marketCap / x, divisor_data[1]))
            temp_data = [divisor_data[0], quotient, symbol, i]

            rel_data_live.append(temp_data)

    # plotdata

    if global_vars.analyze_abs_yahoo:
        processor_filter_plot_data(data_list=abs_data, relative_data=False, all_symbols=False, source=source)
    if global_vars.analyze_rel_yahoo:
        processor_filter_plot_data(data_list=rel_data, relative_data=True, all_symbols=False, source=source)
    if global_vars.analyze_rel_live_yahoo:
        processor_filter_plot_data(data_list=rel_data_live, relative_data=True, all_symbols=False, source=source)


def analyze_data_from_local_json_file(symbols: list, analyze_my_json_data_compare_companies: int):
    source = "my_json"

    if analyze_my_json_data_compare_companies:
        compare_companies(symbols, source)

    else:
        map(one_company_only, symbols)
