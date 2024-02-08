import yfinance as yf
import requests

# Disable SSL certificate verification globally
requests.packages.urllib3.disable_warnings()

# Create a session with SSL verification disabled
session = requests.Session()
session.verify = False

# Set the session for yfinance Ticker object
msft = yf.Ticker("LGVN", session=session)

# Now you can make requests using yfinance without SSL verification
print(msft.info)


def get_industry(ticker):
    industry = ticker.info.get('industry')
    if industry:
        print("Industry:", industry)
    else:
        print("Industry not found for", ticker)


#call function to get industry
get_industry(msft)


