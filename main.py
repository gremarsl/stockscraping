import global_vars
from analyse_data_from_alpha_vantage import analyse_data_from_alpha_vantage
from analyse_data_from_finnhub import analyse_data_from_finnhub
from analyse_data_from_local_json_file import analyse_data_from_local_json_file
from build_own_json import build_own_json_file
from functions_for_finnhub import calling_finnhub_api
from functions_for_alpha_vantage import calling_alpha_vantage_api
from functions_for_yahoo import get_market_cap_from_yahoo_finance
from general_functions import delete_all_lines_from_file

# Understand JSON
# object: {}
# array : []
# key-value pair is object data

automotive_finnhub = ["DAI.DE", "BMW.DE", "VOW.DE", "PAH3.DE"]
chemicals_finnhub = ["BAS.DE", "BAYN.DE", "LIN.DE", "HEN3.DE", "1COV.DE"]
industry_finnhub = ["SIE.DE"]
consumer_finnhub = ["BEI.DE"]

semiconductor = ["INTC", "AMD", "NVDA", "AAPL", "MSFT", "QCOM", "MRVL"]  # "ASML","KLAC","STM","SNPS", "AMBA"
semiconductor_nasdaq_alpha = ["IBM", "MSFT", "AAPL", "AMD", "ASML", "NVDA", "KLAC", "TEAM", "UMC", "TSM"]
semiconductor_nasdaq_alpha2 = ["ZS"]  # , "VSH", "SNPS", "VLDRW", "MU", "ADI"
design_semiconductor = ["SNPS", "CDNS"]
big = ["MSFT", "AAPL", "GOOGL", "FB", "AMD", "NVDA"]
energy = ["CVX"]  # "COP","XOM" ,"RDS-B","BP"

automotive_alpha = ["TSLA"]
network_alpha = ["NOK", "VZ", "T"]
consumer_alpha = ["PRG", "KO", "MCD", "NKE", "DIS", "OR.PA"]  # spencer
mobility_alpha = ["BA"]
pharma_companies_alpha = ["JNJ", "PFE", "ABBV", "MRK", "GSK"]
finance_alpha = ["V"]

insurance = ["ALV"]

get_finnhub_symbol = automotive_finnhub
analyse_finnhub_symbol = automotive_finnhub

get_alpha_vantage_symbol_data = automotive_finnhub
analyse_alpha_vantage_symbol_data = ["MSFT", "AAPL"]

build_json_from_symbols = ["MSFT", "AAPL"]
my_json_symbol = ["MSFT","AAPL"]

# SWITCHES:
build_own_json = 0
analyse_my_json_data = 1
analyse_my_json_data_compare_companies = 1

get_finnhub_data = 0
analyse_finnhub_data = 0

get_alpha_data = 0
analyse_alpha_data = 0
analyse_alpha_data_compare_companies = 0

if __name__ == '__main__':

    delete_all_lines_from_file()

    if get_finnhub_data == 1:
        calling_finnhub_api(get_finnhub_symbol)

    if analyse_finnhub_data == 1:
        analyse_data_from_finnhub(analyse_finnhub_symbol)

    if get_alpha_data == 1:
        calling_alpha_vantage_api(get_alpha_vantage_symbol_data)

    if analyse_alpha_data == 1 or analyse_alpha_data_compare_companies == 1:
        analyse_data_from_alpha_vantage(analyse_alpha_vantage_symbol_data, analyse_alpha_data_compare_companies)

    if build_own_json == 1:
        build_own_json_file(build_json_from_symbols)

    if analyse_my_json_data == 1  or analyse_my_json_data_compare_companies == 1:
        global_vars.market_cap = get_market_cap_from_yahoo_finance(my_json_symbol[0])
        print(global_vars.market_cap)
        analyse_data_from_local_json_file(my_json_symbol,analyse_my_json_data_compare_companies)

'''
next goals: deploy own server to get the graphs shown in the browser

python -m http.server 8000



#Erkenntnis:
# ein JSON Objekt ist in Python in Dictionary - 
# Hinzufügen eines Key Value paares über     
# dict[key]= value - um zu vemreiden dass doppelte anführunggstringe kommen -> vorher mit '' versehen

'''
