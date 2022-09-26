import matplotlib.pyplot as plt
from general_functions import convert_list_elements_to_float, convert_list_elements_to_date_instance
from options import *


def stupid_plot_data_lists(data_list: list, source: str) -> None:
    # x: list, y: list, symbol: str, indicator: str

    # data_per_symbol = [[[x_1],[y_1],symbol_1,indicator_1],...,[x_i],[y_i],symbol_i,indicator_i]]
    plt.figure()

    for i in data_list:

        x = i[0]
        y = i[1]
        y = convert_list_elements_to_float(y)
        symbol = i[2]
        indicator = i[3]

        if len(x) == len(y):
            plt.plot(x, y, label=indicator, color=options_for_plot_color[indicator]())
            plt.scatter(x, y, color=options_for_plot_color[indicator]())

        else:
            print(f"ERROR - Length of x is {len(x)} and length of y is {len(y)} - must be same")

    # show grid
    plt.grid(b=None, which='major', axis='both')
    plt.xticks(data_list[0][0], rotation="vertical")
    plt.title(f'{symbol} source: {source}')
    plt.xlabel('Year')

    # plot_full_screen()
    plt.legend()

    plt.show()


def plot_full_screen():
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    pass


def plot_compare_symbols_one_indicator(data_list, source):
    # show grid
    indicator = data_list[0][3]

    for i in data_list:
        x = i[0]
        x = convert_list_elements_to_date_instance(x)
        y = i[1]
        y = convert_list_elements_to_float(y)
        symbol = i[2]
        indicator = i[3]

        if len(x) != len(y):
            raise print(f"ERROR - Length of x is {len(x)} and length of y is {len(y)} - must be same")

            plt.plot(x, y, label=symbol)
            plt.scatter(x, y)

    plt.grid(b=None, which='major', axis='both')
    plt.xticks(data_list[0][0], rotation="vertical")
    plt.title(f'{indicator} source: {source}')
    plt.xlabel('Year')

    # plot_full_screen()

    plt.legend()
    # save_figure(indicator)
    # print("plt.show is commented, this is why the plot will not show up")
    plt.show()
    plt.cla()
