import os
from time import strftime, gmtime
import json
import pandas as pd
import requests
import json

from general_functions import write_to_file_in_json_format, reverse_lists
import time

from keys import api_key_alpha


def calling_alpha_vantage_api(symbols):
    # 'https://finnhub.io/api/v1/stock/metric?symbol=DAI.DE&metric=all&token=buk3id748v6r2017iuog'

    for s in symbols:
        income_statement = request_income_statement_from_alpha(s)
        balance_sheets = request_balance_sheet_from_alpha(s)
        cash_flow = request_cash_flow_from_alpha(s)
        earnings = request_earnings_from_alpha(s)
        overview = request_overiew_from_alpha(s)

        print("Going to sleep for 60 Seconds now...")
        time.sleep(60)


def request_overiew_from_alpha(symbol):
    API_URL = "https://www.alphavantage.co/query?"

    data = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": api_key_alpha}

    response = requests.get(API_URL, data)

    fundamental_data_response_json = response.json()  # maybe redundant

    name_of_file = "fundamental_alpha_data_" + symbol + ".json"
    # print(fundamental_data_response_json) # this is of type: <class 'dict'>

    write_to_file_in_json_format(fundamental_data_response_json, name_of_file)

    return fundamental_data_response_json


def append_line_to_file_and_save(line: str, filename: str):
    test_filename = "test.csv"
    if os.path.isfile(filename):
        with open(filename, "a") as file_object:
            file_object.write(str(line))
            file_object.write("\n")

    else:
        # create file and print ebitda_list to first line
        with open(filename, "w") as file_object:
            file_object.write("symbol;indicator;date\n")

        # append line
        with open(filename, "a") as file_object:
            # Append 'hello' at the end of file
            file_object.write(str(line))
            file_object.write("\n")


def long_term_data_get_ebitda(data_json: dict, symbol) -> list:
    indicator_ebitda = "EBITDA"
    ebitda_value = data_json['EBITDA']
    time_and_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    data = [symbol, indicator_ebitda, ebitda_value, time_and_date]

    filename = "long_term_data_alpha_data_{}.csv".format(symbol)

    append_line_to_file_and_save(str(data), filename)
    return data


def long_term_data_get_price_to_earning_ratio(data_json: dict, symbol: str) -> list:
    indicator = "PERatio"

    price_to_earning_ratio = data_json['PERatio']
    time_and_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    data = [symbol, indicator, price_to_earning_ratio, time_and_date]

    filename = "long_term_data_alpha_data_{}.csv".format(symbol)

    append_line_to_file_and_save(str(data), filename)

    return data


def request_time_income_data_from_alpha(symbol):
    API_URL = "https://www.alphavantage.co/query?"

    data = {
        "function": "INCOME_STATEMENT",
        "symbol": symbol,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": api_key_alpha}

    response = requests.get(API_URL, data)

    fundamental_data_response_json = response.json()  # maybe redundant

    df = pd.DataFrame(fundamental_data_response_json['annualReports'])
    df.set_index('fiscalDateEnding', inplace=True)


def request_time_series_daily_data_from_alpha(symbol):
    API_URL = "https://www.alphavantage.co/query?"

    data = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": api_key_alpha}

    response = requests.get(API_URL, data)

    fundamental_data_response_json = response.json()  # maybe redundant
    df = pd.DataFrame.from_dict(fundamental_data_response_json['Time Series (Daily)'], orient='index')
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')

    df = df.rename(
        columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close',
                 '5. volume': 'Volume'})
    df = df.astype(
        {'Open': 'float64', 'High': 'float64', 'Low': 'float64', 'Close': 'float64', 'Volume': 'float64', })
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    pass


