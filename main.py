from analyse_data_from_alpha_vantage import analyse_data_from_alpha_vantage
from analyse_data_from_finnhub import analyse_data_from_finnhub
from analyse_data_from_local_json_file import analyse_data_from_local_json_file
from functions_for_finnhub import calling_finnhub_api
from functions_for_alpha_vantage import calling_alpha_vantage_api

# Understand JSON
# object: {}
# array : []

# SWITCHES:
analyse_own_excel_data = 0
get_finnhub_data = 1
analyse_finnhub_data = 1
get_alpha_data = 0
analyse_alpha_data = 0
analyse_alpha_data_compare_companies = 0

automotive_finnhub =  ["DAI.DE","BMW.DE","VOW.DE", "PAH3.DE"]
chemicals_finnhub = ["BAS.DE","BAYN.DE","LIN.DE","HEN3.DE","1COV.DE"]
semiconductor_finnhub = ["NVDA"]
semiconductor_nasdaq_alpha = ["IBM","MSFT","AAPL","AMD","ASML","NVDA","KLAC","TEAM","UMC","TSM"]
semiconductor_nasdaq_alpha2 =["ZS","AMBA","QCOM","AVGO","V","STM","MRVL","VSH","SNPS","VLDRW","MU","ADI"]

consumer_finnhub = ["BEI.DE"]
consumer_companies_alpha = ["PRG"]
mobility_alpha = ["BA"]

pharma_companies_alpha = ["JNJ","PFE"]
industry_finnhub = ["SIE.DE"]

get_finnhub_symbol = ["IFX.DE"]
analyse_finnhub_symbol = ["IFX.DE"]

get_alpha_vantage_symbol_data = semiconductor_nasdaq_alpha
analyse_alpha_vantage_symbol_data = ["MSFT","AAPL","AMD"]

if __name__ == '__main__':
    if analyse_own_excel_data == 1:
        analyse_data_from_local_json_file()

    if get_finnhub_data == 1:
        calling_finnhub_api(get_finnhub_symbol)

    if analyse_finnhub_data == 1:
        analyse_data_from_finnhub(analyse_finnhub_symbol)

    if get_alpha_data == 1:
        calling_alpha_vantage_api(get_alpha_vantage_symbol_data)

    if analyse_alpha_data == 1:
        analyse_data_from_alpha_vantage(analyse_alpha_vantage_symbol_data,analyse_alpha_data_compare_companies)

    if analyse_alpha_data_compare_companies == 1:
        analyse_data_from_alpha_vantage(analyse_alpha_vantage_symbol_data,analyse_alpha_data_compare_companies)
