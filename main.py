from analyse_data_from_alpha_vantage import analyze_data_from_alpha_vantage
from analyse_data_from_local_json_file import analyze_data_from_local_json_file
from analyze_data_from_finnhub import analyze_data_from_finnhub
from build_own_json import build_own_json_file
from functions_for_finnhub import calling_finnhub_api
from functions_for_alpha_vantage import calling_alpha_vantage_api
from functions_for_yahoo import calculate_sp_500_to_gdp_usa

# START USER CONFIG SWITCHES
# set value to 1, to do / enable an analysis and calculation. set value to 0 to skip / disable it
get_finnhub_data = 0
analyze_finnhub_data = 0

get_alpha_data = 0
analyze_alpha_data = 0
analyze_alpha_data_compare_companies = 1

build_own_json = 0
analyze_my_json_data = 0
analyze_my_json_data_compare_companies = 1
# END USER CONFIG SWITCHES

# START ENTER COMPANIES TO ANALYZE
get_finnhub_symbol = ["MSFT", "AAPL"]
analyze_finnhub_symbol = ["MSFT", "AAPL"]

get_alpha_vantage_symbol_data = ["MSFT", "AAPL"]
analyze_alpha_vantage_symbol_data = ["MSFT", "AAPL"]

build_json_from_symbols = ["BAS.DE", "AAPL"]
my_json_symbol = ["BAS.DE", "MSFT"]


# END ENTER COMPANIES TO ANALYZE


def finnhub_analysis():
    if get_finnhub_data == 1:
        calling_finnhub_api(get_finnhub_symbol)

    if analyze_finnhub_data == 1:
        analyze_data_from_finnhub(analyze_finnhub_symbol)
    pass


def alpha_vantage_analysis():
    if get_alpha_data == 1:
        calling_alpha_vantage_api(get_alpha_vantage_symbol_data)

    if analyze_alpha_data == 1 or analyze_alpha_data_compare_companies == 1:
        analyze_data_from_alpha_vantage(analyze_alpha_vantage_symbol_data, analyze_alpha_data_compare_companies)
    pass


def own_json_analysis():
    if build_own_json == 1:
        build_own_json_file(build_json_from_symbols)

    if analyze_my_json_data == 1 or analyze_my_json_data_compare_companies == 1:
        analyze_data_from_local_json_file(my_json_symbol, analyze_my_json_data_compare_companies)

    pass


def start():

    finnhub_analysis()

    alpha_vantage_analysis()

    own_json_analysis()

    #gimmic
    calculate_sp_500_to_gdp_usa()

    pass


if __name__ == '__main__':
    # TODO documentation!!
    #TODO dependency managment
    start()
