# Binance API  

## Exploratory Data Analysis with Python and Binance  

### Step 1  

**INSTALL DEPENDENCIES**  

        !pip install python-binance  
        !pip install pandas # for financial analysis, working with data in tabular format  
        !pip install mplfinance  

**IMPORT DEPENDENCIES**  

        from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager  
        import pandas as pd  
        
### Step 3  

        tickers = client.get_all_tickers() - grabs all the tickers  

### Step 4  

        depth = client.get_order_book(symbol = "BTCUSDT") - gets the order book (price & volume)  
        depth_df.columns = ['Price','Volume'] # setting the column names - .columns is used to set column names  

> `depth_df.dtypes` returns the data types of each column in the DateFrame  

### Step 5  

        historical = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2011") - gets historical data per day from 1 Jan 2011  
        
### Step 6  

        hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1) - .apply converts the columns listed in numeric_columns into numeric values and the argument axis = 1 performs the method on the actual columns  

### Step 7  

        import mplfinance as mpf  
        hist_df_view = hist_df.set_index('Close time').tail(100) # last 100 rows  

        mpf.plot(hist_df_view, type = 'candle', 
                style = 'charles', 
                volume = True,
                title = 'BTCUSD last 100 days',
                mav = (10,20,30))  

---
