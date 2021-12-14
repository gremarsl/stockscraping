from data_processor import processor_filter_plot_data
from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, \
    get_one_relative_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub, calling_finnhub_api
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import get_data_from_file, convert_list_elements_to_int, split_indicator_in_two, \
    calculate_quotient, get_data
from functions_for_alpha_vantage import \
    extract_quarterly_report_data_from_alpha, \
    calling_alpha_vantage_api


# Understand JSON
# object: {}
# array : []

def analyse_data_from_alpha_vantage(symbols: list):
    # define the indicators you want to analyse with alpha vantage data:

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


def analyse_data_from_finnhub(symbols : list):
    source = "finnhub"
    all_plot_data = []

    period = 'quarterly'

    for s in symbols:
        data_per_symbol = []

        #new:
        fundamental_data_json = get_data_from_file("fundamental_data_finnhub_" + s + ".json")

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
analyse_own_excel_data = 0
get_finnhub_data = 0
analyse_finnhub_data = 1
get_alpha_data = 0
analyse_alpha_data = 0

analyse_finnhub_symbol_automotive = ["DAI.DE","BMW.DE","VOW.DE", "PAH3.DE"]

get_finnhub_symbol_dax = ["BAS.DE","SIE.DE","BAYN.DE","IFX.DE","1COV.DE", "LIN.DE","BEI.DE","HEN3.DE"] # ALV.DE, "DBK.DE",
get_finnhub_symbol_dax = ["BAS.DE"]
analyse_finnhub_symbol_dax = ["DAI.DE","BMW.DE","VOW.DE", "PAH3.DE"] # ALV.DE, "DBK.DE",


get_alpha_vantage_symbol_data = ["SNPS"]
analyse_alpha_vantage_symbol_data = ["JNJ","PRG","PFE","AMD","MSFT","AVGO", "AAPL"]
#get_symbol_data_alpha_vantage = ["SNPS","MRVL","AMBA","QCOM","ZS","ASML","NVDA","TEAM"]  # "IBM", "AAPL"
#symbols work: "JNJ","PRG","PFE","AMD","MSFT","AVGO", "AAPL"

# a8b qci raus
#funktioniert: JNJ - PRG - PFE -
#TODO current ratio einbauen

if __name__ == '__main__':
    if analyse_own_excel_data == 1:
        analyse_data_from_local_json_file()

    if get_finnhub_data == 1:
        calling_finnhub_api(get_finnhub_symbol_dax)

    if analyse_finnhub_data == 1:
        analyse_data_from_finnhub(analyse_finnhub_symbol_dax)

    if get_alpha_data == 1:
        calling_alpha_vantage_api(get_alpha_vantage_symbol_data)

    if analyse_alpha_data == 1:
        analyse_data_from_alpha_vantage(analyse_alpha_vantage_symbol_data)
