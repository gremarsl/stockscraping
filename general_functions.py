
import matplotlib.pyplot as plt
import json
import os


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