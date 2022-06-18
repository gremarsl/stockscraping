import os

# START USER CONFIG SWITCHES
# set value to 1, to enable an analysis and calculation. set value to 0 to disable it.

'''
@param get_finnhub_data                         Requests / Gets data from finnhub for the entered companies. 
                                                If enabled / set to 1.
@param analyze_finnhub_data                     Evaluates the available data from finnhub for the entered companies. 
                                                If enabled / set to 1.

@param get_alpha_data                           Requests / Gets data from alpha vantage for the entered companies. 
                                                If enabled / set to 1.
@param analyze_alpha_data                       Evaluates the available data from alpha vantage for the 
                                                entered companies. If enabled / set to 1 every company get evaluated and 
                                                can be interpreted with the help of graphics showing financial indicators 
                                                separately.
@param analyze_alpha_data_compare_companies     Evaluates the available data from alpha vantage. 
                                                If enabled the entered companies are evaluated and shown 
                                                together in one graphic for easier comparison.

@param build_own_json                           Builds a json file for the entered companies with data 
                                                from alpha vantage. If enabled / set to 1.
@param analyze_my_json_data                     Evaluates the available data from the json-files for the 
                                                entered companies. If enabled / set to 1 every company get evaluated 
                                                and can be interpreted with the help of grafics showing financial 
                                                indicators separately.
@param analyze_my_json_data_compare_companies   Evaluates the available data from  the json-files. 
                                                If enabled the entered companies are evaluated and shown 
                                                together in one graphic for easier comparison.
'''

get_finnhub_data = 0
analyze_finnhub_data = 1

get_alpha_data = 0
analyze_alpha_data = 0
analyze_alpha_data_compare_companies = 1

build_own_json = 0
analyze_my_json_data = 0
analyze_my_json_data_compare_companies = 1
# END USER CONFIG SWITCHES


# START COMPANIES TO ANALYZE
'''
@param finnhub_symbols          Companies to analyze with data from finnhub
@param alpha_vantage_symbols    Companies to analyze with data from alpha vantage
@param my_json_symbols          Companies to analyze with own data

'''
finnhub_symbols = ["MSFT", "AAPL"]

alpha_vantage_symbols = ["MSFT", "AAPL"]

my_json_symbols = ["BAS.DE", "MSFT"]
# END COMPANIES TO ANALYZE


# START ADVANCED PARAMETERS
  # START SWITCHES FOR ALPHA VANTAGE ANALYSIS

analyze_absolute_income_statement = 1
analyze_absolute_cash_flow = 1
analyze_percentage_income_statement = 1
analyze_percentage_balance_sheet = 1
analyze_live_with_income_statement = 1
analyze_live_with_balance_sheet = 1
  # END SWITCHES FOR ALPHA VANTAGE ANALYSIS


  # START SWITCHES FOR JSON ANALYSIS
analyze_absolute_my_json = 1
analyze_percentage_my_json = 1
analyze_live_with_my_json = 1
  # END SWITCHES FOR JSON ANALYSIS



  # START PARAMETERS FOR INDEX CALCULATION
sp_500_divisor = 8451.33
usa_gdp = 19731.10  # billion
  # END PARAMETERS FOR INDEX CALCULATION

# END ADVANCED PARAMETERS



# START FILEPATH PARAMETER
directory_of_execution = os.getcwd()

filepath_alpha = directory_of_execution + "\\alpha_vantage\\"

filepath_finnhub = directory_of_execution + "\\finnhub\\"

filepath_my_json = directory_of_execution + "\\reports_json\\"

filepath_yahoo = directory_of_execution + "\\yahoo_info\\"

market_cap = 0

# END FILEPATH PARAMETER
