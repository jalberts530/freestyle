
#Stock List
my_stocks = []
stock_symbols = []

#
#MENU
#
print("---------------------------------------")
print("Welcome to Alberts Equity Research")
print("---------------------------------------")
#print("Date: " + datetime.datetime.now().strftime("%Y-%m-%d") + " " + "Time: " + datetime.datetime.now().strftime("%H:%m:%S"))
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
    running_total = 0
    print("Please input the requested variables: ")
    my_stock_symbol = input("Stock Symbol:")
    number_of_shares = input("Number of Shares:")
    price = input("Purchase Price:")
    price_now = 100
    investment_detail = {
        "Symbol": my_stock_symbol,
        "# of Shares": len(number_of_shares),
        "Purchase Price": price,
        "Current Price": price_now
    }
    stock_symbols.append(my_stock_symbol)

    number_of_shares = int(number_of_shares)
    price_now = int(price_now)
    price = int(price)

    investment_value = (price_now-price)*number_of_shares


    print(investment_detail)
    print("\n")
    print("Your Investment in ", my_stock_symbol, " equals: ", investment_value)




#    for stock_symbol in stock_symbols:
#        running_total += stock["price"]
#        price_usd = ' (${0:.2f})'.format(product["price"])
#        print(" + " + stock_symbol["name"] + price_usd)









#Menu If Statements
if chosen_operation == "Invest": operation_invest()
elif chosen_operation == "Exit": operation_exit()
#elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
