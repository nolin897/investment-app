# Import Modules
import pandas as pd
import datetime
import json #> Import as dictionary
import math
import os
import statistics

# Import Packages
from dotenv import load_dotenv
import plotly
import plotly.graph_objs as go
import requests

load_dotenv()

api_key = os.environ.get("API_KEY")

symbol = "AAPL"
breakpoint()
end = datetime.datetime.utcnow() #https://stackoverflow.com/questions/13890935/does-pythons-time-time-return-the-local-or-utc-timestamp
start = end - (1000*60*60*24*365)

prices = pd.read_json(f'https://finnhub.io/api/v1/stock/candle?symbol={symbol}&resolution=1&from={start}&to={end}&token={api_key}')
financials = pd.read_json(f'https://finnhub.io/api/v1/stock/metric?symbol={symbol}&metric=all&token={api_key}')

# print(financials.columns.tolist())
print(prices.columns.tolist())

# print(prices.head(5))

for index, row in prices.iterrows():
    timestamp = datetime.datetime.fromtimestamp(row["t"])
    print(index, timestamp.strftime('%Y-%m-%d %H:%M:%S'))

# timestamp = datetime.datetime.fromtimestamp(1572651420) #from https://www.tutorialspoint.com/How-to-convert-timestamp-string-to-datetime-object-in-Python
# print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
