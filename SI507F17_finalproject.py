from database import dataBaseConstuct
from retrieveData import retriveStockData
import pandas as pd
import plotly
from plotly import figure_factory as FF
from plotly.graph_objs import *
import plotly.graph_objs as go

# data base construction is used to initialize two tables describe in the file
# if cachData = True, we will cachData from the google fiance, otherwise we just
# use the cached data stored in the csv files under stock_dfs folder.

dataBaseConstuct(cachData = False)


def correlation_table(tickers):
	'''
		calculate the close price correlation table for selected stock
	'''
	df = pd.DataFrame()
	for ticker in stocks:
		df[ticker] = retriveStockData(ticker).info.close
	correlation = df.corr().values.tolist()
	trace = go.Heatmap(z = correlation, x = tickers, y = tickers)
	data=[trace]
	plotly.offline.plot(data, filename = 'correlation_table.html', auto_open=False)

stocks = ['GOOG','MSFT','IBM','AAPL','FB','ORCL','AMZN']
correlation_table(stocks)