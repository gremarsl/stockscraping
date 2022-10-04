import os


'''
@param GET_YAHOO_DATA                     Requests / Gets data from yahoo finance for the entered companies. 
                                          If enabled / set to 1.
@param ANALYZE_YAHOO_DATA                 Evaluates the available data from yahoo finance for the 
                                          entered companies. If enabled / set to 1 every company get evaluated and 
                                          can be interpreted with the help of graphics showing financial indicators 
                                          separately.
@param COMPARE_YAHOO_COMPANIES            Evaluates the available data from alpha vantage. 
                                          If enabled the entered companies are evaluated and shown 
                                          together in one graphic for easier comparison.
'''
# START USER CONFIG SWITCHES
# set value to 1, to enable an analysis and calculation. set value to 0 to disable it.
GET_YAHOO_DATA            = 0
ANALYZE_YAHOO_DATA        = 0
COMPARE_YAHOO_COMPANIES   = 1

BUILD_MY_JSON             = 0
ANALYZE_MY_JSON_DATA      = 0
COMPARE_MY_JSON_COMPANIES = 0

CALC_DAX                  = 0
CALC_SP500                = 0
# END USER CONFIG SWITCHES

'''
@param symbol_list          Companies to analyze
'''
# START COMPANIES TO ANALYZE
SYMBOL_LIST = ["MSFT", "AAPL", "GOOGL" , "FB", "AMD", "NVDA"]
# END COMPANIES TO ANALYZE


# START ADVANCED PARAMETERS
ANALYZE_YAHOO_ABS       = 0
ANALYZE_YAHOO_REL       = 0
ANALYZE_YAHOO_REL_LIVE  = 1
# END ADVANCED PARAMETERS

# START FILEPATH PARAMETER
directory_of_execution  = os.getcwd()
filepath_my_json        = directory_of_execution + "\\reports_json\\"
filepath_yahoo          = directory_of_execution + "\\yahoo_info\\"
# END FILEPATH PARAMETER


# START PARAMETERS FOR INDEX CALCULATION
SP_500_DIVISOR = 8451.33
GDP_USA = 19731.10  # billion
GDP_GERMANY = 3806  # billion
DAX = ["SY1.DE", "1COV.DE", "SHL.DE", "DPW.DE", "CON.DE", "PUM.DE", "AIR.DE", "BEI.DE", "DDAIF", "HEN.DE", "IFX.DE", "ADS.DE", "HNR1.DE", "SIE.DE", "FME.DE", "VOW3.DE", "LIN.DE", "DBK.DE", "BAS.DE", "MRK.DE", "DB1.DE", "ZAL.DE", "FRE.DE", "RWE.DE", "DTE.DE", "BAYN.DE", "BMW.DE", "MTX.DE", "ALV.DE", "HEI.DE", "HFG.DE", "DTG.DE", "BNR.DE", "CON.DE", "EOAN.DE", "QGEN", "PAH3.DE", "SAP.DE", "VNA.DE", "ZAL.DE"]
# END PARAMETERS FOR INDEX CALCULATION