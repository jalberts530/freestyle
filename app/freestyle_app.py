import csv
from pandas_datareader import data
from datetime import datetime
from datetime import date, timedelta
import datetime
from dateutil.parser import parse
import sys

csv_file_path = "data/stock_prices.csv"

#Stock List
portfolio = []
portfolio_shares = []
my_stocks = []
stock_shares = []
stock_symbol = []
stock_symbols = []
us_market_indexes = ["^DJI", "^GSPC", "^IXIC"]
#
#MENU
#
print("---------------------------------------")
print("Welcome to Alberts Equity Research")
print("---------------------------------------")
print("Date: " + datetime.datetime.now().strftime("%Y-%m-%d") + " " + "Time: " + datetime.datetime.now().strftime("%H:%m:%S"))
print("\n")
print("         ~MENU~")
print("Operations   Description")
print("MARKET     | US Market Summary")
print("PRICE      | Look up Stock Price(s) & Write to CSV")
print("INVEST     | Determine Investment Value")
#print("PORTFOLIO  | Determine Current Portfolio Value")
print("EXIT       | Leave the program")
print("---------------------------------------")
print("Disclaimer: All Data Provided by Yahoo & Google Finance")
print("\n")

chosen_operation = input("Please input an operation from the menu: ")
chosen_operation = chosen_operation.title()

while True:
    chosen_operation
    if chosen_operation == "EXIT":
        break
    else:
        break
print(chosen_operation)
#
#
#Operation Definitions
def operation_exit(): # Exit Program
    print("Goodbye! Thanks for using Alberts Equity Research. Come back soon!")

def operation_market():
    print("\n" + "~US Stock Market Index Summary Past 3 Days~")
    #Data Source from Panda Reader
    data_source = 'yahoo'
    start = str(date.today() - timedelta(days=3)) #> '2017-07-09'
    end = str(date.today()) #> '2017-07-24'
    response = data.DataReader(us_market_indexes, data_source, start, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
    daily_closing_prices = daily_closing_prices.round(2)
    print(daily_closing_prices) #figure how to format 2 decimal places

def operation_price(): #Show Stock Price for Past 3 Days
    print("Lookup stock price")
    while True:
        stock_lookup = input("Please input a valid Stock Symbol or DONE to exit: ")
        if stock_lookup == "DONE":
            print("Thanks All Done Here, See Data Below: ")
            break
        else:
            stock_symbol.append(stock_lookup)
    #Data Source from Panda Reader
    data_source = 'google'
    start = str(date.today() - timedelta(days=3)) #> '2017-07-09'
    end = str(date.today()) #> '2017-07-24'
    response = data.DataReader(stock_symbol, data_source, start, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
    print("~Closing Prices Past 3 Days~")
    print(daily_closing_prices)

    confirmation = input("\nWould you like to save this data to a file? (Y/N) ")
    confirmation = confirmation.upper()
    if confirmation == "Y":
        prices = daily_closing_prices.to_csv(csv_file_path)
        print("\nGreat! The data has been saved to data/stock_prices.csv\n")
    else:
        print("\nOK. The data is not saved\n")

def operation_invest(): #Michael Quarato Assisted with this part of the project
    symbol =input("Please select a stock by symbol: ")
    symbol = symbol.upper()
    stock_symbols.append(symbol)
    #Panda Dates
    date_start = input("When did you PURCHASE the stock? input in the format yyyy-mm-dd: ")
    end_date = input("When did you SELL the stock? input in the format yyyy-mm-dd: ")
    try:
        date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
       print("Invalid Date Format Has Been Input, Program has Closed")
       sys.exit()
    #Panda Data
    number_of_stocks = input("Please input quantity of shares owned: ")
    number_of_stocks = float(number_of_stocks)
    data_source = 'google'
    response = data.DataReader(stock_symbols, data_source, date_start, date_start)
    response2 = data.DataReader(stock_symbols, data_source, end_date, end_date)
    daily_closing_prices = response.ix["Close"]
    daily_closing_prices2 = response2.ix["Close"]

    if daily_closing_prices.empty or daily_closing_prices2.empty:
        print("\nThe market was closed on one/both of these days. Try a different date.\n ")
    else:
        print(daily_closing_prices)
        print(daily_closing_prices2)
        difference = daily_closing_prices2.values-daily_closing_prices.values
        difference = float(difference)
        perform = number_of_stocks*difference
        if daily_closing_prices2.values > daily_closing_prices.values:
            print("\nYour gain is: " + str('${0:.2f}'.format(perform)))
        else:
            print("\nYour loss is: " + str('${0:.2f}'.format(abs(perform))))

def operation_portfolio(): #Current Value of Portfolio (May Abadon)
    print("Calculate Current Portfolio Value up to 5 Stocks")

    while True:
        portfolio_stock = input("Input a stock symbol from your portfolio or DONE to exit: ")
        if portfolio_stock == "DONE":
            print("Thanks All Done Here!: ")
            break
        else:
            portfolio.append(portfolio_stock)
            print(portfolio)
    while True:
        portfolio_share_input = input("Input the number of shares to each correspond stock or DONE to exit: ")
        if portfolio_share_input == "DONE":
            print("Thanks All Done Here!: ")
            break
        else:
            portfolio_shares.append(portfolio_share_input)
            print(portfolio_shares)

    #portfolio_shares = int(portfolio_shares)

    #Data Source from Panda Reader
    data_source = 'google'
    start = str(date.today() - timedelta(days=1)) #> '2017-07-09'
    end = str(date.today()) #> '2017-07-24'
    response = data.DataReader(portfolio, data_source, start, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
    print(daily_closing_prices) #figure how to format 2 decimal places

    daily_closing_prices = daily_closing_prices.values

    #total_portfolio_value = (daily_closing_prices*portfolio_shares)

    total_portfolio_value = daily_closing_prices.mul(portfolio_shares, axis=0)
    print(total_portfolio_value)

#Menu If Statements
if chosen_operation == "Market": operation_market()
elif chosen_operation == "Price": operation_price()
elif chosen_operation == "Invest": operation_invest()
#elif chosen_operation == "Portfolio": operation_portfolio()
elif chosen_operation == "Exit": operation_exit()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
