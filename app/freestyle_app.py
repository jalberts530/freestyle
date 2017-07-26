import csv
import datetime # necessary?
import pandas_datareader.data as web # necessary?
from pandas_datareader import data
from datetime import date, timedelta

csv_file_path = "data/stockprice.csv"

#Stock List
my_stocks = []
us_market_indexes = ["^DJI", "^GSPC", "^IXIC"]
#test = ['AAPL','T','GOOGL'] Testing IDs


#MENU
print("---------------------------------------")
print("Welcome to Alberts Financial Management")
print("---------------------------------------")
print("Date: " + datetime.datetime.now().strftime("%Y-%m-%d") + " " + "Time: " + datetime.datetime.now().strftime("%H:%m:%S"))
print("\n")
print("        ~ MENU ~")
print("Operations   Description")
print("MARKET     | US Market Summary")
print("PRICE      | Look up a Stock Price")
print("INVEST     | Determine Investment Value")
print("PORTFOLIO  | Determine Current Portfolio Value")
print("---------------------------------------")
print("Disclaimer: All Data Provided by Google Finance")
print("\n")
chosen_operation = input("Please input an operation from the menu: ")
chosen_operation = chosen_operation.title()
print(chosen_operation)

#Operation Definitions
def operation_market():
    print("\n" + "~ US Stock Market Summary Past 3 Days ~")
    data_source = 'yahoo'
    start = str(date.today() - timedelta(days=3)) #> '2017-07-09'
    end = str(date.today()) #> '2017-07-24'
    response = data.DataReader(us_market_indexes, data_source, start, end)
    daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
    print(daily_closing_prices) #figure how to format 2 decimal places

def operation_price():
    print("Lookup stock price")
    #quote = web.get_quote_google([])
    #stocklookup = input("Input Stock Symbol: ")
    #print(stocklookup)


def operation_invest():
    print("Please input the requested variables: ")
    stock_symbol = input("Stock Symbol:")
    number_of_shares = input("Number of Shares:")
    purchase_date = input("Purchase Date:")
    investment_value = {
        "Symbol": stock_symbol,
        "# of Shares": len(number_of_shares),
        "Purchase Date": purchase_date,
    }
    print("Your Gain/(Loss) on ", stock_symbol) #,"is: " investment_value)
    #products.append(new_product)

def operation_portfolio():
    print("Portfolio Value")

#Menu If Statements
if chosen_operation == "Market": operation_market()
elif chosen_operation == "Price": operation_price()
elif chosen_operation == "Invest": operation_invest()
elif chosen_operation == "Portfolio": operation_portfolio()
#elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.") #insert reset ability


#packages to consider
# 1) tkinter package
# 2) pandas_datareader
# 3) send grid
