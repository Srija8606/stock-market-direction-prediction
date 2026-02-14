import yfinance as yf
import pandas as pd


def download_data(tickers, start, end):
    data = []

    for ticker in tickers:
        df = yf.download(ticker, start=start, end=end)
        df["Ticker"] = ticker
        data.append(df)

    combined = pd.concat(data)
    combined.reset_index(inplace=True)

    return combined
