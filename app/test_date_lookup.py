import csv
from pandas_datareader import data
from datetime import datetime
from datetime import date, timedelta
import datetime
from dateutil.parser import parse

csv_file_path = "data/stockprice.csv"

#Stock List
stock_symbols = []
my_stocks = []
stock_symbol = []
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
print("INVEST     | Determine Investment Value")
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
    print("Goodbye! Thanks for using Alberts Equity Researh. Come back soon!")


def operation_invest():
    symbol =input("Please select a stock by symbol: ")
    symbol = symbol.upper()
    stock_symbols.append(symbol)

    date_start = input("When did you buy the stock? input in the format yyyy-mm-dd: ")
    end_date = input("When did you sell the stock? input in the format yyyy-mm-dd: ")

    date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    number_of_stocks = input("Please input quantity of shares owned: ")
    number_of_stocks = float(number_of_stocks)
    data_source = 'google'

    response = data.DataReader(stock_symbols, data_source, date_start, date_start)
    response2 = data.DataReader(stock_symbols, data_source, end_date, end_date)

    daily_closing_prices = response.ix["Close"]
    daily_closing_prices2 = response2.ix["Close"]
    if daily_closing_prices.empty or daily_closing_prices2.empty:
        print("\nThe market was closed that day. Try a different date.\n ")
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



#Menu If Statements
if chosen_operation == "Invest": operation_invest()

elif chosen_operation == "Exit": operation_exit()
#elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
