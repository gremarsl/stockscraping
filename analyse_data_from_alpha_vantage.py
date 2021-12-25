from data_processor import processor_filter_plot_data
from functions_for_alpha_vantage import extract_quarterly_report_data_from_alpha
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import calculate_quotient, convert_list_elements_to_int, split_indicator_in_two, \
    get_data_from_file, get_data

# SWITCHES FOR ALPHA VANTAGE ANALYSIS
analyze_absolute_income_statement = 1
analyze_percentage_income_statement = 1
analyze_percentage_balance_sheet = 1
analyze_live_with_income_statement = 1
analyze_live_with_balance_sheet = 1

indicator_absolute_with_income_statement = ["netIncome", "totalRevenue", "grossProfit", "ebit",
                                            "incomeBeforeTax", "operatingIncome"]

indicator_percentage_with_income_statement = [
    "netIncome_to_totalRevenue"]  # "researchAndDevelopment_to_totalRevenue"

indicator_percentage_with_balance_sheet = ["totalLiabilities_to_totalAssets",
                                           "totalCurrentLiabilities_to_totalCurrentAssets"]

indicator_live_with_income_statement = ["totalRevenue_to_marketCap"]


def analyse_data_from_alpha_vantage(symbols: list, analyze_only_all_companies: int):
    # TODO all symbols one indicator - in the list with more than one indicator -> e.g. 2 indicator -> I get 10
    #  graphs in the plot. Only one indicator is allowed -> need to be more modularized

    all_symbols_quaterly_absolute_data_with_income_statement = []

    all_symbols_quaterly_relative_percentage_with_balance_sheet = []
    all_symbols_quaterly_relative_percentage_with_income_statement = []

    all_symbols_quaterly_relative_live_data_with_income_statement = []
    all_symbols_quaterly_relative_live_data_with_balance_sheet = []

    for s in symbols:

        quaterly_absolute_data_per_symbol = []
        quaterly_relative_data_per_symbol = []

        if analyze_absolute_income_statement:

            income_statement = get_data_from_file("income_statement_alpha_" + s + ".json")

            counter = 0
            for i in indicator_absolute_with_income_statement:
                try:
                    temp_data = extract_quarterly_report_data_from_alpha(income_statement, i, symbol=s)
                    quaterly_absolute_data_per_symbol.append(temp_data)

                    if analyze_only_all_companies == 1:
                        if counter < 1:
                            all_symbols_quaterly_absolute_data_with_income_statement.append(temp_data)
                            counter = counter + 1

                except:
                    print("error in quaterly data {}".format(s))

        if analyze_percentage_income_statement:

            income_statement = get_data_from_file("income_statement_alpha_" + s + ".json")

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
                    all_symbols_quaterly_relative_percentage_with_income_statement.append(temp_data)


                except:
                    print("-{}- calculate quotient of {} didnt work for".format(s, i))

        if analyze_percentage_balance_sheet:

            balance_sheet = get_data_from_file("balance_sheet_alpha_" + s + ".json")

            counter = 0

            for i in indicator_percentage_with_balance_sheet:

                try:
                    dividend, divisor = split_indicator_in_two(i)
                    dividend_data = get_data(balance_sheet, indicator=dividend, symbol=s)

                    divisor_data = get_data(balance_sheet, indicator=divisor, symbol=s)
                    quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                    temp_data = [dividend_data[0], quotient, s, i]

                    quaterly_relative_data_per_symbol.append(temp_data)

                    if counter < 1:
                        all_symbols_quaterly_relative_percentage_with_balance_sheet.append(temp_data)
                        counter = 1

                except:
                    print("-{}- calculate quotient of {} didnt work".format(s, i))

        quaterly_relative_live_data_per_symbol = []

        if analyze_live_with_income_statement:

            income_statement = get_data_from_file("income_statement_alpha_" + s + ".json")
            counter = 0
            for i in indicator_live_with_income_statement:

                try:
                    dividend, divisor = split_indicator_in_two(i)
                    dividend_data = get_data(income_statement, indicator=dividend, symbol=s)

                    # wenn parameter vorhanden, dann hole dir aus file:
                    use_live_parameter = 1

                    if use_live_parameter == 1:
                        marketCap = get_market_cap_from_yahoo_finance(s)
                        created_list = [marketCap] * len(dividend_data[1])
                        converted_list = convert_list_elements_to_int(created_list)

                        quotient = calculate_quotient(dividend_data[1], converted_list, i, symbol="TEST")
                    else:
                        divisor_data = get_data(income_statement, indicator=divisor, symbol=s)
                        quotient = calculate_quotient(dividend_data[1], divisor_data[1], i, symbol=s)

                    temp_data = [dividend_data[0], quotient, s, i]

                    quaterly_relative_live_data_per_symbol.append(temp_data)

                    if counter < 1:
                        all_symbols_quaterly_relative_live_data_with_income_statement.append(temp_data)
                        counter = 1


                except:
                    print("-{}- calculate quotient of {} didnt work".format(s, i))

        if analyze_live_with_balance_sheet:
            indicator_live_with_balance_sheet = ["totalAssets_to_marketCap"]

            balance_sheet = get_data_from_file("balance_sheet_alpha_" + s + ".json")
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

                    if counter < 1:
                        all_symbols_quaterly_relative_live_data_with_balance_sheet.append(temp_data)
                        counter = 1


                except:
                    print("-{}- calculate quotient of {} didnt work".format(s, i))

        source = "alpha_vantage"

        if analyze_only_all_companies != 1:
            if len(quaterly_relative_data_per_symbol) != 0:
                processor_filter_plot_data(quaterly_relative_data_per_symbol, True, False, source)
            if len(quaterly_relative_data_per_symbol) != 0:
                processor_filter_plot_data(quaterly_absolute_data_per_symbol, False, False, source)
            if len(quaterly_relative_live_data_per_symbol) != 0:
                processor_filter_plot_data(quaterly_relative_live_data_per_symbol, True, False, source)

    source = "alpha_vantage"

    if analyze_absolute_income_statement == 1 and analyze_only_all_companies == 1:
        processor_filter_plot_data(all_symbols_quaterly_absolute_data_with_income_statement, False, True, source)

    if analyze_percentage_balance_sheet == 1 and analyze_only_all_companies == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_percentage_with_balance_sheet, True, True, source)
    if analyze_percentage_income_statement == 1 and analyze_only_all_companies == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_percentage_with_income_statement, True, True, source)

    if analyze_live_with_balance_sheet == 1 and analyze_only_all_companies == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_live_data_with_balance_sheet, True, True, source)
    if analyze_live_with_income_statement == 1 and analyze_only_all_companies == 1:
        processor_filter_plot_data(all_symbols_quaterly_relative_live_data_with_income_statement, True, True, source)
    pass
