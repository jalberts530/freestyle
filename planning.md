## Freestyle Project Planning Document

**Application Name:** Alberts Equity Research

# Application Objective:**
The objective of this application is to provide the user with information on the US Stock market.  The specific functionality of the application is described below.

# Functionality:
The application has the ability to run 4 unique operations.  The operations are called "MARKET", "PRICE", "INVEST" and "EXIT"

**Required API:** The pandas datareader Python Package
**Stock Market Data:**  Data acquired from Yahoo & Google Finance using the panda data reader

# Operation Descriptions:
1) The **"MARKET"** operation allows the user to get data on the closing positions of the Dow Jones (^DJI), S&P 500 (^GSPC) and NASDAQ (^IXIC) Stock Market Indices

2) The **"PRICE"** operation allows the user to get data on the closing price of a one or many stocks of the users choosing.
  a) The user can input as many stocks as they choose and the application will output the stock price information.
  b) The user also has the option to write the stock market data to a CSV file in the "data" folder if they choose.

3) The **"INVEST"** operation allows the user to determine the value of their stock market investment.
  a) The user is required to input the *stock symbol, purchase data, sell date and number of shares.*
  b) Once the above inputs have been entered the application will calculate the gain/loss on the investment.
  c) The user must make sure to enter the dates in the specified format and on days where the stock market was open.

4) The **"EXIT"** operation allows the user to close out of the application from the menu.

# Application INPUTS:
  1) Menu Operations
  2) Stock Symbols
  3) Stock Purchase Date
  4) Stock Sell Date
  5) Number of Shares sold

# Application OUTPUTS:**
  1) US Market Index Data from Panda Reader
  2) Stock Market Price Data from Panda Reader
  3) Ability to write stock market price data to CSV file
  4) Ability to calculate investment value (GAIN/LOSS) of a particular stock based on various inputs

# Application Screenshots:**
Open the Planning Folder to see the application screenshots.
