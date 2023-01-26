import pandas as pd
import yfinance as yf
from datetime import date, timedelta

class StockCollector:
    '''
    Creates collector object with 2 methods. 'collect' and 'collect_days'.
    '''
    def __init__(self, stocks):
        self.stocks = stocks
        self.stock_df = {}

    def collect(self, start_date, end_date):
        '''
        Takes start and end date in YYYY-MM-DD string format and returns pandas dataframe.
        '''
        for stock in self.stocks:
            df = self.download(stock, start_date, end_date)
            self.stock_df[stock] = self.set_df_index(df)

    def collect_days(self, days):
        '''
        Takes integer of how many days of data to collect, then returns pandas dataframe.
        '''
        dates = self.generate_dates(days)
        for stock in self.stocks:
            df = self.download(stock, dates['start_date'], dates['end_date'])
            self.stock_df[stock] = self.set_df_index(df)

    def download(self, stock, start_date, end_date):
        return yf.download(
            stock, 
            start=start_date, 
            end=end_date, 
            progress=False,
        )

    def generate_dates(self, days):
        d1 = date.today()
        d2 = date.today() - timedelta(days=days)
        return {
            "start_date": d2.strftime("%Y-%m-%d"),
            "end_date": d1.strftime("%Y-%m-%d"),
        }

    def set_df_index(self, df):
        df["Date"] = df.index
        df = df[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
        df.reset_index(drop=True, inplace=True)
        return df