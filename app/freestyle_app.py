#import csv
import datetime

menu = '''
---------------------------------------
Welcome to Alberts Financial Management
---------------------------------------
'''

print("Date: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"))
#Time:

menu_2 = '''
Operations   Description
MSummary   | Markey Summary
SPrice     | Look up a stock price
IValue     | Determine Investment Value
PValue     | Determine Current Portfolio Value


'''



print(menu + menu_2)
stock = input("Input Stock Symbol: ")
print(stock)
