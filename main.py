import yfinance as yf
import requests
from prettyprinter import pprint
 

requests.packages.urllib3.disable_warnings()
 
session = requests.Session()
session.verify = False
 
symbol_input = yf.Ticker(input("enter company symbol: "), session=session)

info_keys = ['longName', 'industry', 'country', 'state', 'fullTimeEmployees', 'marketCap', 'exchange', 'totalRevenue', 'heldPercentInsiders']

info = {}
for key in info_keys:
    info[key] = symbol_input.info.get(key, None)

pprint(info)

# longName = symbol_input.info['longName']
# industry = symbol_input.info['industry']
# domicile_country = symbol_input.info['country']
# domicile_state = symbol_input.info['state']
# headcount = symbol_input.info['fullTimeEmployees']
# market_cap = symbol_input.info['marketCap']
# exchange = symbol_input.info['exchange']
# revenue = symbol_input.info['totalRevenue']
# retention = symbol_input.info['heldPercentInsiders']

# print(longName, industry, domicile_country, domicile_state, headcount, market_cap, exchange, revenue, retention)
