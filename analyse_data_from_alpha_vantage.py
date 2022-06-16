from PyPDF2 import PdfFileMerger
import glob
import os

import global_vars
from data_processor import processor_filter_plot_data
from functions_for_alpha_vantage import extract_quarterly_report_data_from_alpha
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import calculate_quotient, convert_list_elements_to_int, split_indicator_in_two, \
    read_data_from_file, get_data, get_key_value_from_local_file

# SWITCHES FOR ALPHA VANTAGE ANALYSIS
analyse_absolute_income_statement = 1
analyse_absolute_cash_flow = 1
analyse_percentage_income_statement = 1
analyze_percentage_balance_sheet = 1
analyse_live_with_income_statement = 1
analyse_live_with_balance_sheet = 1

analyse_absolute_my_json = 0
analyse_percentage_my_json = 0
analyse_live_with_my_json = 0

indicator_absolute_with_income_statement = ["netIncome",
                                            "totalRevenue"]
# , "grossProfit", "totalRevenue", "ebit", "incomeBeforeTax", "operatingIncome"

indicator_absolute_with_cash_flow = ["operatingCashflow", "changeInCashAndCashEquivalents"]

indicator_percentage_with_income_statement = [
    "netIncome_to_totalRevenue"]  # "researchAndDevelopment_to_totalRevenue"

indicator_percentage_with_balance_sheet = ["totalLiabilities_to_totalAssets",
                                           "totalCurrentLiabilities_to_totalCurrentAssets"]

indicator_live_with_income_statement = ["totalRevenue_to_marketCap"]


def pdf_merger():
    merger = PdfFileMerger()

    os.chdir("D:\\Desktop\\Finanzreporte\\financial_grafics")
    for file in glob.glob("*.pdf"):
        print(file)
        merger.append(file)

    merger.write("D:\\Desktop\\Finanzreporte\\financial_grafics\\result.pdf")
    merger.close()
    pass


def analyze_one_symbol(args):
    pass


