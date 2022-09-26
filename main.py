import global_vars
from analyse_data_from_local_json_file import analyze_data_from_local_json_file
from build_own_json import build_own_json_file
from functions_for_yahoo import calculate_sp_500_to_gdp_usa, calculate_dax_to_gdp_germany, get_yahoo_data
from general_functions import merge_file_list


def own_json_analysis():
    print("start own json analysis ...")

    if global_vars.build_own_json:
        build_own_json_file(global_vars.my_json_symbols)

    if global_vars.analyze_my_json_data or global_vars.analyze_my_json_data_compare_companies:

        analyze_data_from_local_json_file(global_vars.my_json_symbols,
                                          global_vars.analyze_my_json_data_compare_companies)

    print("end own json analysis  ...")


def yahoo_data_analysis():
    print("start yahoo finance analysis ...")
    if global_vars.get_yahoo_data == 1:
        file_list = get_yahoo_data(global_vars.yahoo_symbols)

        merge_file_list(file_list, global_vars.yahoo_symbols)

    if global_vars.analyze_yahoo_data == 1:
        analyze_data_from_local_json_file(global_vars.yahoo_symbols, global_vars.analyze_yahoo_compare_companies)
    print("end yahoo finance analysis ...")


def start():
    yahoo_data_analysis()
    own_json_analysis()


    # gimmic
    calculate_dax_to_gdp_germany()
    calculate_sp_500_to_gdp_usa()


if __name__ == '__main__':
    start()
