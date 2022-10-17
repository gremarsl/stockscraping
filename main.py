# **********************************************************************************************************************
# Imports
# **********************************************************************************************************************
import global_vars
from analyse_data_from_local_json_file import analyze_data_from_local_json_file
from build_own_json import build_own_json_file
from functions_for_yahoo import calculate_sp_500_to_gdp_usa, calculate_dax_to_gdp_germany, get_yahoo_data
from general_functions import merge_file_list


# **********************************************************************************************************************
# Functions
# **********************************************************************************************************************

def own_json_analysis():
    print("### START OWN JSON ANALYSIS ###")

    if global_vars.BUILD_MY_JSON == 1:
        build_own_json_file(global_vars.SYMBOL_LIST)

    if global_vars.ANALYZE_MY_JSON_DATA == 1 or global_vars.COMPARE_MY_JSON_COMPANIES == 1:
        analyze_data_from_local_json_file(global_vars.SYMBOL_LIST, global_vars.COMPARE_MY_JSON_COMPANIES)

    print("### END OWN JSON ANALYSIS ###")


def yahoo_data_analysis():
    print("### START YAHOO FINANCE ANALYSIS ###")
    # set global variable SOURCE to yahoo
    global_vars.SOURCE = "yahoo"
    if global_vars.GET_YAHOO_DATA:
        file_list = get_yahoo_data(global_vars.SYMBOL_LIST)

        merge_file_list(file_list, global_vars.SYMBOL_LIST)

    if global_vars.ANALYZE_YAHOO_DATA == 1 or global_vars.COMPARE_YAHOO_COMPANIES == 1:
        analyze_data_from_local_json_file(global_vars.SYMBOL_LIST, global_vars.COMPARE_YAHOO_COMPANIES)

    print("### END YAHOO FINANCE ANALYSIS ###")


# ----------------------------------------------------------------------------------------------------------------------
# main()
# ----------------------------------------------------------------------------------------------------------------------
def main() -> None:
    yahoo_data_analysis()
    own_json_analysis()

    # calculate_dax_to_gdp_germany()
    # calculate_sp_500_to_gdp_usa()


# ----------------------------------------------------------------------------------------------------------------------
# Entrypoint
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