def compare_companies(symbols, source):
    all_symbols_quaterly_absolute_data_with_income_statement = []
    all_symbols_quaterly_absolute_data_with_cash_flow = []

    all_symbols_quaterly_relative_percentage_with_balance_sheet = []
    all_symbols_quaterly_relative_percentage_with_income_statement = []

    all_symbols_quaterly_relative_live_data_with_balance_sheet = []
    all_symbols_quaterly_relative_live_data_with_income_statement = []
    all_symbols_quaterly_relative_live_data_with_my_json = []

    for s in symbols:

        if analyse_absolute_income_statement:

            income_statement = read_data_from_file(global_vars.filepath_alpha + "income_statement_alpha_" + s + ".json")

            for i in indicator_absolute_with_income_statement:
                try:
                    temp_data = extract_quarterly_report_data_from_alpha(income_statement, i, symbol=s)
                    all_symbols_quaterly_absolute_data_with_income_statement.append(temp_data)

                except BaseException:
                    print("error in quaterly data {}".format(s))

        if analyse_percentage_income_statement:

            income_statement = read_data_from_file(global_vars.filepath_alpha + "income_statement_alpha_" + s + ".json")

            for i in indicator_percentage_with_income_statement:

                try:
                    # extract data for every indicator
                    dividend, divisor = split_indicator_in_two(i)
                    dividend_data = get_data(income_statement, indicator=dividend, symbol=s)

                    divisor_data = get_data(income_statement, indicator=divisor, symbol=s)
                    quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                    temp_data = [dividend_data[0], quotient, s, i]

                    all_symbols_quaterly_relative_percentage_with_income_statement.append(temp_data)

                except:
                    print("-{}- calculate quotient of {} didnt work for".format(s, i))

        if analyse_absolute_cash_flow:

            cash_flow = read_data_from_file(global_vars.filepath_alpha + "cash_flow_alpha_" + s + ".json")

            for i in indicator_absolute_with_cash_flow:
                try:
                    temp_data = extract_quarterly_report_data_from_alpha(cash_flow, i, symbol=s)
                    all_symbols_quaterly_absolute_data_with_cash_flow.append(temp_data)

                except:
                    print("error in quaterly data {}".format(s))

        if analyze_percentage_balance_sheet:
            balance_sheet = read_data_from_file(global_vars.filepath_alpha + "balance_sheet_alpha_" + s + ".json")

            for i in indicator_percentage_with_balance_sheet:
                try:
                    dividend, divisor = split_indicator_in_two(i)
                    dividend_data = get_data(balance_sheet, indicator=dividend, symbol=s)

                    divisor_data = get_data(balance_sheet, indicator=divisor, symbol=s)
                    quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                    temp_data = [dividend_data[0], quotient, s, i]
                    all_symbols_quaterly_relative_percentage_with_balance_sheet.append(temp_data)

                except:
                    print("-{}- calculate quotient of {} didnt work".format(s, i))

        if analyse_live_with_income_statement:

            income_statement = read_data_from_file(global_vars.filepath_alpha + "income_statement_alpha_" + s + ".json")
            for i in indicator_live_with_income_statement:

                try:
                    dividend, divisor = split_indicator_in_two(i)
                    dividend_data = get_data(income_statement, indicator=dividend, symbol=s)

                    # wenn parameter vorhanden, dann hole dir aus file:
                    use_live_parameter = 1

                    if use_live_parameter == 1:

                        # try to get data live from yahooo
                        try:
                            marketCap = get_market_cap_from_yahoo_finance(s)

                        except:
                            marketCap = get_key_value_from_local_file("marketCap", s)
                        created_list = [marketCap] * len(dividend_data[1])
                        converted_list = convert_list_elements_to_int(created_list)

                        quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol="TEST")
                    else:
                        divisor_data = get_data(income_statement, indicator=divisor, symbol=s)
                        quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                    temp_data = [dividend_data[0], quotient, s, i]
                    all_symbols_quaterly_relative_live_data_with_income_statement.append(temp_data)


                except:
                    print("-{}- calculate quotient of {} didnt work".format(s, i))

        if analyse_live_with_balance_sheet:
            indicator_live_with_balance_sheet = ["totalAssets_to_marketCap"]

            balance_sheet = read_data_from_file(global_vars.filepath_alpha + "balance_sheet_alpha_" + s + ".json")
            counter = 0
            for i in indicator_live_with_balance_sheet:
                try:
                    dividend, divisor = split_indicator_in_two(i)
                    dividend_data = get_data(balance_sheet, indicator=dividend, symbol=s)

                    # wenn parameter vorhanden, dann hole dir aus file:
                    use_live_parameter = 1

                    if use_live_parameter == 1:
                        marketCap = get_market_cap_from_yahoo_finance(s)
                        created_list = [marketCap] * len(dividend_data[1])
                        converted_list = convert_list_elements_to_int(created_list)

                        quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol="TEST")
                    else:
                        divisor_data = get_data(balance_sheet, indicator=divisor, symbol=s)
                        quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                    temp_data = [dividend_data[0], quotient, s, i]

                    if counter < 1:
                        all_symbols_quaterly_relative_live_data_with_balance_sheet.append(temp_data)
                        counter = 1


                except:
                    print("-{}- calculate quotient of {} didnt work".format(s, i))

        if analyse_live_with_my_json:

            my_json_data = read_data_from_file(global_vars.filepath_my_json + s + ".json")

            counter = 0
            for i in indicator_live_with_income_statement:

                try:
                    dividend, divisor = split_indicator_in_two(i)
                    dividend_data = get_data(my_json_data, indicator=dividend, symbol=s)

                    # try to get data live from yahooo
                    try:
                        marketCap = get_market_cap_from_yahoo_finance(s)

                    except:
                        marketCap = get_key_value_from_local_file("marketCap", s)
                    created_list = [marketCap] * len(dividend_data[1])
                    converted_list = convert_list_elements_to_int(created_list)

                    quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol="TEST")

                    temp_data = [dividend_data[0], quotient, s, i]

                    if counter < 1:
                        all_symbols_quaterly_relative_live_data_with_my_json.append(temp_data)
                        counter = 1

                except:
                    print("-{}- calculate quotient of {} didnt work".format(s, i))

    if analyse_absolute_income_statement == 1:
        processor_filter_plot_data(all_symbols_quaterly_absolute_data_with_income_statement, False, True, source)

    if analyse_absolute_cash_flow == 1:
        processor_filter_plot_data(all_symbols_quaterly_absolute_data_with_cash_flow, False, True, source)

    if analyze_percentage_balance_sheet == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_percentage_with_balance_sheet, True, True, source)
    if analyse_percentage_income_statement == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_percentage_with_income_statement, True, True, source)

    if analyse_live_with_balance_sheet == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_live_data_with_balance_sheet, True, True, source)
    if analyse_live_with_income_statement == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_live_data_with_income_statement, True, True, source)

    if analyse_live_with_my_json == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_live_data_with_my_json, True, True, source)

    pass


