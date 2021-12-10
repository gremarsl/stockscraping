import os
import json
from typing import Dict, List

import requests

from functions_for_finnhub import get_one_absolute_indicator_from_finnhub, get_fundamental_data_from_finnhub, \
    get_one_relative_indicator_from_finnhub, get_one_ratio_indicator_from_finnhub
from general_functions import write_to_file_in_json_format
from plot_functions import stupid_plot_data_lists, stupid_plot_data_list
from functions_for_alpha_vantage import \
    request_income_statement_from_alpha, \
    request_earnings_from_alpha, \
    request_cash_flow_from_alpha, \
    request_balance_sheet_from_alpha, \
    request_symbol_search_from_alpha, \
    request_overiew_from_alpha, \
    get_quaterly_report_alpha, \
    get_annual_report_alpha, \
    long_term_data_get_ebitda, \
    long_term_data_get_price_to_earning_ratio, calling_alpha_vantage_api


# Understand JSON
# object: {}
# array : []

class NoData(Exception): pass  # declare a label


class NoEbitData(Exception):    pass


class NoNetMarginData(object):
    print("Known Except: No net margin data in fundamental Data for")
    pass


def filter_plot_data_list_per_symbol(data_list: list,relativeData:bool, data_is_from_platform: str):

    # hier:  all_data_list = [data_per_symbol_1]
    if relativeData and data_is_from_platform == "alpha_vantage":
            try:
                if len(data_list) == 0: raise NoData()

                try:
                    indicators = list(filter(
                        lambda x: x[3] == "researchAndDevelopment_to_totalRevenue" or "totalLiabilities_to_totalAssets" ,
                        data_list))
                    stupid_plot_data_lists(indicators, data_is_from_platform)
                except:
                    print("no working indicators data")

            except NoData:
                print("no income data ")
                pass

    else:
        eps_ebit_per_share_plot_data = []
        if data_is_from_platform == "finnhub":
            except_grossmargin = list(filter(lambda x: (x[3] != "grossMargin"), data_list))

            except_grossmargin_debt = list(filter(lambda x: x[3] != "totalDebtToEquity", except_grossmargin))

            eps_ebit_per_share_plot_data = list(
                filter(lambda x: x[3] == "eps" or x[3] == "ebitPerShare", data_list))

            ratios_eps_ebit_net_margin_data = list(filter(
                lambda x: (x[3] == "eps" or x[3] == "cashRatio" or x[3] == "currentRatio" or x[3] != "ebitPerShare" or
                           x[3] == "netMargin"), data_list))

            stupid_plot_data_lists(eps_ebit_per_share_plot_data, data_is_from_platform)

            try:
                stupid_plot_data_lists(except_grossmargin_debt, data_is_from_platform)
            except:
                print("Not working to plot ratios_eps_ebit_net_margin_data data in one plot {}".format(data_list))

        if data_is_from_platform == "alpha_vantage":
            try:
                if len(data_list) == 0: raise NoData()

                try:
                    indicators = list(filter(
                        lambda x: x[3] == "grossProfit" or "totalRevenue" or "ebit" or "netIncome" or "operatingIncome" or "incomeBeforeTax",
                        data_list))
                    stupid_plot_data_lists(indicators, data_is_from_platform)
                except:
                    print("no working indicators data")

            except NoData:
                print("no income data ")
                pass

        try:
            if len(eps_ebit_per_share_plot_data) == 0: raise NoEbitData()
        except NoEbitData:
            print("no ebit data skip")
            pass

def get_data_from_file(filename):

    if os.path.isfile(filename):
        with open(filename) as json_file:
            income_statement = json.load(json_file)
    else:
        print("WARNING: alpha vantage was called but you filese are not found. Is get_alpha_data False? This should not be reached if get_alpha_data is True. maybe options fehlt für plot")

    return income_statement
