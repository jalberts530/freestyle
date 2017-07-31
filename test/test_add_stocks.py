
stocks = []

my_stocks = input("My Stocks: ")
stocks.append(my_stocks)

while True:
    if my_stocks == "Done":
        print("I'm Done")
        break
    else:
        stocks.append(my_stocks)
    print(stocks)

#print(stocks)

#running_total = 0

#for stock in stocks:
#    stocks = lookup_stock_price(my_stocks)
#    running_total += product["price"]
#    price_usd = ' (${0:.2f})'.format(product["price"])
#    print(" + " + product["name"] + price_usd)