def one_company_only(symbol):
    s = symbol
    quaterly_absolute_data_per_symbol = []
    quaterly_relative_data_per_symbol = []

    if analyse_absolute_income_statement:

        income_statement = read_data_from_file(global_vars.filepath_alpha + "income_statement_alpha_" + s + ".json")

        counter = 0
        for i in indicator_absolute_with_income_statement:
            try:
                temp_data = extract_quarterly_report_data_from_alpha(income_statement, i, symbol=s)
                quaterly_absolute_data_per_symbol.append(temp_data)
            except:
                print("error in quaterly data {}".format(s))

    if analyse_percentage_income_statement:

        income_statement = read_data_from_file(global_vars.filepath_alpha + "income_statement_alpha_" + s + ".json")

        counter = 0
        for i in indicator_percentage_with_income_statement:

            try:
                # extract data for every indicator
                dividend, divisor = split_indicator_in_two(i)
                dividend_data = get_data(income_statement, indicator=dividend, symbol=s)

                divisor_data = get_data(income_statement, indicator=divisor, symbol=s)
                quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                temp_data = [dividend_data[0], quotient, s, i]

                quaterly_relative_data_per_symbol.append(temp_data)


            except:
                print("-{}- calculate quotient of {} didnt work for".format(s, i))

    if analyse_absolute_cash_flow:

        cash_flow = read_data_from_file(global_vars.filepath_alpha + "cash_flow_alpha_" + s + ".json")

        counter = 0
        for i in indicator_absolute_with_cash_flow:
            try:
                temp_data = extract_quarterly_report_data_from_alpha(cash_flow, i, symbol=s)
                quaterly_absolute_data_per_symbol.append(temp_data)

            except:
                print("error in quaterly data {}".format(s))

    if analyze_percentage_balance_sheet:
        balance_sheet = read_data_from_file(global_vars.filepath_alpha + "balance_sheet_alpha_" + s + ".json")

        counter = 0

        for i in indicator_percentage_with_balance_sheet:
            try:
                dividend, divisor = split_indicator_in_two(i)
                dividend_data = get_data(balance_sheet, indicator=dividend, symbol=s)

                divisor_data = get_data(balance_sheet, indicator=divisor, symbol=s)
                quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                temp_data = [dividend_data[0], quotient, s, i]

                quaterly_relative_data_per_symbol.append(temp_data)
            except:
                print("-{}- calculate quotient of {} didnt work".format(s, i))

    quaterly_relative_live_data_per_symbol = []

    if analyse_live_with_income_statement:

        income_statement = read_data_from_file(global_vars.filepath_alpha + "income_statement_alpha_" + s + ".json")
        counter = 0
        for i in indicator_live_with_income_statement:

            try:
                dividend, divisor = split_indicator_in_two(i)
                dividend_data = get_data(income_statement, indicator=dividend, symbol=s)

                # wenn parameter vorhanden, dann hole dir aus file:
                use_live_parameter = 1

                if use_live_parameter == 1:

                    # try to get data live from yahooo
                    try:
                        marketCap = get_market_cap_from_yahoo_finance(s)

                    except:
                        marketCap = get_key_value_from_local_file("marketCap", s)
                    created_list = [marketCap] * len(dividend_data[1])
                    converted_list = convert_list_elements_to_int(created_list)

                    quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol="TEST")
                else:
                    divisor_data = get_data(income_statement, indicator=divisor, symbol=s)
                    quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                temp_data = [dividend_data[0], quotient, s, i]

                quaterly_relative_live_data_per_symbol.append(temp_data)

            except:
                print("-{}- calculate quotient of {} didnt work".format(s, i))

    if analyse_live_with_balance_sheet:
        indicator_live_with_balance_sheet = ["totalAssets_to_marketCap"]

        balance_sheet = read_data_from_file(global_vars.filepath_alpha + "balance_sheet_alpha_" + s + ".json")
        counter = 0
        for i in indicator_live_with_balance_sheet:
            try:
                dividend, divisor = split_indicator_in_two(i)
                dividend_data = get_data(balance_sheet, indicator=dividend, symbol=s)

                # wenn parameter vorhanden, dann hole dir aus file:
                use_live_parameter = 1

                if use_live_parameter == 1:
                    marketCap = get_market_cap_from_yahoo_finance(s)
                    created_list = [marketCap] * len(dividend_data[1])
                    converted_list = convert_list_elements_to_int(created_list)

                    quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol="TEST")
                else:
                    divisor_data = get_data(balance_sheet, indicator=divisor, symbol=s)
                    quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                temp_data = [dividend_data[0], quotient, s, i]

                quaterly_relative_live_data_per_symbol.append(temp_data)

            except:
                print("-{}- calculate quotient of {} didnt work".format(s, i))

    source = "alpha_vantage"

    if len(quaterly_relative_data_per_symbol) != 0:
        processor_filter_plot_data(quaterly_relative_data_per_symbol, True, False, source)
    if len(quaterly_absolute_data_per_symbol) != 0:
        processor_filter_plot_data(quaterly_absolute_data_per_symbol, False, False, source)
    if len(quaterly_relative_live_data_per_symbol) != 0:
        processor_filter_plot_data(quaterly_relative_live_data_per_symbol, True, False, source)

    pass


def analyze_data_from_alpha_vantage(symbols: list, analyze_alpha_data_compare_companies: int):
    if type(symbols) is not list:
        raise Exception("IncorrectParameter. List as parameter type is expected")

    if analyze_alpha_data_compare_companies:
        compare_companies(symbols, "alpha_vantage")

    else:
        map(one_company_only, symbols)

    pass
