# stock-data-collector
Class used to collect stock market data from yahoo's api, yfinance.

## Methods
* StockCollector.collect(START_DATE, END_DATE)
    
    Takes 2 string inputs as start and end dates to collect
    data from yfinance api and creates and stores pandas dataframe for each stock given
    in object dict attribute `stock_df`.

    ### Parameters:
        START_DATE : string
            'YYYY-MM-DD' format, of date collector will start collectiong data from.
        
        END_DATE : string
            'YYYY-MM-DD' format, of date collector will collect data up to.
        
        EXAMPLE: 'StockCollector.collect('2020-01-01', '2021-01-01')',
        would collect 1 years worth of data between the given dates. 

* StockCollector.collect_days(DAYS)

    Takes integer of days worth of data to collect from yfinance api.

    ### Parameters:
        DAYS : integer
            number of days of data to collect from todays date.
            
        EXAMPLE: `StockCollector.collect_days(7)`,
        would collect the past 7 days of the given stocks market data.