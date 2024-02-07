import yfinance as yf

def main():
    # Replace 'AAPL' with any ticker symbol you want to fetch data for
    ticker_symbol = 'AAPL'
    
    # Fetching data for the specified ticker symbol
    stock_data = yf.Ticker(ticker_symbol)
    
    # Printing basic information about the stock
    print("Stock Info:")
    print("-----------")
    print("Ticker Symbol:", stock_data.info['symbol'])
    print("Company Name:", stock_data.info['longName'])
    print("Exchange:", stock_data.info['exchange'])
    print("Sector:", stock_data.info['sector'])
    print("Industry:", stock_data.info['industry'])
    print("\n")

    # Printing recent historical data
    print("Recent Historical Data (Last 5 days):")
    print("--------------------------------------")
    print(stock_data.history(period='5d'))
    
if __name__ == "__main__":
    main()
