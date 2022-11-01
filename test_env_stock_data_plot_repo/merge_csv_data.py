import os

import pandas as pd

import global_vars

symbol = "GOOGL"
symbol_list = ["GOOGL"]

file_list = [
    'C:\\Users\\marce\\PycharmProjects\\stockscraperFinnhub\\yahoo_info\\yahoo_df_quarterly_balance_sheet_GOOGL.csv',
    'C:\\Users\\marce\\PycharmProjects\\stockscraperFinnhub\\yahoo_info\\yahoo_df_quarterly_cashflow_GOOGL.csv',
    'C:\\Users\\marce\\PycharmProjects\\stockscraperFinnhub\\yahoo_info\\yahoo_df_quarterly_financials_GOOGL.csv']


file_list = [
    os.getcwd() + "\\a.csv",
    os.getcwd() + "\\b.csv",
    os.getcwd() + "\\c.csv"]
file_list = [
    os.getcwd() + "\\GOOGL\\GOOGL\\" + "balanceSheetQuarterly.csv",
    os.getcwd() + "\\GOOGL\\GOOGL\\" + "cashflowQuarterly.csv",
    os.getcwd() + "\\GOOGL\\GOOGL\\" + "incomeStatementQuarterly.csv"]


def merge_csv_file_list(file_list, s):

    concat_dest_file = global_vars.filepath_yahoo + "concat_" + s + ".csv"

    df0 = pd.read_csv(file_list[0])
    df1 = pd.read_csv(file_list[1])
    df2 = pd.read_csv(file_list[2])

    frames = [df0,df1,df2]

    concat_csv = pd.concat(frames, axis="columns")
    print(concat_csv)

    concat_csv.to_csv(concat_dest_file, index=True, encoding='utf-8-sig')


def merge_csv_file_list_new(file_list, symbol_list):
    for idx, symbol in enumerate(symbol_list):
        dest_file = global_vars.filepath_yahoo + "concat_new_" + symbol + ".csv"

        frames = [pd.read_csv(f) for f in file_list]
        combined_csv = pd.concat(frames,axis="columns")
        combined_csv.to_csv(dest_file, index=True, encoding='utf-8-sig')




merge_csv_file_list(file_list,symbol)

merge_csv_file_list_new(file_list,symbol_list)
