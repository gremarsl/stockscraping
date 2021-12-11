import yfinance as yf




# get stock info



symbol = "MSFT"



def get_base_info_from_yahoo_finance(symbol):
    symbol_base = yf.Ticker(symbol)
    symbol_info = symbol_base.info

    return symbol_info

def get_last_price_for_symbol_from_yahoo_finance(symbol):
    ticker_yahoo = yf.Ticker(symbol)
    data = ticker_yahoo.history()
    last_quote = (data.tail(1)['Close'].iloc[0])

    return last_quote


def get_market_cap_from_yahoo_finance(symbol):
    symbol_info = get_base_info_from_yahoo_finance(symbol)
    value = symbol_info["marketCap"]

    return value