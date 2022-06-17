import os

global market_cap
market_cap = 0

directory_of_execution = os.getcwd()

global filepath_alpha
filepath_alpha = directory_of_execution + "\\alpha_vantage\\"

global filepath_finnhub
filepath_finnhub = directory_of_execution + "\\finnhub\\"

global my_json
filepath_my_json = directory_of_execution + "\\reports_json\\"

global sp_500_divisor
sp_500_divisor = 8451.33

global usa_gdp
usa_gdp = 19731.10  # billion
