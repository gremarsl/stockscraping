import os

import pandas as pd

from structure_data import stockDataPlots

from plotter import Plotter


def merge_csv_files(file_list, symbol_list):
    try:
        for idx, symbol in enumerate(symbol_list):
            destination_file_path = os.getcwd() + "\\total_data_" + symbol + ".csv"

            frames = [pd.read_csv(f) for f in file_list]
            combined_csv = pd.concat(frames, axis="columns")
            combined_csv.to_csv(destination_file_path, index=True, encoding='utf-8-sig')
            print("merge was successful")
            return destination_file_path
    except:
        print("merge failed!")


def main():
    # TODO falsche fehlermeldung
    # New Folder for ticker GOOGL has been created at C:\Users\marce\PycharmProjects\stockscraperFinnhub\AAPL\
    company_ticker = "GOOGL"
    data = stockDataPlots(company_ticker)

    print(data)
    data.getCurrentYahooData()

    folder_path = os.getcwd() + f"\\{company_ticker}\\"

    # TODO append works already?
    data.updateLocalData(folder_path)

    symbol_list = ["GOOGL"]

    file_list = [
        os.getcwd() + f"\\{symbol_list[0]}\\{symbol_list[0]}\\" + "balanceSheetQuarterly.csv",
        os.getcwd() + f"\\{symbol_list[0]}\\{symbol_list[0]}\\" + "cashflowQuarterly.csv",
        os.getcwd() + f"\\{symbol_list[0]}\\{symbol_list[0]}\\" + "incomeStatementQuarterly.csv"]

    destination_file_path = merge_csv_files(file_list, symbol_list)

    plotter = Plotter(symbol_list[0])

    plotter.plot_all()


# ----------------------------------------------------------------------------------------------------------------------
# Entrypoint
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
