import global_vars
from data_processor import processor_filter_plot_data
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import read_data_from_file, split_indicator_in_two, calculate_quotient, \
    extract_quarterly_report_data_from_my_json_file, get_float_data, \
    get_key_value_from_local_file

analyse_abs_indicator = 1
analyse_rel_indicator = 0
analyse_rel_live_indicator = 1


def compare_companies(symbol, source="my_json"):
    # TODO - see alpha vantage implementation
    pass


def one_company_only(symbol, source="my_json"):
    data = read_data_from_file(global_vars.filepath_my_json + symbol + ".json")

    ''' 
    my indicators for finnhub and alpha vantage indiactors I want to analyse from the json file
    my_abs_indicators = #,"totalRevenue", "grossProfit", "operatingIncome", "ebit", "netIncome"
    my_rel_indicators = ["researchAndDevelopment_to_totalRevenue", "operatingIncome_to_totalRevenue",
                         "totalLiabilities_to_totalAssets", "totalCurrentLiabilities_to_totalCurrentAssets",
                         "grossProfit_to_totalRevenue",
                         ]  # , "totalShareholdersEquity_to_totalAssets" == ,"totalAssets_minus_totalLiabilities"
    '''
    abs_indicators = ["TotalAssets"]
    rel_indicators = ["TotalLiab_to_TotalAssets", "TotalCurrentLiab_to_TotalCurrentAssets"]
    my_rel_indicators_live = ["marketCap_to_TotalAssets",
                              "marketCap_to_TotalLiab"]  # "marketCap_to_totalRevenue", ,"marketCap_to_netIncome"

    abs_data = []
    if analyse_abs_indicator == 1:
        for i in abs_indicators:
            extracted_data = extract_quarterly_report_data_from_my_json_file(data_json=data, indicator=i, symbol=symbol)
            abs_data.append(extracted_data)

    rel_data = []
    if analyse_rel_indicator == 1:
        for i in rel_indicators:
            dividend, divisor = split_indicator_in_two(i)
            dividend_data = get_float_data(data, indicator=dividend, symbol=symbol)

            divisor_data = get_float_data(data, indicator=divisor, symbol=symbol)
            quotient = calculate_quotient(dividend_data[1], divisor_data[1])

            temp_data = [dividend_data[0], quotient, symbol, i]
            rel_data.append(temp_data)

    rel_data_live = []
    if analyse_rel_live_indicator == 1:
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