def request_symbol_search_from_alpha(keywords):
    # https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=PORSCHE&apikey=X90PH4C1TIFJA4MP
    api_url = "https://www.alphavantage.co/query?"

    data = {
        "function": "SYMBOL_SEARCH",
        "keywords": keywords,
        "apikey": api_key_alpha}

    response_json = requests.get(api_url, data).json()

    print('----------')
    print(response_json)
    print('----------')

    # XETRA:
    # Porsche: 	"PAH3.DEX", "Porsche Automobil Holding SE"
    # HENKEL HEN3.DEX

    # SAP = SAP
    # Deutsche Bank: DB
    #


def request_income_statement_from_alpha(symbol):
    # https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=HENKY&apikey=X90PH4C1TIFJA4MP

    API_URL = "https://www.alphavantage.co/query?"
    filename = "income_statement_alpha_" + symbol + ".json"

    input = {
        "function": "INCOME_STATEMENT",
        "symbol": symbol,
        "apikey": api_key_alpha}

    if os.path.isfile(filename):
        with open(filename) as json_file:
            income_statement = json.load(json_file)

    else:
        response = requests.get(API_URL, input)

        income_statement = response.json()  # maybe redundant

    write_to_file_in_json_format(income_statement, filename)

    return income_statement


def request_balance_sheet_from_alpha(symbol):
    # https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=demo

    API_URL = "https://www.alphavantage.co/query?"
    filename = "balance_sheet_alpha_" + symbol + ".json"

    input = {
        "function": "BALANCE_SHEET",
        "symbol": symbol,
        "apikey": api_key_alpha}

    if os.path.isfile(filename):
        with open(filename) as json_file:
            balance_sheet = json.load(json_file)

    else:
        response = requests.get(API_URL, input)
        balance_sheet = response.json()  # maybe redundant

    print(balance_sheet)

    write_to_file_in_json_format(balance_sheet, filename)

    return balance_sheet


def request_cash_flow_from_alpha(symbol):
    # https://www.alphavantage.co/query?function=CASH_FLOW&symbol=VLDR&apikey=X90PH4C1TIFJA4MP
    API_URL = "https://www.alphavantage.co/query?"
    filename = "cash_flow_alpha_" + symbol + ".json"

    input = {
        "function": "CASH_FLOW",
        "symbol": symbol,
        "apikey": api_key_alpha}

    if os.path.isfile(filename):
        with open(filename) as json_file:
            cash_flow = json.load(json_file)

    else:
        response = requests.get(API_URL, input)

        cash_flow = response.json()  # maybe redundant
    print(cash_flow)

    write_to_file_in_json_format(cash_flow, filename)
    pass


def request_earnings_from_alpha(symbol):
    # https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=demo
    API_URL = "https://www.alphavantage.co/query?"
    filename = "earnings_alpha_" + symbol + ".json"

    input = {
        "function": "EARNINGS",
        "symbol": symbol,
        "apikey": api_key_alpha}
    if os.path.isfile(filename):
        with open(filename) as json_file:
            earnings = json.load(json_file)

    else:
        response = requests.get(API_URL, input)

        earnings = response.json()  # maybe redundant
    print(earnings)

    write_to_file_in_json_format(earnings, filename)
    pass


def get_annual_report_alpha(data_json: dict, indicator: str, symbol: str) -> list:
    reports = data_json['annualReports']
    time_points = []
    value_points = []
    for i in reports:
        # i ist ein  Array
        time_points.append(i['fiscalDateEnding'])
        value_points.append(i[indicator])

    value_points, time_points = reverse_lists(value_points, time_points)

    data = [time_points, value_points, symbol, indicator]

    return data


def get_quaterly_report_alpha(data_json: dict, indicator: str, symbol: str) -> list:
    reports = data_json['quarterlyReports']
    time_points = []
    value_points = []
    for i in reports:
        # i ist ein  Array
        time_points.append(i['fiscalDateEnding'])
        value_points.append(i[indicator])

    value_points, time_points = reverse_lists(value_points, time_points)

    data = [time_points, value_points, symbol, indicator]

    return data
