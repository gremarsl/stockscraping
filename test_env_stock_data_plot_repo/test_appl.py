import os

from structure_data import stockDataPlots

from plotter import Plotter
from processor import Processor





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

    destination_file_path = Processor.merge_csv_files(file_list, symbol_list)

    plotter = Plotter(symbol_list[0])

    plotter.plot_all()


# ----------------------------------------------------------------------------------------------------------------------
# Entrypoint
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
