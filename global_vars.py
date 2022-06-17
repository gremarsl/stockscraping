import os

# START SWITCHES FOR ALPHA VANTAGE ANALYSIS
# set value to 1, to do / enable an analysis and calculation. set value to 0 to skip / disable it
analyze_absolute_income_statement = 1
analyze_absolute_cash_flow = 1
analyze_percentage_income_statement = 1
analyze_percentage_balance_sheet = 1
analyze_live_with_income_statement = 1
analyze_live_with_balance_sheet = 1
# START SWITCHES FOR ALPHA VANTAGE ANALYSIS


# START SWITCHES FOR JSON ANALYSIS
# set value to 1, to do / enable an analysis and calculation. set value to 0 to skip / disable it
analyze_absolute_my_json = 1
analyze_percentage_my_json = 1
analyze_live_with_my_json = 1
# END SWITCHES FOR JSON ANALYSIS


# START PARAMETERS TO BE UPDATED ONCE IN A WHILE
sp_500_divisor = 8451.33
usa_gdp = 19731.10  # billion
# END PARAMETERS TO BE UPDATED ONCE IN A WHILE

# START PATH PARAMETER
directory_of_execution = os.getcwd()

filepath_alpha = directory_of_execution + "\\alpha_vantage\\"

filepath_finnhub = directory_of_execution + "\\finnhub\\"

filepath_my_json = directory_of_execution + "\\reports_json\\"

filepath_yahoo = directory_of_execution + "\\yahoo_info\\"

market_cap = 0
# END PATH PARAMETER
