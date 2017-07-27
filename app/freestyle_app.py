import csv
import datetime # necessary?
import pandas_datareader.data as web # necessary?
from pandas_datareader import data
from datetime import date, timedelta

csv_file_path = "data/stockprice.csv"

#Stock List
my_stocks = []
stock_symbol = []
us_market_indexes = ["^DJI", "^GSPC", "^IXIC"]

#MENU
print("---------------------------------------")
print("Welcome to Alberts Financial Management")
print("---------------------------------------")
print("Date: " + datetime.datetime.now().strftime("%Y-%m-%d") + " " + "Time: " + datetime.datetime.now().strftime("%H:%m:%S"))
print("\n")
print("         ~MENU~")
print("Operations   Description")
print("MARKET     | US Market Summary")
print("PRICE      | Look up a Stock Price")
print("INVEST     | Determine Investment Value")
print("PORTFOLIO  | Determine Current Portfolio Value")
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

#Operation Definitions
def operation_exit(): # Exit Program
    print("Goodbye! Come back soon!")

def operation_market():
    print("\n" + "~US Stock Market Index Summary Past 3 Days~")
    #Data Source from Panda Reader
    data_source = 'yahoo'
    start = str(date.today() - timedelta(days=3)) #> '2017-07-09'
    end = str(date.today()) #> '2017-07-24'
    response = data.DataReader(us_market_indexes, data_source, start, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
    print(daily_closing_prices) #figure how to format 2 decimal places

def operation_price(): #Show Stock Price for Past 5 Days
    print("Lookup stock price")
    while True:
        stock_lookup = input("Please input a valid Stock Symbol or DONE to exit: ")
        if stock_lookup == "DONE":
            print("Thanks All Done Here!")
            break
        else:
            stock_symbol.append(stock_lookup)
    #Data Source from Panda Reader
    data_source = 'google'
    start = str(date.today() - timedelta(days=6)) #> '2017-07-09'
    end = str(date.today()) #> '2017-07-24'
    response = data.DataReader(stock_symbol, data_source, start, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
    print("~Closing Prices Past 5 Days~")
    print(daily_closing_prices)


def operation_invest():
    print("Please input the requested variables: ")
    my_stock_symbol = input("Stock Symbol:")
    #stock_symbol = stock_symbol.title
    number_of_shares = input("Number of Shares:")
    purchase_date = input("Purchase Date:")
    investment_value = {
        "Symbol": my_stock_symbol,
        "# of Shares": len(number_of_shares),
        "Purchase Date": purchase_date,
    }

    stock_symbol.append(my_stock_symbol)

    #Data Source from Panda Reader
    data_source = 'google'
    start = str(date.today() - timedelta(days=1)) #> '2017-07-09'
    end = str(date.today()) #> '2017-07-24'
    response = data.DataReader(stock_symbol, data_source, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function

    print("Your Gain/(Loss) on ", stock_symbol) #,"is: " investment_value)
    print(daily_closing_prices)
    #products.append(new_product)

def operation_portfolio():
    print("Portfolio Value")

#Menu If Statements
if chosen_operation == "Market": operation_market()
elif chosen_operation == "Price": operation_price()
elif chosen_operation == "Invest": operation_invest()
elif chosen_operation == "Portfolio": operation_portfolio()
elif chosen_operation == "Exit": operation_exit()
#elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")


#packages to consider
# 1) tkinter package
# 2) pandas_datareader
# 3) send grid
