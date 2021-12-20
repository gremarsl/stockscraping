from data_processor import processor_filter_plot_data
from functions_for_alpha_vantage import extract_quarterly_report_data_from_alpha
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import get_data_from_file, split_indicator_in_two, calculate_quotient, \
    convert_list_elements_to_int, get_data


def analyse_data_from_local_json_file():
    filename = "D:\\Desktop\\Finanzreporte\\json\\testsymbol.json"
    s = "TEST"
    data = get_data_from_file(filename)

    # my indicators I want to analyse from the json file

    # TODO switch on and off these indicators
    my_abs_indicators = ["totalRevenue", "netIncome"]
    my_rel_indicators = ["researchAndDevelopment_to_totalRevenue", "totalLiabilities_to_totalAssets"]
    my_rel_indicators_live = ["totalRevenue_to_marketCap", "totalAssets_to_marketCap"]

    abs_data = []
    for i in my_abs_indicators:
        extracted_data = extract_quarterly_report_data_from_alpha(data_json=data, indicator=i, symbol="TEST")
        abs_data.append(extracted_data)

    rel_data = []
    for i in my_rel_indicators:
        dividend, divisor = split_indicator_in_two(i)
        dividend_data = get_data(data, indicator=dividend, symbol=s)

        divisor_data = get_data(data, indicator=divisor, symbol=s)
        quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

        temp_data = [dividend_data[0], quotient, s, i]

        rel_data.append(temp_data)

    rel_data_live = []
    for i in my_rel_indicators_live:
        dividend, divisor = split_indicator_in_two(i)
        dividend_data = get_data(data, indicator=dividend, symbol="TEST")

        # wenn parameter vorhanden, dann hole dir aus file:
        use_live_parameter = True

        if not use_live_parameter:
            return_data2 = get_data(data, indicator=divisor, symbol="TEST")
            quotient = calculate_quotient(dividend_data[1], return_data2[1], i, symbol="TEST")

        if use_live_parameter:
            marketCap = get_market_cap_from_yahoo_finance("DAI.DE")
            created_list = [marketCap] * len(dividend_data[1])
            converted_list = convert_list_elements_to_int(created_list)

            quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol="TEST")

        # add another list around to make it work
        temp_data = [dividend_data[0], quotient, "TEST", i]
        rel_data_live.append(temp_data)

    # plotdata
    source = "excel"
    processor_filter_plot_data(data_list=abs_data, relative_data=False, all_symbols=True, source=source)
    processor_filter_plot_data(data_list=rel_data, relative_data=True, all_symbols=True, source=source)
    processor_filter_plot_data(data_list=rel_data_live, relative_data=True, all_symbols=True, source=source)

    pass