def analyse_data_from_alpha_vantage(symbols : list):
    source = "alpha_vantage"
    print("------------------------")
    indicator_absolute_income_statement = ["grossProfit", "totalRevenue", "ebit", "netIncome", "incomeBeforeTax", "operatingIncome"]
    indicator_percentage_income_statement = ["researchAndDevelopment_to_totalRevenue","totalLiabilities_to_totalAssets"]
    test = ["grossProfit", "ebit"]

    for s in symbols:
        income_statement_filename = "income_statement_alpha_" + s + ".json"

        income_statement = get_data_from_file(income_statement_filename)

        annual_absolute_data_per_symbol = []
        quaterly_absolute_data_per_symbol = []
        quaterly_relative_data_per_symbol =[]

        for i in indicator_absolute_income_statement:
            try:
                annual_absolute_data_per_symbol.append(get_annual_report_alpha(income_statement, i, symbol=s))
            except:
                print("error in annual data per symbol {}".format(s))

            try:
                quaterly_absolute_data_per_symbol.append(get_quaterly_report_alpha(income_statement, i, symbol=s))
            except:
                print("error in quaterly data {}".format(s))

        for s in symbols:
            balance_sheet_filename = "balance_sheet_alpha_" + s + ".json"

            # TODO give these separate filenames and then read the json file oder enter the else
            # cash_flow = request_cash_flow_from_alpha(s)
            # earnings =request_earnings_from_alpha(s)
            # overview = request_overiew_from_alpha(s)

            if os.path.isfile(balance_sheet_filename):
                with open(balance_sheet_filename) as json_file:
                    balance_sheet = json.load(json_file)
            else:
                print(
                    "WARNING: alpha vantage was called but you filese are not found. Is get_alpha_data False? This should not be reached if get_alpha_data is True. maybe options fehlt für plot")
                calling_alpha_vantage_api(symbols)

        try:
            # quotient: research and development:
            research = get_quaterly_report_alpha(income_statement, "researchAndDevelopment", symbol=s)
            revenue = get_quaterly_report_alpha(income_statement, "totalRevenue", symbol=s)
            res = []
            res.append(research[0])

            #convert to int
            research = [int(x) for x in research[1]]

            revenue = [int(x) for x in revenue[1]]

            quotient = [(x / y)*100 for x, y in zip(research,revenue)]
            res.append(quotient)
            res.append(s)
            res.append("researchAndDevelopment_to_totalRevenue")

            # format for res: [time_points, value_points, symbol, indicator]
            quaterly_relative_data_per_symbol.append(res)


        except:
            print("calculate quotient of two absolute indicators (research and developement to totalrevenue not working")

        try:
            # quotient: totalAssets to total Liabilites: - balance sheet
            totalLiabilities = get_quaterly_report_alpha(balance_sheet, "totalLiabilities", symbol=s)
            totalAssets = get_quaterly_report_alpha(balance_sheet, "totalAssets", symbol=s)
            res = []
            res.append(totalAssets[0])

            #convert to int
            totalLiabilities = [int(x) for x in totalLiabilities[1]]
            totalAssets = [int(x) for x in totalAssets[1]]

            quotient = [(x / y)*100 for x, y in zip(totalLiabilities,totalAssets)]
            res.append(quotient)
            res.append(s)
            res.append("totalLiabilities_to_totalAssets")

            quaterly_relative_data_per_symbol.append(res)


        except:
            print("calculate quotient of two absolute indicators total Assets / to total Liabilites not working")
        # filter_plot_data_list_per_symbol(annual_data_per_symbol, source)

        filter_plot_data_list_per_symbol(quaterly_absolute_data_per_symbol,False, source)
        filter_plot_data_list_per_symbol(quaterly_relative_data_per_symbol, True,source)



    pass


def get_data_from_finnhub():
    source = "finnhub"
    all_plot_data = []
    all_plot_data_test = []

    # TODO switch annual or quaterly
    period = 'annual'
    period = 'quarterly'

    symbol_dax_stocks = ["BAS.DE",
                         "SIE.DE",
                         "BAYN.DE",
                         "IFX.DE",
                         "1COV.DE",
                         "LIN.DE",
                         "BEI.DE",
                         "HEN3.DE",
                         ]
    # ALV.DE, "DBK.DE",

    automotive_dax_stocks = ["DAI.DE",
                             "BMW.DE",
                             "VOW.DE"]
    test_symbol = ["BAS.DE"]

    for s in automotive_dax_stocks:
        data_per_symbol = []
        print(s)

        fundamental_data_json = get_fundamental_data_from_finnhub(s)

        indicator_absolute_list = ["grossMargin"]  # netMargin
        indicators_per_share = ["eps", "ebitPerShare"]
        indicators_ratio = ["cashRatio", "currentRatio"]
        indicators_percentage = ["totalDebtToEquity"]

        for i in indicator_absolute_list:
            try:
                data_per_symbol.append(
                    get_one_absolute_indicator_from_finnhub(fundamental_data_json, period, i, s))
            except:
                print(" no {} data for {} ".format(i, s))
        for i in indicators_per_share:
            try:
                data = get_one_absolute_indicator_from_finnhub(fundamental_data_json, period, i, s)
                data_per_symbol.append(data)
            except:
                print("no {} data for {} ".format(i, s))
        for i in indicators_ratio:
            try:
                data_per_symbol.append(
                    get_one_ratio_indicator_from_finnhub(fundamental_data_json, period, i, s))
            except:
                print("no {} data  for  {} ".format(i, s))
        for i in indicators_percentage:
            try:
                data_per_symbol.append(
                    get_one_relative_indicator_from_finnhub(fundamental_data_json, period, i, s))
            except:
                print("no {} data  for  {} ".format(i, s))

        filter_plot_data_list_per_symbol(data_per_symbol, source)
        all_plot_data.append(data_per_symbol)


# SWITCHES:
analyse_finnhub_data = False
get_alpha_data = False
analyse_alpha_data = True
alpha_vantage_symbols = ["AVGO"]  # "IBM", "AAPL"

if __name__ == '__main__':

    if analyse_finnhub_data:
        get_data_from_finnhub()

    if get_alpha_data:
        calling_alpha_vantage_api(alpha_vantage_symbols)

    if analyse_alpha_data:
        analyse_data_from_alpha_vantage(alpha_vantage_symbols)
