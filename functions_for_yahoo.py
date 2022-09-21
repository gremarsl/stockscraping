import csv

import yfinance as yf
import global_vars
from general_functions import write_to_file_in_json_format, write_to_file_in_csv_format, create_json_object_finance, \
    append_key_value_to_object


def calculate_dax_to_gdp_germany():
    if global_vars.calculate_dax == 1 and len(global_vars.dax_40) == 40:
        companies = global_vars.dax_40

        list_of_market_cap = list(map(get_market_cap_from_yahoo_finance, companies))
        print(list_of_market_cap)

        latest_sum_market_cap = sum(list_of_market_cap)
        latest_sum_market_cap = latest_sum_market_cap / 1000000000  # now it is billion
        print(latest_sum_market_cap)

        latest_dax_value = get_index_value_from_yahoo_finance("^GDAXI")

        factor_sum_market_cap = latest_sum_market_cap / global_vars.germany_gdp
        factor_latest_dax_value = latest_dax_value / global_vars.germany_gdp

        print(
            f"The quotient sum of market cap from all DAX40 to last Germany Gross Domestic Product (GDP) number is: {factor_sum_market_cap}")
        print(
            f"The quotient latest_dax_value to last Germany Gross Domestic Product (GDP) number is: {factor_latest_dax_value}")


def calculate_sp_500_to_gdp_usa():
    if global_vars.calculate_sp500 == 1:
        price = get_index_value_from_yahoo_finance("^GSPC")
        valuation = price * global_vars.sp_500_divisor / 1000  # now it is in unit: trillion
        print(f"The latest valuation of S&P 500 is: {valuation} Trillion US-Dollar ")

        factor = valuation / global_vars.usa_gdp
        print(f"The quotient S&P 500 to last US Gross Domestic Product (GDP) number is: {factor}")


def get_earnings(base, symbol: str):
    balance = base.balance_sheet

    balance_csv = balance.to_csv()

    name_of_file_csv = "yahoo_balance_" + symbol + ".csv"

    write_to_file_in_csv_format(balance_csv, name_of_file_csv)

    file = open(name_of_file_csv)

    header = []
    csvreader = csv.reader(file)
    header = next(csvreader)

    # remove list elements which are empty
    header = list(filter(None, header))

    # extract rows and filter empty lists from the base list
    rows = []
    for row in csvreader:
        rows.append(row)

    rows = list(filter(None, rows))

    # remove spaces from indicators
    new_rows = []
    for row in rows:
        row_stripped = row[0].replace(" ", "")

        row[0] = row_stripped

    # create basic financial json object
    basic_object = create_json_object_finance(symbol)

    # zugriff auf das array vom basic object
    output_quarter_array = basic_object["quarterlyReports"]

    # zusammenbau des objects
    quater_idx = 0
    for quater in header:
        object = {}

        append_key_value_to_object(object, "fiscalDateEnding", header[quater_idx])

        for row in rows:
            append_key_value_to_object(object, row[0], row[quater_idx + 1])

        # hinzufügen des objects zu dem array
        output_quarter_array.append(object)

        quater_idx += 1

    name_of_file_json = "yahoo_balance_" + symbol + ".json"
    write_to_file_in_json_format(basic_object, name_of_file_json)

    return balance


def stub():
    base = get_base_ticker_from_yahoo_finance("MSFT")

    earnings = get_earnings(base, "MSFT")


def get_base_ticker_from_yahoo_finance(symbol):
    try:
        symbol_base = yf.Ticker("MSFT")

    except:
        print(f"yf.Ticker failed for symbol: {symbol}")

    return symbol_base


def get_info_from_yahoo_finance(symbol):
    try:
        try:
            symbol_base = yf.Ticker(symbol)

            name_of_ticker_file = "yahoo_ticker_data_" + symbol + ".json"

            write_to_file_in_json_format(symbol_base, name_of_ticker_file)
        except:
            print(f"yf.Ticker failed for symbol: {symbol}")
        symbol_info = symbol_base.info

        name_of_info_file = "yahoo_info_data_" + symbol + ".json"

        write_to_file_in_json_format(symbol_info, name_of_info_file)
    except:
        print(f"get_base_info_from_yahoo_finance failed for symbol: {symbol}")

    return symbol_info


def get_last_price_for_symbol_from_yahoo_finance(symbol):
    ticker_yahoo = yf.Ticker(symbol)
    data = ticker_yahoo.history()
    last_quote = (data.tail(1)['Close'].iloc[0])

    return last_quote


def get_market_cap_from_yahoo_finance(symbol):
    try:
        symbol_info = get_info_from_yahoo_finance(symbol)

    except:
        print(f"get_market_cap_from_yahoo_finance failed for symbol: {symbol}")

    try:
        market_cap = symbol_info["marketCap"]

        if market_cap is None:
            print(f"not data for market_cap - since None was returned for symbol {symbol}")

    except:
        print(f"The call symbol_info[marketCap] failed for symbol: {symbol}")

    return market_cap


def get_index_value_from_yahoo_finance(symbol):
    try:
        symbol_info = get_info_from_yahoo_finance(symbol)

    except:
        print(f"get_index_value_from_yahoo_finance failed for symbol: {symbol}")

    price = symbol_info["regularMarketPrice"]

    return price
