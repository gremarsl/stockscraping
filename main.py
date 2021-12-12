import options
from data_processor import processor_filter_plot_data
from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, get_fundamental_data_from_finnhub, \
    get_one_relative_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import get_data_from_file, filter_data, convert_list_elements_to_int, split_indicator_in_two, \
    calculate_quotient, get_data
from plot_functions import stupid_plot_data_lists
from functions_for_alpha_vantage import \
    extract_quarterly_report_data_from_alpha, \
    calling_alpha_vantage_api


# Understand JSON
# object: {}
# array : []



def analyse_data_from_alpha_vantage(symbols: list):

    #define the indicators you want to analyse with alpha vantage data:

    indicator_absolute_with_income_statement = ["grossProfit", "totalRevenue", "ebit", "netIncome", "incomeBeforeTax",
                                           "operatingIncome"]
    indicator_percentage_with_income_statement = ["researchAndDevelopment_to_totalRevenue", "netIncome_to_totalRevenue"]

    indicator_percentage_with_balance_sheet = ["totalLiabilities_to_totalAssets"]

    for s in symbols:

        quaterly_absolute_data_per_symbol = []
        quaterly_relative_data_per_symbol = []
        income_statement = get_data_from_file("income_statement_alpha_" + s + ".json")


        for i in indicator_absolute_with_income_statement:
            try:
                quaterly_absolute_data_per_symbol.append(
                    extract_quarterly_report_data_from_alpha(income_statement, i, symbol=s))
            except:
                print("error in quaterly data {}".format(s))


        for i in indicator_percentage_with_income_statement:

            try:
                dividend, divisor = split_indicator_in_two(i)
                dividend_data = get_data(income_statement, indicator=dividend, symbol=s)

                divisor_data = get_data(income_statement, indicator=divisor, symbol=s)
                quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                temp_data = [dividend_data[0], quotient, s, i]

                quaterly_relative_data_per_symbol.append(temp_data)

            except:
                print(
                    "calculate quotient of {} didint work".format(i))

        balance_sheet = get_data_from_file("balance_sheet_alpha_" + s + ".json")


        for i in indicator_percentage_with_balance_sheet:

            try:
                dividend, divisor = split_indicator_in_two(i)
                dividend_data = get_data(balance_sheet, indicator=dividend, symbol=s)

                divisor_data = get_data(balance_sheet, indicator=divisor, symbol=s)
                quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                temp_data = [dividend_data[0], quotient, s, i]

                quaterly_relative_data_per_symbol.append(temp_data)

            except:
                print(
                    "calculate quotient of {} didint work".format(i))

        source = "alpha_vantage"
        processor_filter_plot_data(quaterly_relative_data_per_symbol, True, source)
        processor_filter_plot_data(quaterly_absolute_data_per_symbol, False, source)

    pass


def get_data_from_finnhub():
    source = "finnhub"
    all_plot_data = []
    all_plot_data_test = []

    period = 'quarterly'

    symbol_dax_stocks = ["BAS.DE",
                         "SIE.DE",
                         "BAYN.DE",
                         "IFX.DE",
                         "1COV.DE",
                         "LIN.DE",
                         "BEI.DE",
                         "HEN3.DE",
                         ]
    # ALV.DE, "DBK.DE",

    automotive_dax_stocks = ["DAI.DE",
                             "BMW.DE",
                             "VOW.DE"]
    test_symbol = ["BAS.DE"]

    for s in automotive_dax_stocks:
        data_per_symbol = []

        fundamental_data_json = get_fundamental_data_from_finnhub(s)

        indicator_absolute_list = ["grossMargin"]  # netMargin
        indicators_per_share = ["eps", "ebitPerShare"]
        indicators_ratio = ["cashRatio", "currentRatio"]
        indicators_percentage = ["totalDebtToEquity"]

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

        processor_filter_plot_data(data_per_symbol, relativeData=False, source=source)
        all_plot_data.append(data_per_symbol)


def analyse_data_from_local_json_file():
    filename = "D:\\Desktop\\Finanzreporte\\json\\testsymbol.json"
    s = "TEST"
    data = get_data_from_file(filename)

    # my indicators I want to analyse from the json file
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
    processor_filter_plot_data(data_list=abs_data, relativeData=False, source=source)
    processor_filter_plot_data(data_list=rel_data, relativeData=True, source=source)
    processor_filter_plot_data(data_list=rel_data_live, relativeData=True, source=source)

    pass


# SWITCHES:
analyse_own_excel_data = 1
analyse_finnhub_data = 0
get_alpha_data = 0
analyse_alpha_data = 1
alpha_vantage_symbols = ["AVGO","AAPL"]  # "IBM", "AAPL"



#TODO - Improve my stock analysis in general / in total

if __name__ == '__main__':
    if analyse_own_excel_data == 1:
        analyse_data_from_local_json_file()

    if analyse_finnhub_data == 1:
        get_data_from_finnhub()

    if get_alpha_data == 1:
        calling_alpha_vantage_api(alpha_vantage_symbols)

    if analyse_alpha_data == 1:
        analyse_data_from_alpha_vantage(alpha_vantage_symbols)
