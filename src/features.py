import pandas as pd


def create_features(df):
    df = df.copy()

    df["Return"] = df["Close"].pct_change()
    df["Lag_1"] = df["Return"].shift(1)
    df["Lag_2"] = df["Return"].shift(2)

    df["MA_5"] = df["Close"].rolling(5).mean()
    df["MA_10"] = df["Close"].rolling(10).mean()

    df["Volatility"] = df["Return"].rolling(5).std()

    df["Target"] = (df["Return"].shift(-1) > 0).astype(int)

    df.dropna(inplace=True)

    return df
