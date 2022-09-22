import csv
import time

import matplotlib.pyplot as plt
import json
import os
import datetime as dt

import requests

import global_vars


def extract_quarterly_report_data_from_my_json_file(data_json: dict, indicator: str, symbol: str) -> list:
    reports = data_json['quarterlyReports']
    time_points = []
    value_points = []
    for i in reports:
        # i ist ein  Array
        try:
            time_points.append(i['fiscalDateEnding'])  # releaseDate
            value_points.append(i[indicator])
        except:
            print("Appending data element to array didn´t work with indicator {}. Is the indicator in the data?".format(
                indicator))
            exit()
    value_points, time_points = reverse_lists(value_points, time_points)

    data = [time_points, value_points, symbol, indicator]

    return data


def extract_quarterly_report_data(data_json: dict, indicator: str, symbol: str) -> list:
    # this function is a direct copy of extract_quarterly_report_data_from_alpha!! and based on the namings in alpha data
    reports = data_json['quarterlyReports']
    time_points = []
    value_points = []
    for i in reports:
        # i ist ein  Array
        try:
            time_points.append(i['fiscalDateEnding'])
            value_point = i[indicator]
            if value_point == "None":
                print("Analyzing of {} not possible, since no data available - data == None".format(indicator))
            value_points.append(i[indicator])
        except:
            print("Appending data element to array didn´t work with indicator {}. Is the indicator in the data?".format(
                indicator))
            exit()
    value_points, time_points = reverse_lists(value_points, time_points)

    data = [time_points, value_points, symbol, indicator]

    return data


def get_data(input_data, indicator, symbol):
    # if you change this please also change get_float_data
    # quotient: research and development:
    try:
        list_dividend = extract_quarterly_report_data(input_data, indicator, symbol=symbol)

        # convert to int
        list_dividend_converted = convert_list_elements_to_int(list_dividend[1])

        data = [list_dividend[0], list_dividend_converted, symbol, indicator]

        return data
    except:
        print(f"function call: get data failed - parameter:{indicator}; {symbol} ")
    return 1  # error if 1 is returned


def get_float_data(input_data, indicator, symbol):
    # if you change this please also change get_data

    # quotient: research and development:
    try:
        list_dividend = extract_quarterly_report_data(input_data, indicator, symbol=symbol)

        # convert to int
        temp_converted = convert_list_elements_to_float(list_dividend[1])
        list_dividend_converted = convert_list_elements_to_int(temp_converted)

        data = [list_dividend[0], list_dividend_converted, symbol, indicator]
        return data

    except:
        print("function call: get float data failed - parameter:{}; {} ".format(indicator, symbol))
    return 1  # error if 1 is returned


def calculate_quotient(dividend_data, divisor_data):
    quotient_list = [(x / y) * 100 for x, y in zip(dividend_data, divisor_data)]

    return quotient_list


def split_indicator_in_two(indicator):
    dividend_str = indicator.split('_to_')[0]
    divisor_str = indicator.split('_to_')[1]

    return dividend_str, divisor_str


def filter_data(data_list, options):
    packed_indicators = []
    indicators = []
    for i in options:
        indicator = filter(lambda x: x[3] == i, data_list)
        indicator_list = list(indicator)
        if len(indicator_list) != 0:
            packed_indicators.append(indicator_list)

    # unpacking the list because with append to indicators - we have one list element to much - what we didnt have when doing list(filter(...))
    # unpack one level
    temp = packed_indicators[0]

    for i in temp:
        indicators.append(i)

    return indicators


def read_data_from_file(filename):
    try:
        if os.path.isfile(filename):
            with open(filename) as json_file:
                data = json.load(json_file)
                return data

    except FileExistsError:
        print("File does not exist")


def only_plot(data, title):
    data.plot()
    plt.title(title)
    plt.show()


def reverse_lists(x: list, y: list) -> list:
    x = x[::-1]
    y = y[::-1]

    return x, y


def write_to_file_in_csv_format(data, name_of_file: str) -> None:
    f = open(name_of_file, "w")
    f.write(str(data))
    f.close()


def write_to_file_in_json_format(data, name_of_file: str) -> None:
    f = open(name_of_file, "w")
    f.write(str(json.dumps(data, indent=4)))
    f.close()


def convert_list_elements_to_float(y):
    y_converted = []
    for x in y:
        x = float(x)
        y_converted.append(x)
    return y_converted


def convert_list_elements_to_int(y):
    return [int(x) for x in y]


def convert_list_elements_to_date_instance(dates_as_strings):
    dates_as_dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates_as_strings]

    return dates_as_dates


def delete_object_key(json_data_object, key):
    del json_data_object[key]
    return json_data_object


def create_json_object_finance(s):
    d = {}
    d['symbol'] = s
    d["quarterlyReports"] = []
    array = d["quarterlyReports"]
    return d


# füge jedes quarter in dem input_file_object - füge das quarter mit den wichtigen parameter als object hinzu
def add_keys_values_to_object(list_filtered):
    # erstelle ein object für das aktuelle quarter
    obj = {}

    for elem in list_filtered:
        # füge key und value zu dem object hinzu
        obj[elem[0]] = elem[1]

    return obj


# add key value to an object
def append_key_value_to_object(object, key, value):
    object[key] = value

    return object


def get_key_value_from_local_file(indicator, s):
    try:
        symbol_info = read_data_from_file("yahoo_info_data_" + s[0] + ".json")
        i = symbol_info[indicator]

    except:
        print(i)
        print("live data from yahoo failed and no locally data for {} available".format(indicator))

    return i


def delete_all_lines_from_file():
    with open(global_vars.filepath_my_json + "\\atestsite.html", "w") as file:
        file.truncate()
    pass


def add_file_to_main_html_file(indicator, complete_string):
    f = open(global_vars.filepath_my_json + '\\atestsite.html', 'a')

    message = """
    <html>
       <center>
        <figure>
            <figcaption> {} im Quartal </figcaption>
            <img src="{}" vspace=30 alt="my img"/>    
        </figure>
       </center>
    </html>
    """.format(indicator, complete_string)

    f.write(message)
    f.close()
    pass


def save_figure(indicator):
    path = global_vars.filepath_my_json + "\\financial_grafics\\"

    complete_string_svg = path + indicator + ".svg"
    complete_string_pdf = path + indicator + ".pdf"

    plt.tight_layout()
    plt.savefig(complete_string_svg, dpi=300, bbox_inches="tight")
    plt.savefig(complete_string_pdf, dpi=300, bbox_inches="tight")

    add_file_to_main_html_file(indicator, complete_string_svg)
    pass


def get_file_age_in_hours(filepath) -> float:
    delta = time.time() - os.path.getmtime(filepath)
    delta_in_hours = delta / 3600
    print(delta_in_hours)
    return delta_in_hours


def http_basic_access_authentication():
    try:
        resp = requests.post('https://pes.ciplus.vi.vector.int/login/auth/', data={}, auth=('abc', 'abc'), verify=False)
        print(resp)
    except ValueError:
        print("Auth login didnt work")


def convert_and_save_to_csv(data, name_of_file):
    data_csv = data.to_csv()
    write_to_file_in_csv_format(data_csv, name_of_file)


def yahoo_csv_data_formatting(file):
    # this function makes some operations on csv data
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
    for row in rows:
        row_stripped = row[0].replace(" ", "")

        row[0] = row_stripped

    return header, rows

