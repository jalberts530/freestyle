
from pandas_datareader import data
from datetime import date, timedelta

# COMPILE REQUEST PARAMS

stock_symbol =[]
my_stock_symbol = input("Input a Stock Ticker: ")
stock_symbol.append(my_stock_symbol)
#stock_symbol = stock_symbol.title()
#stock_symbol = []
#print = stock_symbol


#symbols = ['AAPL', 'MSFT']
data_source = 'google'
start = str(date.today() - timedelta(days=5)) #> '2017-07-09'
end = str(date.today()) #> '2017-07-24'

# ISSUE REQUEST
# ... see docs at https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

response = data.DataReader(stock_symbol, data_source, start, end)

# PARSE RESPONSE

daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function

print(daily_closing_prices)
