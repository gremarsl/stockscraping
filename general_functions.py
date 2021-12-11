import matplotlib.pyplot as plt
import json
import os


def calculate_quotient(dividend_data, divisor_data, indicator, symbol):
    dividend_str, divisor_str = split_indicator_in_two(indicator)

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
