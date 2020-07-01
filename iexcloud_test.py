# Import Modules
import pandas as pd
# import datetime
import json #> Import as dictionary
# import math
import os
# import statistics
# import urllib

# Import Packages
import requests
from dotenv import load_dotenv
import plotly
import plotly.graph_objs as go

load_dotenv()

api_key = os.environ.get("sandbox_publishable")

symbol = "AAPL" 

spxt_url = f"https://sandbox.iexapis.com/stable/stock/SPXT/chart/max?token={api_key}"
request_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/chart/max?token={api_key}"

spxt_response = requests.get(spxt_url)
response = requests.get(request_url) #get the url in question

spxt_parsed_response = json.loads(spxt_response.text)
parsed_response = json.loads(response.text) #convert json format to dictionary format

spxt_prices = pd.DataFrame(spxt_parsed_response)
selection_prices = pd.DataFrame(parsed_response) #convert the dictionary into a Pandas Dataframe

print(spxt_prices)

spxt_closing = spxt_prices["close"]
selection_closing = selection_prices["close"]

# plotly.offline.plot({
#         "data": [go.Scatter(x=dates, y=spxt_prices, y)],
#         "layout": go.Layout(title=f"{symbol.upper()} Time Series")
#         }, auto_open=True)    

