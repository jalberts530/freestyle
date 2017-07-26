import csv
import datetime

csv_file_path = "data/stockprice.csv"

#MENU
print("---------------------------------------")
print("Welcome to Alberts Financial Management")
print("---------------------------------------")
print("Date: " + datetime.datetime.now().strftime("%Y-%m-%d"))
print("Time: " + datetime.datetime.now().strftime("%H:%m:%S"))
print("\n")
print("          MENU")
print("Operations   Description")
print("Market     | Market Summary")
print("Price      | Look up a stock price")
print("Invest     | Determine Investment Value")
print("Portfolio  | Determine Current Portfolio Value")
print("---------------------------------------")
print("All Data Provided by Google Finance")
print("\n")
operation = input("Please input an operation from the menu: ")
print(operation)


#Menu If Statements
if chosen_operation == "Market": operation_market()
elif chosen_operation == "Price": operation_price()
elif chosen_operation == "Invest": operation_invest()
elif chosen_operation == "Portfolio": operation_portfolio()
#elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
