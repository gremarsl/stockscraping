from analyse_data_from_alpha_vantage import analyse_data_from_alpha_vantage
from analyse_data_from_finnhub import analyse_data_from_finnhub
from analyse_data_from_local_json_file import analyse_data_from_local_json_file
from build_own_json import build_own_json_file
from functions_for_finnhub import calling_finnhub_api
from functions_for_alpha_vantage import calling_alpha_vantage_api

# Understand JSON
# object: {}
# array : []
# key-value pair is object data

# SWITCHES:
build_own_json = 1
analyse_my_json_data =1
get_finnhub_data = 0
analyse_finnhub_data = 0
get_alpha_data = 0
analyse_alpha_data = 1
analyse_alpha_data_compare_companies = 0

automotive_finnhub = ["DAI.DE", "BMW.DE", "VOW.DE", "PAH3.DE"]
chemicals_finnhub = ["BAS.DE", "BAYN.DE", "LIN.DE", "HEN3.DE", "1COV.DE"]
industry_finnhub = ["SIE.DE"]
consumer_finnhub = ["BEI.DE"]

semiconductor = ["INTC", "AMD", "ASML", "NVDA", "KLAC", "UMC", "TSM", "QCOM", "STM", "MRVL", "SNPS", "VLDRW", "AMBA",
                 "AMAT"]
semiconductor_nasdaq_alpha = ["IBM", "MSFT", "AAPL", "AMD", "ASML", "NVDA", "KLAC", "TEAM", "UMC", "TSM"]
semiconductor_nasdaq_alpha2 = ["ZS", "AMBA", "QCOM", "AVGO", "STM", "MRVL", "VSH", "SNPS", "VLDRW", "MU", "ADI"]

network_alpha = ["NOK", "VZ", "T"]
consumer_alpha = ["PRG", "KO", "MCD", "NKE", "DIS"]
mobility_alpha = ["BA"]
pharma_companies_alpha = ["JNJ", "PFE", "ABBV", "MRK", "GSK"]
finance_alpha = ["V"]

get_finnhub_symbol = ["IFX.DE"]
analyse_finnhub_symbol = automotive_finnhub

get_alpha_vantage_symbol_data = pharma_companies_alpha
analyse_alpha_vantage_symbol_data = pharma_companies_alpha

my_json_symbol = ["JNJ"]
if __name__ == '__main__':
    if build_own_json ==1:
        build_own_json_file(my_json_symbol)

    if analyse_my_json_data == 1:
        analyse_data_from_local_json_file(my_json_symbol)

    if get_finnhub_data == 1:
        calling_finnhub_api(get_finnhub_symbol)

    if analyse_finnhub_data == 1:
        analyse_data_from_finnhub(analyse_finnhub_symbol)

    if get_alpha_data == 1:
        calling_alpha_vantage_api(get_alpha_vantage_symbol_data)

    if analyse_alpha_data == 1 or analyse_alpha_data_compare_companies == 1:
        analyse_data_from_alpha_vantage(analyse_alpha_vantage_symbol_data, analyse_alpha_data_compare_companies)
