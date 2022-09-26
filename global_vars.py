import os

# START USER CONFIG SWITCHES
# set value to 1, to enable an analysis and calculation. set value to 0 to disable it.

'''

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


get_yahoo_data = 0
analyze_yahoo_data = 1
analyze_yahoo_compare_companies = 1


build_own_json =get_yahoo_data
analyze_my_json_data = analyze_yahoo_data
analyze_my_json_data_compare_companies = analyze_yahoo_compare_companies

calculate_dax = 0
calculate_sp500 = 0
# END USER CONFIG SWITCHES


# START COMPANIES TO ANALYZE
'''
@param my_json_symbols          Companies to analyze with own data
'''


my_json_symbols = ["MSFT"]
yahoo_symbols = ["MSFT","AAPL"]
# END COMPANIES TO ANALYZE


# START ADVANCED PARAMETERS



  # START SWITCHES FOR JSON ANALYSIS
analyze_absolute_my_json = 0
analyze_percentage_my_json = 0
analyze_live_with_my_json = 0
  # END SWITCHES FOR JSON ANALYSIS

  # START SWITCHES FOR JSON ANALYSIS
analyze_abs_yahoo = 1
analyze_rel_yahoo = 0
analyze_rel_live_yahoo = 0
  # END SWITCHES FOR JSON ANALYSIS

  # START PARAMETERS FOR INDEX CALCULATION
sp_500_divisor = 8451.33
usa_gdp = 19731.10  # billion
germany_gdp = 3806  # billion
dax_40_test = ["SY1.DE","1COV.DE","SHL.DE"]

dax_40 = ["SY1.DE","1COV.DE","SHL.DE","DPW.DE","CON.DE","PUM.DE","AIR.DE","BEI.DE","DDAIF","HEN.DE","IFX.DE","ADS.DE","HNR1.DE","SIE.DE","FME.DE","VOW3.DE","LIN.DE","DBK.DE","BAS.DE","MRK.DE","DB1.DE","ZAL.DE","FRE.DE","RWE.DE","DTE.DE","BAYN.DE","BMW.DE","MTX.DE","ALV.DE","HEI.DE","HFG.DE","DTG.DE","BNR.DE","CON.DE","EOAN.DE","QGEN","PAH3.DE","SAP.DE","VNA.DE","ZAL.DE"]
  # END PARAMETERS FOR INDEX CALCULATION

# END ADVANCED PARAMETERS



# START FILEPATH PARAMETER
directory_of_execution = os.getcwd()

filepath_my_json = directory_of_execution + "\\reports_json\\"

filepath_yahoo = directory_of_execution + "\\yahoo_info\\"

market_cap = 0

# END FILEPATH PARAMETER
