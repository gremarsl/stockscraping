import os

from general_functions import pdf_merger
from structure_data import stockDataPlots

from plotter import Plotter
from processor import Processor


def main():
    # TODO falsche fehlermeldung
    # New Folder for ticker GOOGL has been created at C:\Users\marce\PycharmProjects\stockscraperFinnhub\AAPL\

    # TODO live market cap
    symbol_list = ["NVDA"]
    data = stockDataPlots(symbol_list[0])
    data.getCurrentYahooData()

    folder_path = os.getcwd() + f"\\{symbol_list[0]}\\"

    # TODO append works already?
    data.updateLocalData(folder_path)

    file_list = [
        os.getcwd() + f"\\{symbol_list[0]}\\{symbol_list[0]}\\" + "balanceSheetQuarterly.csv",
        os.getcwd() + f"\\{symbol_list[0]}\\{symbol_list[0]}\\" + "cashflowQuarterly.csv",
        os.getcwd() + f"\\{symbol_list[0]}\\{symbol_list[0]}\\" + "incomeStatementQuarterly.csv"]

    Processor.merge_csv_files(file_list, symbol_list)

    plotter = Plotter(symbol_list[0])

    plotter.plot_all()

    # TODO this is a possible method
    pdf_merger(os.getcwd()+ f"\\{symbol_list[0]}")


# ----------------------------------------------------------------------------------------------------------------------
# Entrypoint
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
