#import csv
import datetime

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
