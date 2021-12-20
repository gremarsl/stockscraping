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
get_finnhub_data = 0
analyse_finnhub_data = 0
get_alpha_data = 0
analyse_alpha_data = 1
analyse_alpha_data_compare_companies = 1

# analyse_finnhub_symbol_automotive = ["DAI.DE","BMW.DE","VOW.DE", "PAH3.DE"]
dax_symbols = ["BAS.DE", "SIE.DE", "BAYN.DE", "IFX.DE", "1COV.DE", "LIN.DE", "BEI.DE", "HEN3.DE"]  # a",
# get_finnhub_symbol = ["MRVL","AMBA","QCOM","ZS","ASML","NVDA","TEAM","JNJ","PRG","PFE","AMD","MSFT","AVGO", "AAPL"]
get_finnhub_symbol = ["PYPL"]

# analyse_finnhub_symbol = ["SNPS","MRVL","AMBA","QCOM","ZS","ASML","NVDA","TEAM","JNJ","PRG","PFE","AMD","MSFT","AVGO", "AAPL"] # ALV.DE, "DBK.DE",

analyse_finnhub_symbol = ["BAS.DE"]  # ALV.DE, "DBK.DE",

get_alpha_vantage_symbol_data = ["ALIZF", "BMWYY"]
analyse_alpha_vantage_symbol_data = ["PYPL", "AMD", "SNPS"] #"MRVL", "AMBA", "QCOM", "ZS", "ASML", "NVDA", "TEAM"
# get_symbol_data_alpha_vantage = ["SNPS","MRVL","AMBA","QCOM","ZS","ASML","NVDA","TEAM"]  # "IBM", "AAPL"
# symbols work: "JNJ","PRG","PFE","AMD","MSFT","AVGO", "AAPL"

if __name__ == '__main__':
    if analyse_own_excel_data == 1:
        analyse_data_from_local_json_file()

    if get_finnhub_data == 1:
        calling_finnhub_api(get_finnhub_symbol)

    if analyse_finnhub_data == 1:
        analyse_data_from_finnhub(analyse_finnhub_symbol)

    if get_alpha_data == 1:
        calling_alpha_vantage_api(get_alpha_vantage_symbol_data)

    if analyse_alpha_data == 1 and analyse_alpha_data_compare_companies == 0:
        analyse_data_from_alpha_vantage(analyse_alpha_vantage_symbol_data)

    if analyse_alpha_data == 1 and analyse_alpha_data_compare_companies == 1:
        analyse_data_from_alpha_vantage(analyse_alpha_vantage_symbol_data)
