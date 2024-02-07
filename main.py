import yfinance as yf
import requests
from prettyprinter import pprint
 
# Disable SSL certificate verification globally
requests.packages.urllib3.disable_warnings()
 
# Create a session with SSL verification disabled
session = requests.Session()
session.verify = False
 
company_name = input("Enter the company name here: ")
# Set the session for yfinance Ticker object


def companyname_to_symbol(company_name):
    return yf.Ticker(company_name).info['symbol']

msft = yf.Ticker(companyname_to_symbol(company_name), session=session)
 
# Now you can make requests using yfinance without SSL verification
# pprint(msft.info)
pprint(companyname_to_symbol(company_name))