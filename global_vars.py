# **********************************************************************************************************************
# Imports
# **********************************************************************************************************************
import os

# **********************************************************************************************************************
# Constants
# **********************************************************************************************************************

'''
@param symbol_list          Companies to analyze
'''
SYMBOL_LIST = ["GOOGL"] # MSFT", "AAPL","AMD","NVDA
SOURCE = "EMPTY"

'''
@param GET_YAHOO_DATA                     Requests data from yahoo finance for the entered companies. 
                                          If enabled, data is requested for each company symbol with the list
@param ANALYZE_YAHOO_DATA                 Evaluates the available data from yahoo finance for the 
                                          entered companies. If enabled every company get evaluated and 
                                          can be interpreted with the help of graphics showing financial indicators 
                                          separately.
@param COMPARE_YAHOO_COMPANIES            Evaluates the available data from alpha vantage. 
                                          If enabled the entered companies are evaluated and shown 
                                          together in one graphic for easier comparison.
'''

GET_YAHOO_DATA = 0
ANALYZE_YAHOO_DATA = 1
COMPARE_YAHOO_COMPANIES = 0

BUILD_MY_JSON = 0
ANALYZE_MY_JSON_DATA = 0
COMPARE_MY_JSON_COMPANIES = 0

CALC_DAX = 0
CALC_SP500 = 0

'''
# set value to 1, to enable an analysis and calculation. set value to 0 to disable it.

@param ANALYZE_YAHOO_ABS                If enabled, script analyzes yahoo absolute indicators 
                                        from list ABS_INDICATOR_LIST and plots the data.
                                        e.g. TotalRevenue,NetIncome,TotalAssets
@param ANALYZE_YAHOO_REL                If enabled, script analyzes yahoo relative indicators 
                                        from list REL_INDICATORS_LIST and plots the data.
                                        e.g. TotalRevenue/TotalAssets
@param ANALYZE_YAHOO_REL_LIVE           If enabled, script analyzes live yahoo relative indicator 
                                        from list REL_LIVE_INDICATOR_LIST and plots the data.
                                        If enabled the entered companies are evaluated and shown 
                                        together in one graphic for easier comparison.
                                        e.g. TotalRevenue/live_marketCap
'''
ANALYZE_YAHOO_ABS = 1
ANALYZE_YAHOO_REL = 1
ANALYZE_YAHOO_REL_LIVE = 1

ABS_INDICATOR_LIST = ["TotalRevenue", "NetIncome","GrossProfit"]

REL_INDICATORS_LIST = ["NetIncome_to_TotalRevenue", "ResearchDevelopment_to_TotalRevenue", "TotalLiab_to_TotalAssets",
                       "TotalCurrentLiab_to_TotalCurrentAssets","OperatingIncome_to_TotalRevenue"]

REL_LIVE_INDICATOR_LIST = ["marketCap_to_TotalRevenue", "marketCap_to_NetIncome", "marketCap_to_TotalAssets"]


SP_500_DIVISOR = 8451.33
GDP_USA = 19731.10  # billion
GDP_GERMANY = 3806  # billion
DAX = ["SY1.DE", "1COV.DE", "SHL.DE", "DPW.DE", "CON.DE", "PUM.DE", "AIR.DE", "BEI.DE", "DDAIF", "HEN.DE", "IFX.DE",
       "ADS.DE", "HNR1.DE", "SIE.DE", "FME.DE", "VOW3.DE", "LIN.DE", "DBK.DE", "BAS.DE", "MRK.DE", "DB1.DE", "ZAL.DE",
       "FRE.DE", "RWE.DE", "DTE.DE", "BAYN.DE", "BMW.DE", "MTX.DE", "ALV.DE", "HEI.DE", "HFG.DE", "DTG.DE", "BNR.DE",
       "CON.DE", "EOAN.DE", "QGEN", "PAH3.DE", "SAP.DE", "VNA.DE", "ZAL.DE"]

# **********************************************************************************************************************
# Variables
# **********************************************************************************************************************
directory_of_execution = os.getcwd()
filepath_my_json = directory_of_execution + "\\reports_json\\"
filepath_yahoo = directory_of_execution + "\\yahoo_info\\"


