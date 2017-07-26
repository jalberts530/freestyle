
from pandas_datareader import data
from datetime import date, timedelta

# COMPILE REQUEST PARAMS

symbols = ['AAPL', 'MSFT']
data_source = 'google'
start = str(date.today() - timedelta(days=15)) #> '2017-07-09'
end = str(date.today()) #> '2017-07-24'

# ISSUE REQUEST
# ... see docs at https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

response = data.DataReader(symbols, data_source, start, end)

# PARSE RESPONSE

daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function

print(daily_closing_prices)
