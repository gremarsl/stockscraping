import os

from structure_data import stockDataPlots


def main():
    #TODO falsche fehlermeldung
    # New Folder for ticker GOOGL has been created at C:\Users\marce\PycharmProjects\stockscraperFinnhub\AAPL\
    ticker = "BAS.DE"
    google = stockDataPlots(ticker)

    print(google)
    google.getCurrentYahooData()

    folder_path = os.getcwd() + f"\\{ticker}\\"
    google.updateLocalData(folder_path)


# ----------------------------------------------------------------------------------------------------------------------
# Entrypoint
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
