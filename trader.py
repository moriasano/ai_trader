import datetime
import yfinance as yf
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


class StockData:

    def __init__(self, symbol):
        self.symbol = symbol
        self.raw_data = yf.Ticker(symbol)

        self.price_history = None
        self.get_price_data()

    def get_price_data(self, granularity='1d', days_ago=365):
        today = datetime.date.today()
        start_date = today - datetime.timedelta(days=int(days_ago))
        self.price_history = self.raw_data.history(start=start_date, end=today, interval=granularity)

    def generate_graph(self, x_axis="High"):
        self.price_history[x_axis].plot()
        plt.show()


if __name__ == '__main__':
    s = StockData("CSCO")

    s.generate_graph()
