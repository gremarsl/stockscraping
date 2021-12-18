import matplotlib.pyplot as plt
import json
import os
import datetime as dt


def extract_quarterly_report_data(data_json: dict, indicator: str, symbol: str) -> list:
    # this function is a direct copy of extract_quarterly_report_data_from_alpha!! and based on the namings in alpha data
    reports = data_json['quarterlyReports']
    time_points = []
    value_points = []
    for i in reports:
        # i ist ein  Array
        try:
            time_points.append(i['fiscalDateEnding'])
            value_points.append(i[indicator])
        except:
            print("Appending data element to array didn´t work with indicator {}. Is the indicator in the data?".format(
                indicator))
            exit()
    value_points, time_points = reverse_lists(value_points, time_points)

    data = [time_points, value_points, symbol, indicator]

    return data


def get_data(input_data, indicator, symbol):
    # quotient: research and development:
    list_dividend = extract_quarterly_report_data(input_data, indicator, symbol=symbol)

    # convert to int
    list_dividend_converted = convert_list_elements_to_int(list_dividend[1])

    data = [list_dividend[0], list_dividend_converted, symbol, indicator]

    return data


def calculate_quotient(dividend_data, divisor_data, indicator, symbol):
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
        if (len(indicator_list) != 0):
            packed_indicators.append(indicator_list)

    # unpacking the list because with append to indicators - we have one list element to much - what we didnt have when doing list(filter(...))
    for i in packed_indicators:
        [unpack] = i
        indicators.append(unpack)

    return indicators


def get_data_from_file(filename):
    if os.path.isfile(filename):
        with open(filename) as json_file:
            data = json.load(json_file)
    else:
        print(
            "WARNING: file not found - This should not be reached")

    return data


def only_plot(data, title):
    data.plot()
    plt.title(title)
    plt.show()


def reverse_lists(x: list, y: list) -> list:
    x = x[::-1]
    y = y[::-1]

    return x, y


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

    dates_as_dates= [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates_as_strings]

    return dates_as_dates